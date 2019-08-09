from tqdm import tqdm as progress_bar
import multiprocessing as mp
import logging
from webscraper.scraper import Scraper
from webscraper.orchestrator import make_problem_list


def scrape_all_problems(problem_tuple):
    scraper = Scraper(*problem_tuple)
    scraper.download_all()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='log.txt')
    problem_list = make_problem_list()
    with mp.Pool(mp.cpu_count()) as pool:
        list(progress_bar(pool.imap(scrape_all_problems,
                                    problem_list), total=len(problem_list)))
