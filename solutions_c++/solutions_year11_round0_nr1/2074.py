#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<stdlib.h>
using namespace std;
int O[5*100],B[5*100];
char M[5*100],ch;


int mn(int a,int b)
{
    return a>b?b:a;
}

int mx(int a,int b)
{
    return a>b?a:b;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A1.out","w",stdout);
    int t,n,i,j,cas=1,k,cst,red,oind,bind,ii,jj;
    scanf("%d",&t);
    while(t--)
    {
         scanf("%d",&n);j=0;
         int p=0,q=0;
        for(i=0;i<n;i++)
        {
            scanf(" %c %d",&ch,&k);
            if(ch=='O')
                    O[p++]=k;
            else
                    B[q++]=k;
            M[i]=ch;
        }
         oind=bind=1;cst=0;
         ii=0;jj=0;
         for(i=0;i<n;i++)
         {
            if(M[i]=='O')
            {
                red=abs(O[ii]-oind)+1;cst+=red;oind=O[ii++];
                bind=(B[jj]>bind)? mn(bind+red,B[jj]): mx(bind-red,B[jj]);
            }
            else
            {
                red=abs(B[jj]-bind)+1; cst+=red;bind=B[jj++];
                oind=(O[ii]>oind)? mn(oind+red,O[ii]) : mx(oind-red,O[ii]);
            }
         }
        printf("Case #%d: %d\n",cas++,cst);
    }

    return 0;
}
