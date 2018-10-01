string = [s.strip() for s in
          open('input3.txt').readlines()[1:] if len(s.strip())]


def get_chunk():
    for index, line in enumerate(string):
        yield [int(x) for x in line.split(' ')]


def get_next_palindrome(nbr):
    if nbr <= 8:
        return nbr + 1
    if nbr == 9:
        return 11
    nbr=str(nbr)
    centr=len(nbr)//2
    if len(nbr)%2:  #odd number
        a,b,c=int(nbr[0:centr]),int(nbr[centr]),int(nbr[len(nbr):centr:-1])
        if c>=a:
            d=str(int(str(a)+str(b))+1)
            e="0"*len(str(c))
            return get_next_palindrome(int(d+e))
        else:
            a=str(a)
            b=str(b)
            c=str(str(a)[::-1])
            return int(a+b+c)

    else:  #even number
        d=int(nbr[0:centr])
        e=(nbr[len(nbr):centr-1:-1])
        if int(e)>=d:
            d=str(d+1)
            e="0"*len(e)
            return get_next_palindrome(int(str(d+e)))
        else:
            d=str(d)
            e=str(str(d)[::-1])
            return int(d+e)

def check_square_palindrome(n):
    check = n * n
    if str(check) == str(check)[::-1]:
        return 1
    return 0


def solve(chunk):
    import math
    A, B = chunk
    A = int(math.ceil(math.sqrt(A)))
    B = int(math.sqrt(B))
    found = 0
    i = A
    if str(i) == str(i)[::-1]:
        found += check_square_palindrome(i)
        i = get_next_palindrome(i)
    else:
        i = get_next_palindrome(i)

    while i <= B:
        found += check_square_palindrome(i)
        i = get_next_palindrome(i)
    return found

for index, chunk in enumerate(get_chunk()):
    print 'Case #%s:' % (index + 1), solve(chunk)
    # break
