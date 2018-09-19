def process(vals):
    if reduce(lambda x,y: x^y,vals) != 0: return 'NO'
    return str(sum(vals) - min(vals))

def main():
    for case in xrange(1,int(raw_input())+1):
        candy = int(raw_input())
        vals = [int(x) for x in raw_input().split(' ')]
        print 'Case #%d: %s' %(case,process(vals))
    
if __name__ == "__main__":
    main()
