#include<iostream>
using namespace std;
const int maxn=1010;
int infi=100000000;
int tu,n,m,t,tt,h[maxn],w[maxn],c[maxn],d1[maxn],d2[maxn],hmin,hmax,wmin,wmax,h1min,h1max,w1min,w1max;
void init()
{
     scanf("%d",&n);
     int i;
     char ch;
     for (i=0;i<n;i++)
     {
         scanf("%d%d",&h[i],&w[i]);
         scanf(" %c",&ch);
         if (ch=='B') c[i]=1;
         else c[i]=0;
         for (;;)
         {
             scanf("%c",&ch);
             if (ch=='\n') break;
         }
     }     
}

void work()
{
     memset(d1,0,sizeof(d1));
     memset(d2,0,sizeof(d2));
     hmin=infi;
     hmax=-infi;
     wmin=infi;
     wmax=-infi;
     int i;
     tu=0;
     for (i=0;i<n;i++)
     if (c[i])
     {
              tu++;
              hmin<?=h[i];
              hmax>?=h[i];
              wmin<?=w[i];
              wmax>?=w[i];
     }  
     h1min=infi;
     h1max=-infi;
     w1min=infi;
     w1max=-infi;
     for (i=0;i<n;i++)
     if (!c[i])
     {
        if ((h[i]>=hmin)&&(h[i]<=hmax))
           if (w[i]>wmax) w1min<?=w[i];
           else w1max>?=w[i];
        else
        if ((w[i]>=wmin)&&(w[i]<=wmax))
           if (h[i]>hmax) h1min<?=h[i];
           else h1max>?=h[i];
        else
        {
            if (h[i]<hmin) d1[i]=-1;
            else d1[i]=1;
            if (w[i]<wmin) d2[i]=-1;
            else d2[i]=1;
        }
     }
   //  cout << hmin << " " << hmax << "  " << wmin << " " << wmax << endl;
   //  cout << h1min <<" " << h1max << endl;
}

int check(int x,int y)
{
    if (x<hmin) return 0;
    if (x>hmax) return 0;
    if (y<wmin) return 0;
    if (y>wmax) return 0;
    return 1;
}

int check2(int x,int y)
{
    if (x>=h1min) return 1;
    if (x<=h1max) return 1;
    if (y>=w1min) return 1;
    if (y<=w1max) return 1;
    int i;
    for (i=0;i<n;i++)
    if (d1[i]!=0)
    {
       if (((d1[i]<0)&&(x<=h[i]))||((d1[i]>0)&&(x>=h[i])))
          if (((d2[i]<0)&&(y<=w[i]))||((d2[i]>0)&&(y>=w[i]))) return 1;
    }
    return 0;  
}

void print()
{
     int a,b,i;
     scanf("%d",&m);
     printf("Case #%d:\n",t+1);
     for (;m;m--)
     {
         scanf("%d%d",&a,&b);
         if (!tu) printf("UNKNOWN\n");
         else
         if (check(a,b)) printf("BIRD\n");
         else
         if (check2(a,b)) printf("NOT BIRD\n");
         else printf("UNKNOWN\n");
     }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    for (scanf("%d",&tt),t=0;t<tt;t++)
    {
        init();
        work();
        print();
    }
    return 0;
}
