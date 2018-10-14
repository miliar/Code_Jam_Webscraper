from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import logging


def simple_get(url):
    
    logger = logging.getLogger(__name__)
    content = None

    try:
        with closing(get(url, stream=True)) as resp:
            if _is_good_response(resp):
                content = resp.content
                
    except RequestException :
        logger.exception('Error during requests to %s', url)
    
    return content
    

def _is_good_response(resp):
    
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

