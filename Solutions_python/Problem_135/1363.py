

def get_line():
    return raw_input().strip()

formatIntegerList = lambda s: list(map(int,s.split(' ')))

def standard_input():
    count = int(get_line())
    for i in range(count):
        c1 = int(get_line())
        g1 = [formatIntegerList(get_line()) for j in range(4)]
        c2 = int(get_line())
        g2 = [formatIntegerList(get_line()) for j in range(4)]
        yield (i+1,(c1,g1,c2,g2))
        
def handle_case(case):
    c1,g1,c2,g2 = case
    s = set(g1[c1 - 1]) & set(g2[c2 - 1])
    if len(s) == 0:
        return 'Volunteer cheated!'
    elif len(s) == 1:
        return s.pop()
    else:
        return 'Bad magician!'
        
def main():
    for i,case in standard_input():
        print "Case #%d: %s" %(i,handle_case(case))        

if __name__ == '__main__':
    main()
    