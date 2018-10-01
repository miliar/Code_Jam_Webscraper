from math import sqrt
from math import pow


        
def getPoint(a,b,c):
    return [(a[0]+b[0]+c[0]), (a[1]+b[1]+c[1])];
def solve(xxx):

    [n, A, B, C, D, x0, y0, M] = xxx;
    x=x0;
    y=y0;
    mas = [[x,y]];
    for i in range(n-1):
        x=(A*x+B) % M;
        y=(C*y+D) % M;
        mas.append([x,y]);
        #print x,y;
    mas2=[[xx*3,yy*3] for [xx,yy] in mas];

    #print xxx;
    #print n, A, B, C, D, x0, y0, M;
    #print x,y;
    #print mas;
    #print mas2;

    cnt = 0;
    cnt2 = 0;
    cnt3 = 0;
    for i1 in range(len(mas)):
        for i2 in range(i1+1, len(mas)):
           for i3 in range(i2+1, len(mas)):
              center= getPoint(mas[i1], mas[i2], mas[i3]);
              if ((center[0] % 3 == 0) & (center[1] % 3 ==0)):
                  cnt3 +=1;
              #try:
              #    ind = mas2.index(center)
              #except ValueError:
              #    ind = -1 # no match

              #print i1, i2, i3, center, ind;    
              #if (ind != -1):
              #    cnt += 1;
              #    print "found", i1, i2, i3, center, ind;
              #if ((ind != -1) & (ind != i1) & (ind != i2) & (ind != i3)):
              #    cnt2 += 1;
              #    print "spec", i1, i2, i3, center, ind;
              
    return cnt3;




def solveAll():
    name="A-small-attempt2";
    
    fi=open("C:/" + name + ".in", "r");
    fo=file("C:/" + name + ".out", "w");

    n=int(fi.readline());
    print "n", n;
    
    for i in range(n):
        xxx=[int(xx) for xx in fi.readline().split(" ")];
        
        rez=solve(xxx);
        print "rez", rez;   

        rezString="Case #%s: %s\n" % ((i+1), rez);
        print rezString;
        fo.write(rezString);

    fo.close();


solveAll()


