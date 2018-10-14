import logging
from helper import *
from config import *

def _get_url_adress(year, round_nr=0, problem_nr=1):
        return URL + f'{year}/solutions/{round_nr}/{problem_nr}/{LANGUAGE}'
    
def make_problem_list():
        logger = logging.getLogger(__name__)
        logger.info('Making problem list')
        problem_list = []
        dir_nr = 1
        
        for year in YEARS :
            round_nr = 0
            problem_nr = 1
            url = _get_url_adress(year)
            while simple_get(url) is not None:
                while simple_get(url) is not None:
                    problem_list.append((year, round_nr, problem_nr, SAVE_PATH + str(dir_nr)))
                    problem_nr += 1
                    dir_nr += 1
                    url = _get_url_adress(year, round_nr, problem_nr)
                round_nr += 1
                problem_nr = 1
                url = _get_url_adress(year, round_nr, problem_nr)
                
        logger.info('Finished problem list of %s items', len(problem_list))
        return problem_list
                    