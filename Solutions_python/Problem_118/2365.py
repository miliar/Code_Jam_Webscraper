import math

liste_palindrome = set()
liste_non_palindrome = set()
liste_carre = set()
liste_non_carre = set()

def is_palindrome(a):
    if len(str(a)) == 1:
        return True
    if a in liste_palindrome:
        return True
    if a in liste_non_palindrome:
        return False
    A = str(a)
    for i in range(len(str(a)) // 2):
        if A[i] != A[-(i+1)]:
            liste_non_palindrome.add(a)
            return False
    liste_palindrome.add(a)
    return True

def is_a_carre(b):
    sq = int(math.sqrt(a))
    if math.pow(sq, 2) == a:
        return True
    return False

def is_carre(a):
    if a in liste_carre:
        return True
    if a in liste_non_carre:
        return False
    sq = int(math.sqrt(a))
    if math.pow(sq, 2) == a:
        if is_palindrome(sq):
            liste_carre.add(a)
            return True
        else:
            return False
    else:
        liste_non_carre.add(a)
        return False
    
import sys
f = sys.stdin
T = int(f.readline()) + 1
for tc in range(1, T):
    [a, b] = [int(x) for x in f.readline().rstrip('\r\n').split()]
    lr=0    
    for i in range(a, b + 1):
        if is_palindrome(i) and is_carre(i):
            lr += 1
    print 'Case #{tc}: {lr}'.format(tc=tc, lr=lr)
