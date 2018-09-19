import math
from reverse_string import reverse

def is_square(n):
    raiz = math.sqrt(n)
    if int(raiz) != raiz:
        return False
    s = str(int(raiz))
    if reverse(s)==s:
        return True

    return False
    
