#include<iostream>
#include<vector>
#include<map>
#include<cmath>

typedef long long ll;
#define int  ll

const int MAXN = 1<<23;
int size[MAXN];
int money[MAXN];
int next[MAXN];

int r;
int n,k;
int md(int i)
{
    return ((i+n)%n);
}

main()
{
    int t;
    std::cin>>t;
    for(int z=0;z<t;z++)
    {
        std::cin>>r;
        std::cin>>k;
        std::cin>>n;
        for(int i=0;i<n;i++)
            std::cin>>size[i];
        int fr = k;
        int total = 0;
        for(int i=0;i<=n;i++){
            if(fr<size[i] or i==n){
                money[0] = k-fr;
                next[0]=md(i);
                break;
            }
            fr-=size[i];
        }
        for(int i=1;i<n;i++)
        {
            int m = money[i-1]-size[i-1];
            fr = k-m;
            int j = next[i-1];
            while(fr>=size[md(j)])
            {
                m+=size[md(j)];
                fr = k-m;
                j++;
                j = md(j);
                if(j==i)break;
            }
            money[i]=m;
            next[i]=md(j);
        }
        int j = 0;
        int rounds = 0;
        std::vector<int> used(n,0);
        while(true)
        {
            rounds++;
            //std::cout<<rounds<<":"<<"j = "<<j<<"\n";
            total+=money[j];
            j = next[j];
            if(rounds>=r)break;
            if(j==0)break;
        }
        //std::cout<<'t'<<' '<<total<<std::endl;
        //std::cout<<"r = "<<r<<"\n";
        total = total*(r/rounds);
        //total=0;
        int r2 = r%rounds;
        //r2=r;
        for(int x = 0 ;x<r2;x++)
        {
            total+=money[j];
            j = next[j];
        }
        //for(int j=0;j<n;j++)
            //std::cout<<money[j]<<" "<<next[j]<<"\n";
        //std::cout<<"rounds = "<<rounds<<" r2 = "<<r2<<"\n";
        std::cout<<"Case #"<<(z+1)<<": "<<total<<"\n";
    }
}
