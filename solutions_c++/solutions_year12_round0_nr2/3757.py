#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
using namespace std;
int f[105];
bool vx[105],vy[105];
int n,s,p;
bool check(int a)//no
{
     int x,y;
     x=f[a]/3;
     int flag=f[a]%3;
     //cout<<"x="<<x<<"  flag="<<flag<<endl;
     if(flag==0){if(x>=p)return true;}
     if(flag==1){if((x+1)>=p)return true;}
     if(flag==2){if((x+1)>=p)return true;}
     return false;
}
bool check2(int a)//yes
{
     int x,y;
     x=f[a]/3;
     int ans=f[a]%3;
     if(f[a]==0)return false;
     if(ans==0){if((x+1)>=p)return true;}
     if(ans==1){if((x+1)>=p)return true;}
     if(ans==2){if((x+2)>=p)return true;}
     return false;
}
int main()
{
    int i,j,k;
    int t;
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    scanf("%d",&t);
    int ca=0;
    while(t--)
    {
        scanf("%d%d%d",&n,&s,&p);
        for(i=1;i<=n;i++)scanf("%d",&f[i]);
        memset(vx,false,sizeof(vx));
        memset(vy,false,sizeof(vy));
        int flag1=0;
        int flag2=0;
        for(i=1;i<=n;i++)
        {
            if(check(i)){flag1++;vx[i]=true;}
            if(check2(i)){flag2++;vy[i]=true;}
        }
        int ans=0;
        int flag=0;
        for(i=1;i<=n;i++)
        {
            if(vx[i]==true && vy[i]==true){ans++;flag++;}
        }
        flag2-=flag;
        if(flag2>s)ans+=s;
        else ans+=flag2;
        flag1-=flag;
        ans+=flag1;
        cout<<"Case #"<<++ca<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
