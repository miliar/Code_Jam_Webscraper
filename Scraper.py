from bs4 import BeautifulSoup
import re
import zipfile
import io
import pathlib
import logging
from Helper import *

class Scraper:
    
    _language = 'Python'
    _parser = 'html.parser'
    
    def __init__(self, year, round_nr, problem_nr, save_path):
        self.save_path = save_path
        self.url = 'https://www.go-hero.net/jam/' + f'{year}/solutions/{round_nr}/{problem_nr}/{self._language}'
        self.download_links = []
        self._logger = logging.getLogger(__name__)
        self._logger.info('Init Scraper for %s', self.url)
    
    def download_all(self):
        pathlib.Path(self.save_path).mkdir(parents=True, exist_ok=True)
        self.get_all_download_links()
        self._download_files()
        
    def get_all_download_links(self):
        self._logger.debug('Get all download links main page')
        main_page = simple_get(self.url)
        self._save_download_links_from_page(main_page)
        
        page = 1
        sub_page = simple_get(self.url + f'/partial/{page}')
        while sub_page is not None:
            self._logger.debug('Get all download links sub page: %s', str(page))
            self._save_download_links_from_page(sub_page)
            page += 1
            sub_page = simple_get(self.url + f'/partial/{page}')
        self._logger.info('Saved %s download links for %s', str(len(self.download_links)), self.url)
        
    def _save_download_links_from_page(self, url_content):
        html = BeautifulSoup(url_content, self._parser)
        for link_text in html.select('a'):
            link = self._extract_download_link_from_text(link_text)
            if link is not None:
                self._logger.debug('Appending link: %s', link)
                self.download_links.append(link)
                
    def _extract_download_link_from_text(self, text):
        try:
            download_link = "https://code" + re.search('"http://code(.*?)"', str(text)).group(1)
            download_link = re.sub("&amp;", "&", download_link)
            return download_link
        
        except AttributeError:
            self._logger.debug('Failed extracting download link from %s', text)
            return None
        
    def _download_files(self):
        for nr, link in enumerate(self.download_links):
            save_path = f'{self.save_path}/{nr}.py'
            self._logger.debug('Downloading file from %s as %s', link, save_path)
            try:
                zip_link = get(link, stream=True)
                with zipfile.ZipFile(io.BytesIO(zip_link.content)) as zip_file:
                    with open(save_path,"wb") as extracted_file:
                        extracted_file.write(zip_file.read(zip_file.namelist()[0]))
            except:
                self._logger.warning('Failed downloading %s',link)
                
        count_files = len([file for file in pathlib.Path(self.save_path).glob('*.py')])
        self._logger.info('Download %s files for %s', count_files, self.url)
                
                

