import re

def main():
    filename = 'B-small-attempt2'
    
    inf = open(filename + '.in', 'r')
    outf = open(filename + '.out', 'w')
    for i, line in enumerate(inf):
        values = line.split()
        print values
        if i == 0:
            T = int(values[0]) # number of test cases
            print T
            continue
        if i <= T:
            p = 0
            C = int(values[p])
            p += 1
            if C > 0:
                strC = values[p]
                p += 1
            D = int(values[p])
            p += 1
            if D > 0:
                strD = values[p]
                p += 1
            N = int(values[p])
            p += 1
            strN = values[p]
        else:
            continue
        
        
        elements = []
        
        # invoke
        for j in range(len(strN)):
            if j == 0:
                elements.append(strN[j])
                continue
            
            # combine
            if C > 0 and len(elements) > 0:
                if strC[0] == strN[j] and strC[1] == elements[-1]:
                    elements[-1] = strC[2]
                    continue
                elif strC[1] == strN[j] and strC[0] == elements[-1]:
                    elements[-1] = strC[2]
                    continue
                else:
                    pass
                
            # opposed
            if D > 0:
                try:
                    head = elements.index(strD[0])
                    if strN[j] == strD[1]:
                        elements = []
                        continue
                except ValueError, e:
                    try:
                        head = elements.index(strD[1])
                        if strN[j] == strD[0]:
                            elements = []
                            continue
                    except ValueError, e:
                        pass
#            if D > 0:
#                try:
#                    head = reindex(elements, strD[0])
#                    if strN[j] == strD[1]:
#                        elements = elements[:head]
#                        continue
#                except ValueError, e:
#                    try:
#                        head = reindex(elements, strD[1])
#                        if strN[j] == strD[0]:
#                            elements = elements[:head]
#                            continue
#                    except ValueError, e:
#                        pass
            
            elements.append(strN[j])
        
        buf = 'Case #%d: %s\n' % (i, re.sub("'", '', str(elements)))
        print re.sub('\n', '', buf)
        outf.write(buf)
    inf.close()

def reindex(list, value):
    for i in range(len(list)-1, -1, -1):
        if list[i] == value:
            return i
    raise ValueError

if __name__ == '__main__':
    main()
    
