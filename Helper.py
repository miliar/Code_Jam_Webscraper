from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import logging


def simple_get(url):
    
    logger = logging.getLogger(__name__)

    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                logger.debug('Good response on %s', url)
                return resp.content
            else:
                logger.debug('Bad response on %s', url)
                return None

    except RequestException :
        logger.exception('Error during requests to %s', url)
        return None

def is_good_response(resp):
    
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

