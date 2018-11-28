#include  <iostream>
#include <cmath>
using namespace std;

bool rec(int x, int y)
{

    if (x==y) return false;
    if (x>2*y) return true;
    if (x>y) swap(x,y);    
    return !rec(x,x-y);
}

int main()
{
    FILE *fin=fopen("c-large.in", "rt");
    FILE *fout=fopen("c-large.out", "wt");
    int t, a1,a2,b1,b2;    
    fscanf(fin, "%d",&t);
    for (int i1=1; i1<=t; i1++)
    {
    fscanf(fin, "%d%d%d%d",&a1,&a2,&b1,&b2);        
    long long int res=0;
    for (int i=a1; i<=a2; i++)
    {
        int x1, x2;
        x1=ceil(i*((sqrt(5)-1)/2));
        x2=floor(i*((sqrt(5)+1)/2));
        int y1,y2;
        y1=max(x1,b1);
        y2=min(x2,b2);
        res+=(b2-b1)+1-max(0,y2-y1+1);
    }
    fprintf(fout, "Case #%d: %lld\n", i1, res);
    }        
fclose(fout);
    }
