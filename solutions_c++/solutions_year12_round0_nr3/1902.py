#include <cstdio>
#include <string>
#include <iostream>
#include <set>
#include <cmath>
#include <cstdlib>
#include <map>
#include <algorithm>
using namespace std;

#define FILEIO
string _input="C-large.in";

const int N=2000100;
int a[N][10];
int asz[N];

int main()
{
#ifdef FILEIO
    freopen(_input.c_str(),"r",stdin);
    freopen((_input+".txt").c_str(), "w", stdout);
#endif
    for(int i=1,b=10;i<N;i++)
    {
        if(i==b) b*=10;
        for(int ten=10;ten<=i;ten*=10)
        {
            int x=i%ten;
            int y=i/ten;
            int j=x*(b/ten)+y;
            if(j>i)
            {
                bool has=false;
                for(int f=0;f<asz[i];f++)if(a[i][f]==j){has=true;break;}
                if(!has)a[i][asz[i]++]=j;
            }
        }
    }
    int T; scanf("%d",&T);
    for(int IT=0;IT<T;IT++)
    {
        int A,B; scanf("%d%d",&A,&B);
        int result=0;
        for(int i=A;i<=B;i++)
        {
            for(int j=0;j<asz[i];j++)if(a[i][j]>=A&&a[i][j]<=B)result++;
        }
        printf("Case #%d: %d\n", IT+1,result);
    }
    return 0;
}
