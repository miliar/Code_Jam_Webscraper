import sys
def check(pat,r,c):
    possible=True
    for i in range(r):
        for j in range(c):
            if (pat[i][j]=='#'):
                if(i+1<r and j+1< c and pat[i+1][j] == '#' and pat[i][j+1]=='#' and pat[i+1][j+1]=='#'):
                   pat[i][j]='/'
                   pat[i][j+1]='\\'
                   pat[i+1][j]='\\'
                   pat[i+1][j+1]='/'
                else:
                    possible=False
                    return possible
    return possible

ifile = open('a-small.in','r')
ofile = open('a-small.out','w')
sys.stdin = ifile
c = int(input())
for i in range(c):
    r,c = [int(i) for i in input().split()]
    pat = []
    for j in range(r):
        row = list(input())
        pat.append(row)
    print("Case #%s:" %(i+1,),file=ofile)
    possible = check(pat,r,c)        
    if not possible:
        print("Impossible",file=ofile)
    else:
        pat = [''.join(k) for k in pat]
        for k in pat:
            print(k,file=ofile)  
                
ifile.close()
ofile.close()
