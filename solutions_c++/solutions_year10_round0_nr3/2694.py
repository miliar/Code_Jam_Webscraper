#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;
int main()
{
    freopen("out.txt","w",stdout);
    queue<int>s;
    int t,r,k,n,x,sum,temp;
    int num[11];
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%d%d%d",&r,&k,&n);
        while(s.empty()==false)s.pop();
        while(n--)
        {
            scanf("%d",&x);
            s.push(x);
        }
        sum=0;
        int j;
        while(r--)
        {
            j=1;
            temp=0;
            temp=s.front();
            num[j++]=temp;
            s.pop();
            while(s.empty()==false&&temp+s.front()<=k)
            {
                temp+=s.front();
                num[j++]=s.front();
                s.pop();
            }
            sum+=temp;
            for(int l=1;l<j;l++)
            {
                s.push(num[l]);
            }        
        }
        printf("Case #%d: %d\n",i,sum);        
    }
    return 0;    
}    
