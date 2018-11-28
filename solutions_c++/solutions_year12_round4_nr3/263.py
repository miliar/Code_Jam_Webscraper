#include <iostream>
#include <cmath>
#include <algorithm>

#define MAX 7777777

using namespace std;

int T,n,flag;
int x[3000];
int h[3000];
long long mm;
int ttx[3000];


int check(long long a, long long b,long long c)
{
    long long tt;
    tt = h[b]*(c-a)-h[c]*(b-a);
    return tt/(c-b);
}

void cacul(int a,int b,int c)
{
     //int ttx[3000];
     if (b-a < 1) return;
     int i = 0;
     ttx[0] = a;
     while (ttx[i] < b)
     {
         ttx[i+1] = x[ttx[i]];
         i++;
     }
     if (ttx[i] > b)
     {
         flag = 0;
         return;
     }
     h[a-1]--;
     h[ttx[i-1]] = min(check(ttx[i-1],a-1,ttx[i]),check(ttx[i-1],ttx[i],c));
     h[a-1]++;
     //if (mm > h[ttx[i-1]])  mm = h[ttx[i-1]];
     
     int j;
     for (j = i-2; j >= 0;j--)
     {
         h[ttx[j]] = check(ttx[j],ttx[j+1],ttx[j+2]);
         //if (mm > h[ttx[j]])  mm = h[ttx[j]];
     }
     j = a;
     while (j < b)
     //for (j = a;j < b;j = x[j])
     {
         int nn1,nn2;
         nn1 = x[j];
         if (nn1 == b)
             nn2  = c;
         else
             nn2 = x[nn1];
         cacul(j+1,nn1,nn2);
         j = x[j];
     }
         
}


int main()
{
    freopen("small.in","r",stdin);
    freopen("small.txt","w",stdout);
    scanf("%d",&T);
    int i;
    for (i = 1;i <= T;i++)
    {
        flag = 1;
        scanf("%d",&n);
        int j;
        for (j = 1;j < n;j++)
            scanf("%d",x+j);
        x[n] = n+1;
        for (j = 1;j < n;j++)
            h[j] = 0;
        h[0] = MAX-1;
        h[n] = MAX;
        h[n+1] = h[n];
        cacul(1,n,n+1);
        printf("Case #%d:",i);
        if (flag)
        {
            for (j = 1;j <= n;j++)
                printf(" %d",h[j]); 
            printf("\n"); 
        }
        else
            printf(" Impossible\n");
    }   
    return 0;
}
