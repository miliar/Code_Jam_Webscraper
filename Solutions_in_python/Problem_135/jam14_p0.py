'''
Code jam 2014: A. Magic Trick
'''
def main():
    f = open('/home/ayush/A-small-attempt0.in','r')
    o = open("/home/ayush/Downloads/output.txt",'w')
    t=int(f.readline())
    x=0
    while t:
        t-=1
        x+=1
        fa = int(f.readline()) #first answer
        grid = []
        for q in xrange(4):
            grid.append(map(int,f.readline().split()))
        sa = int(f.readline()) #second answer
        grid2 = []
        for q in xrange(4):
            grid2.append(map(int,f.readline().split()))
        match=0
        for p in grid[fa-1]:
            if p in grid2[sa-1]:
                ans = p;match+=1
        if match>1:
            s='Case #%d: Bad magician!\n' %x
            o.write(s)
        elif match==1:
            s= 'Case #%d: %d\n' %(x,ans)
            o.write(s)
        else:
            s= 'Case #%d: Volunteer cheated!\n' %x
            o.write(s)
main()
