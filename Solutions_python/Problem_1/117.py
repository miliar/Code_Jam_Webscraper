import sys
#import psyco

def solution(qu, nse):
    tmp = set()
    nswitch = 0
    for i in qu:
        tmp.add(i)
        if len(tmp) == nse:
            nswitch += 1
            tmp = set()
            tmp.add(i)
    return nswitch

def main():
    file = open(sys.argv[1], 'r')
    nc = int(file.readline())

    count = 1
    GET_SE_NUMBER = True
    GET_SE = False
    GET_QU_NUMBER = False
    GET_QU = False
    COUNT_SE = 0
    COUNT_QU = 0
    se = set()
    qu = []
    nqu = None
    for line in file:
        if GET_QU and COUNT_QU < nqu:
            qu.append(line.strip())
            COUNT_QU += 1

        if GET_QU_NUMBER:
            nqu = int(line.strip())
            GET_QU_NUMBER = False
            GET_QU = True

        if GET_SE and COUNT_SE < nse:
            se.add(line.strip())
            COUNT_SE += 1
            if COUNT_SE == nse:
                GET_SE = False
                COUNT_SE = 0
                GET_QU_NUMBER = True
        if GET_SE_NUMBER:
            nse = int(line.strip())
            GET_SE_NUMBER = False
            GET_SE = True

        if COUNT_QU == nqu:
            GET_QU = False
            COUNT_QU = 0
            GET_SE_NUMBER = True
            print 'Case #' + str(count) + ':', solution(qu, nse)
            count += 1
            se = set()
            qu = []
            nqu = None
        
if __name__ == "__main__":
    #g = psyco.proxy(main)
    #g()
    main()
