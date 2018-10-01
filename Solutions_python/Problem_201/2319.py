import sys
import math

def main():
    input_file = str(sys.argv[1])
    output_file = str(sys.argv[2])

    in_file = open(input_file, 'r')
    output_file = open(output_file, 'w')

    n = int(in_file.readline())
    l = 1

    for line in in_file:
        t = line.rstrip('\n')
        u = int(find_n(t))
        v = int(find_k(t))
        #print('n=',u,'\tk=',v,sep='')
        w = solve(n=u,k=v)
        #print(w)
        r = w[0]
        s = w[1]
        #print('n,k,x,i', u, v, r, s)
        output_file.write('Case #' + str(l) + ': ' + str(r) + ' ' + str(s) + '\n')
        l += 1
    in_file.close()
    output_file.close()

def find_n(x):
    a = ''
    for char in x:
        if char != ' ':
            a += char
        else:
            break
    return a

def find_k(x):
    a = ''
    found = False
    for char in x:
        if found == False:
            if char != ' ':
                continue
            else:
                found = True
        else:
            a += char
    return a

def solve(n,k):
    a = k + 1
    b = 0
    while a > 1:
        a = a // 2
        b += 1
    c = k + 1 - 2 ** b
    d = n + 1 - 2 ** b
    e = d // (2 ** b)
    f = math.ceil(d / (2**b))
    g = d % (2 ** b)
    if c == 0:
        if g >= (2**(b-1)):
            x = f
            y = e
        else:
            x = e
            y = e
    elif c <= g:
        x = math.ceil((f-1) / 2)
        y = (f-1) // 2
    else:
        x = math.ceil((e-1) / 2)
        y = (e-1) // 2
    #return [a,b,c,d,e,f,g,' ',n,k,' ',x,y]
    return [x,y]

main()
