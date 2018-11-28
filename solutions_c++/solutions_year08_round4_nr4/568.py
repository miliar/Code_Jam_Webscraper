#include<iostream>
using namespace std;
char st[50005],st1[50005];
bool mark[20];
int aa[20];
int mm; 
void work(int k,int ii)
{
     if (ii<k)
     {
               for (int i=0;i<k;i++)
                 if (mark[i]==false)
                 {
                                    mark[i]=true;
                                    aa[ii]=i; 
                                    work(k,ii+1);
                                    mark[i]=false; 
                 }
     }
     else
     {
         int ll=strlen(st);
         for (int i=0;i<ll/k;i++)
         {
             for (int j=0;j<k;j++)
             {
                 st1[i*k+j]=st[i*k+aa[j]];
             }
         }
         int bb=1; 
         for (int i=1;i<ll;i++)
         {
             if (st1[i]!=st1[i-1])bb++;
         }
         if (bb<mm)mm=bb;
     }
}
                                     
int main()
{
    int casen,k;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout); 
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d",&k);
        scanf("%s",st);
        memset(mark,0,sizeof(mark));
        mm=100000; 
        work(k,0);
        printf("Case #%d: %d\n",casei,mm);
    }
    return 0;
} 
 
