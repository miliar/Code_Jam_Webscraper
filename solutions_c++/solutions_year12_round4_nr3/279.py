#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<list>
#include<sstream>
#include <functional>
#include <utility>
using namespace std;

int w[2200];
long long h[2200];
int n;



int main()
{
    freopen("C.in","rt",stdin);
    freopen("C.out","wt",stdout);
    int tst,cas;
    scanf("%d",&tst);
    for(cas=1;cas<=tst;cas++)
    {
        scanf("%d",&n);
        for(int i=1;i<=n-1;i++) scanf("%d",&w[i]);

        bool pl=false;
        for(int i=1;i<=n;i++) h[i]=i;
        bool plx;
        long long mx1,mx2,ind;



        do
        {
            plx=true;
            for(int i=1;i<=n-1;i++)
            {
                mx1=h[i+1]-h[i];mx2=1;ind=i+1;
                for(int j=i+2;j<=n;j++) {
                    if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
                }
                if(ind!=w[i]) {
                    plx=false;
                    break;
                }
            }
            if(plx) {
                pl=true;
                break;
            }

        }while(next_permutation(h+1,h+1+n));

        for(int m=1;m<=n;m++){
            if(pl) break;
        w[n]=m;
        for(int i=1;i<=n;i++) h[i]=w[i];
        sort(h+1,h+1+n);
        do
        {
            plx=true;
            for(int i=1;i<=n-1;i++)
            {
                mx1=h[i+1]-h[i];mx2=1;ind=i+1;
                for(int j=i+2;j<=n;j++) {
                    if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
                }
                if(ind!=w[i]) {
                    plx=false;
                    break;
                }
            }
            if(plx) {
                pl=true;
                break;
            }

        }while(next_permutation(h+1,h+1+n));
        if(pl) break;
        }


        int cn5=0;
        while(!pl)
        {
            cn5++;
            if(cn5==1000000) break;
            for(int i=1;i<=n;i++) h[i]=(rand()%n+2*rand()+1)%n+1;
            random_shuffle(h+1,h+1+n);

            plx=true;
            for(int i=1;i<=n-1;i++)
            {
                mx1=h[i+1]-h[i];mx2=1;ind=i+1;
                for(int j=i+2;j<=n;j++) {
                    if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
                }
                if(ind!=w[i]) {
                    plx=false;
                    break;
                }
            }
            if(plx) {
                pl=true;
                break;
            }

        }

        if(!pl)
        {
            h[n]=1;
            plx=true;

            h[n-1]=1;


            for(int i=n-2;i>=1;i--)
            {
                h[i]=1;

                mx1=h[i+1]-h[i];mx2=1;ind=i+1;
                for(int j=i+2;j<=n;j++) {
                    if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
                }
                if(ind!=w[i])
                {
                    h[w[i]]=(mx1*(w[i]-i)+h[i]*mx2)/mx2;
                    while(h[w[i]]*mx2<=(mx1*(w[i]-i)+h[i]*mx2)) h[w[i]]++;
                }
            }

            for(int i=1;i<=n-1;i++)
            {
                mx1=h[i+1]-h[i];mx2=1;ind=i+1;
                for(int j=i+2;j<=n;j++) {
                    if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
                }
                if(ind!=w[i]) plx=false;
            }

            for(int i=1;i<=n;i++)
            {
                if(h[i]>1000000000LL||h[i]<0) plx=false;
            }
            if(plx) pl=true;

            int cn7=0;
            while(!pl&&cn7<100000)
            {
                cn7++;
                plx=true;
                for(int i=n-2;i>=1;i--)
                {


                    mx1=h[i+1]-h[i];mx2=1;ind=i+1;
                    for(int j=i+2;j<=n;j++) {
                        if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
                    }
                    if(ind!=w[i])
                    {
                        h[w[i]]=(mx1*(w[i]-i)+h[i]*mx2)/mx2;
                        while(h[w[i]]*mx2<=(mx1*(w[i]-i)+h[i]*mx2)) h[w[i]]++;
                    }
                }

                for(int i=1;i<=n-1;i++)
                {
                    mx1=h[i+1]-h[i];mx2=1;ind=i+1;
                    for(int j=i+2;j<=n;j++) {
                        if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
                    }
                    if(ind!=w[i]) plx=false;
                }

                for(int i=1;i<=n;i++)
                {
                    if(h[i]>1000000000LL||h[i]<0) plx=false;
                }
                if(plx) pl=true;


            }
        }


        /*h[n]=1;
        bool pl=true;
        if(w[n-1]!=n) pl=false;
        h[n-1]=1;

        long long mx1,mx2,ind;
        for(int i=n-2;i>=1;i--)
        {
            h[i]=1;

            mx1=h[i+1]-h[i];mx2=1;ind=i+1;
            for(int j=i+2;j<=n;j++) {
                if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
            }
            if(ind!=w[i])
            {
                h[w[i]]=(mx1*(w[i]-i)+h[i]*mx2)/mx2;
                while(h[w[i]]*mx2<=(mx1*(w[i]-i)+h[i]*mx2)) h[w[i]]++;
            }
        }

        for(int i=1;i<=n-1;i++)
        {
            mx1=h[i+1]-h[i];mx2=1;ind=i+1;
            for(int j=i+2;j<=n;j++) {
                if((h[j]-h[i])*mx2>(j-i)*mx1) mx1=h[j]-h[i],mx2=j-i,ind=j;
            }
            if(ind!=w[i]) pl=false;
        }

        for(int i=1;i<=n;i++)
        {
            if(h[i]>1000000000LL||h[i]<0) pl=false;
        }*/




        printf("Case #%d:",cas);
        if(pl)
        {
            for(int i=1;i<=n;i++) printf(" %lld",h[i]);
            printf("\n");
        }
        else printf(" Impossible\n");


    }
    return 0;
}
