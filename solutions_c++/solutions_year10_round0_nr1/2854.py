#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int t;
    cin>>t;
    unsigned long long k,x=1,y;
    int n;
    while(t-->0)
    {
        cin>>n>>k;
        y=1;
        for(int i=0;i<n;i++)
            y*=2;
        if(k%y == y-1)
        {printf("Case #%lld: ",x);printf("ON\n");
        }
        else
        {printf("Case #%lld: ",x);printf("OFF\n");
        }
        x++;
    }
    return 0;
}

        
