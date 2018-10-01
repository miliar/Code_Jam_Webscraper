import sys

def main(argv):
    file = open(argv[1])
    case = 0
    for line in file:
        if (case == 0):
            case = 1
            continue
        strin = 'Case #%d: ' % case
        case += 1
        x = line.split()
        a = int(x[0])
        b = int(x[1])
        map = {}
        i = a
        res = 0
        while (i <= b):
            if map.get(i, 0) == i: continue
            y = str(i)
            tmp = 0
            for j in range(0, len(y)):
                if int(y) >= a and int(y) <= b and map.get(int(y), 0) == 0:
                    tmp += 1
                map[int(y)] = 1
                y = y[1:] + y[0]
            res += (tmp*(tmp-1))/2
            i+=1
        strin += str(res)
        print strin
     
if __name__ == "__main__":
    main(sys.argv)