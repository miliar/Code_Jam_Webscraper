import logging
from Helper import *

class Orchestra:
    
    _years = ['08','09','10','11','12','13','14','15','16','17']
    _language = 'Python'
    _URL = 'https://www.go-hero.net/jam/'
     
    def __init__(self, save_path):
        self._round_nr = 0
        self._problem_nr = 1
        self._dir_nr = 1
        self._save_path = save_path
        self._url = self._URL + f'{self._years[0]}/solutions/{self._round_nr}/{self._problem_nr}/{self._language}'
        self.problem_list = []
        self._logger = logging.getLogger(__name__)
        self._logger.info('Init Orchestra')
        
    def make_problem_list(self):
        self._logger.info('Making problem list')
        for year in self._years:
            self._init_new_year(year)
            while simple_get(self._url) is not None:
                while simple_get(self._url) is not None:
                    self.problem_list.append((year, self._round_nr, self._problem_nr, self._save_path + str(self._dir_nr)))
                    self._logger.debug('Appending--- year: %s roundnr: %s problemnr: %s savepath: %s',
                                       year, self._round_nr, self._problem_nr, self._save_path + str(self._dir_nr))
                    self._init_next_problem(year)
                self._init_next_round(year)
        self._logger.info('Finished problem list of %s items', len(self.problem_list))
    
    def _init_new_year(self, year):
        self._round_nr = 0
        self._problem_nr = 1
        self._url = self._URL + f'{year}/solutions/{self._round_nr}/{self._problem_nr}/{self._language}'
        
    def _init_next_round(self, year):
        self._round_nr += 1
        self._problem_nr = 1
        self._url = self._URL + f'{year}/solutions/{self._round_nr}/{self._problem_nr}/{self._language}'
        
    def _init_next_problem(self, year):
        self._problem_nr += 1
        self._url = self._URL + f'{year}/solutions/{self._round_nr}/{self._problem_nr}/{self._language}'
        self._dir_nr += 1
        

