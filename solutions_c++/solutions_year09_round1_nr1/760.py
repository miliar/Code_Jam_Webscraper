#include<cstring>
#include<cstdio>
#include<map>
using namespace std;
int dig[12],aa[100];

bool isHappy(int num,int r)
{
    map<int,int>mp;
    mp[num]=1;
    while(1)
    {
        int j=0,sum=0;
        while(num){
            aa[j++]=num%r;
            num/=r;
        }
        for(int i=0;i<j;i++)
            sum+=aa[i]*aa[i];
        if(sum==1)return true;
        if(mp.find(sum)!=mp.end())return false;
        mp[sum]=1;  num=sum;
    }
}
int main()
{
    int t;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t);
    for(int ii=1;ii<=t;ii++)
    {
        char ch;
        int k=0,d;
        do{
            scanf("%d%c",&d,&ch);
            dig[k++]=d;
        }while(ch!='\n');

        int ans=1,flag;
        while(1){
            ans++;
            flag=1;
            for(int i=0;i<k;i++)
                if(!isHappy(ans,dig[i])){flag=0;break;}
            if(flag)break;
        }
        printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}
