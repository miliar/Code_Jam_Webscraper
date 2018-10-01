import math
def read_data (filename):
    r = open(filename)
    data = r.readlines()
    r.close()
    return data

def write_result (data,filename='result3.txt'):
    w = open(filename,'w')
    for i in data:
        w.write(i)
    w.close()

def is_prime (n):
    s = str(n)
    length = len(s)
    for i in range(length/2):
        if s[i] != s[length-i-1]:
            return False
    return True

def cal_prime_square(start,end):
    prime_num = 0
    for i in range(start,end+1):
        tmp = math.sqrt(i)
        if abs(int(tmp)-tmp) < 0.00001:
            if is_prime(i) and is_prime(int(tmp)):
                prime_num += 1
    return prime_num

def search (data):
    testcases = int(data[0])
    results = []
    k = 1
    while k <= testcases:
        n,m = map (int,data[k].strip().split())
        results.append ('Case #%d: %d\n' % (k,cal_prime_square(n,m)))
        k+= 1
    write_result (results)

#search(read_data('c.txt'))
search(read_data('C-small-attempt0.in'))

