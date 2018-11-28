#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int h=1;
    while(n--)
    {
        int a,b;
        cin>>a>>b;
        int ans=0;
        if(a%10==a)
        ;
        else if(a%100==a)
        {
            for(int i=a;i<=b;i++)
            {
                int v=i%10;
                int u=i/10;
                v=((v*10)+u);
                if(v<=b && v>a && v>i)
                ans++;
            }
        }
        else if(a%1000==a)
        {
            for(int i=a;i<=b;i++)
            {
                int v=i%10;
                int u=i/10;
                v=((v*100)+u);
                if(v<=b && v>a && v>i)
                ans++;
                int x=i%100;
                int y=i/100;
                x=((x*10)+y);
                if(x<=b && x>a && x>i)
                ans++;
            }
        }
        else if(a%10000==a)
        {
            for(int i=a;i<=b;i++)
            {
                int v=i%10;
                int u=i/10;
                v=((v*1000)+u);
                if(v<=b && v>a && v>i)
                ans++;
                int x=i%100;
                int y=i/100;
                x=((x*100)+y);
                if(x<=b && x>a && x>i)
                ans++;
                int l=i%1000;
                int m=i/1000;
                l=((l*10)+m);
                if(l<=b && l>a && l>i)
                ans++;
            }
        }
        cout<<"Case #"<<h++<<": "<<ans<<endl;
    }
}
