#!/usr/bin/python


def isValid(tmpStr, dict):
    for word in dict:
        if word.startswith(tmpStr):
            return True
    return False

def main():
    l, d, n = raw_input().split(' ')
    l = int(l)
    d = int(d)
    n = int(n)
    
    dict = set()
    for x in xrange(0, d):
        dict.add(raw_input())
    
    for x in xrange(1,n+1):
        line = raw_input()
        lista = ['']
        tmp = []
        mode = False
        for ch in line:
            if ch == '(':
                mode = True
            if ch == ')':
                lista = tmp
                tmp = []
                mode = False
            if ch.isalpha():
                for elem in lista:
                    tmpStr = elem + ch
                    if isValid(tmpStr, dict):
                        tmp.append(tmpStr)
                if not mode:
                    lista = tmp
                    tmp = []
        print "Case #" + str(x) + ": " + str(len(lista))

if __name__ == '__main__':
    main()