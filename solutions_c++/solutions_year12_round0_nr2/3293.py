#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
int main()
{
    FILE *fpr,*fpw;
    fpr=fopen("B-large.in","rb");
    fpw=fopen("out.txt","wb");

    int T,Case,i;
    int n,s,p;
    int t[110];
    fscanf(fpr,"%d",&T);
    for(Case=1;Case<=T;Case++)
    {
        fscanf(fpr,"%d%d%d",&n,&s,&p);
        for(i=0;i<n;i++)
            fscanf(fpr,"%d",&t[i]);
        int ans=0;
        for(i=0;i<n;i++)
        {
            int mm;
            if(t[i]%3==0)
            {
                mm=t[i]/3;
                if(mm>=p)
                    ans++;
                else if(p-mm==1&&s>0&&mm>0)
                {
                    ans++;s--;
                }
            }
            else if(t[i]%3==1)
            {
                mm=t[i]/3+1;
                if(mm>=p)
                    ans++;
            }
            else
            {
                mm=t[i]/3+1;
                if(mm>=p)
                    ans++;
                else if(p-mm==1&&s>0)
                {
                    ans++;s--;
                }
            }
        }
        fprintf(fpw,"Case #%d: %d\n",Case,ans);
    }
    fclose(fpr);
    fclose(fpw);
    return 0;
}
