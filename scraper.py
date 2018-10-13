from bs4 import BeautifulSoup
import re
import zipfile
import io
import pathlib
import logging
from helper import *
from config import *

class Scraper:
    
    def __init__(self, year, round_nr, problem_nr, save_path):
        self.save_path = save_path
        self.url = URL + f'{year}/solutions/{round_nr}/{problem_nr}/{LANGUAGE}'
        self._logger = logging.getLogger(__name__)
    
    def download_all(self):
        pathlib.Path(self.save_path).mkdir(parents=True, exist_ok=True)
        links = self.get_all_download_links()
        self._download_files(links)
        
    def get_all_download_links(self):
        main_page = simple_get(self.url)
        download_links = self._get_download_links_from_page(main_page)
        
        page = 1
        sub_page = simple_get(self.url + f'/partial/{page}')
        while sub_page is not None:
            download_links.extend(self._get_download_links_from_page(sub_page))
            page += 1
            sub_page = simple_get(self.url + f'/partial/{page}')
        
        self._logger.info('Saved %s download links for %s', str(len(download_links)), self.url)
        return download_links
        
        
    def _get_download_links_from_page(self, url_content):
        download_links = []
        html = BeautifulSoup(url_content, PARSER)
        
        for link_text in html.select('a'):
            link = self._extract_download_link_from_text(link_text)
            if link is not None:
                download_links.append(link)
                
        return download_links
                
    def _extract_download_link_from_text(self, text):
        try:
            download_link = "https://code" + re.search('"http://code(.*?)"', str(text)).group(1)
            download_link = re.sub("&amp;", "&", download_link)
            return download_link
        
        except AttributeError:
            self._logger.debug('Failed extracting download link from %s', text)
            return None
        
    def _download_files(self, download_links):
        for nr, link in enumerate(download_links):
            save_path = f'{self.save_path}/{nr}.py'
            try:
                zip_link = get(link, stream=True)
                with zipfile.ZipFile(io.BytesIO(zip_link.content)) as zip_file:
                    with open(save_path,"wb") as extracted_file:
                        extracted_file.write(zip_file.read(zip_file.namelist()[0]))
            except:
                self._logger.warning('Failed downloading %s',link)
                
        count_files = len([file for file in pathlib.Path(self.save_path).glob('*.py')])
        self._logger.info('Download %s files for %s', count_files, self.url)
                
                

