#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
bool check(int a,int b)
{
    int te=a;
    int len=0;
    while(te!=0)
    {
        len++;
        te/=10;
    }
    int i;
    for(i=1;i<len;i++)
    {
        int ww=1,t=i;
        while(t--) ww*=10;
        int _left=a/ww;
        int _right=a%ww;
        if(_right<(ww/10))
            continue;
        int get;
        ww=1;t=len-i;
        while(t--) ww*=10;
        get=_right*ww+_left;
        if(get==b)
            return true;
    }
    return false;
}
int main()
{
    FILE *fpr,*fpw;
    fpr=fopen("C-small-attempt0.in","rb");
    fpw=fopen("out.txt","wb");
    int A,B;
    int T,Case;
    int i,j;

    fscanf(fpr,"%d",&T);
    for(Case=1;Case<=T;Case++)
    {
        fscanf(fpr,"%d%d",&A,&B);
        int ans=0;
        for(i=A;i<B;i++)
        {
            for(j=i+1;j<=B;j++)
            {
                if(check(i,j))
                    ans++;
            }
        }
        fprintf(fpw,"Case #%d: %d\n",Case,ans);
    }
    fclose(fpr);
    fclose(fpw);
    return 0;
}
