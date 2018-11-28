#include <iostream>
#include <deque>

using namespace std;

int main()
{
    int t;
    freopen("cin.txt","r",stdin);
    freopen("cout.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int r,n,temp;
        long long k;
        long long mm=0;
        scanf("%d%I64d%d",&r,&k,&n);
        deque<int>a;
        for(int j=1;j<=n;j++){scanf("%d",&temp);a.push_back(temp);}
        while(r--)
        {
            long long num=0;int p=1;
            while(num<k&&p<=n)
            {
                temp=a.front();
                if(num+temp<=k)
                {
                    num+=temp;p++;
                    a.pop_front();a.push_back(temp);
                }
                else break;
            }
            mm+=num;
        }
        printf("Case #%d: %I64d\n",i,mm);
    }
}
