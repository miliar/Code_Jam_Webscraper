#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;


int judge(int a,int s,int p)
{
    if(a==0)
    {
        return 0>=p;
    }
    if(a==30)
    {
        return 10>=p;
    }
    if(a%3==0)
    {
        if(!s)
        {
            //cout<<(a/3)<<" "<<p<<endl;
            return a/3>=p;
        }
        else return a/3+1>=p;
    }
    else if(a%3==1)
    {
        if(!s)
        {
            return a/3+1>=p;
        }
        else return a/3+1>=p;
    }
    else if(a%3==2)
    {
        if(!s)
        {
            return a/3+1>=p;
        }
        else
        {
            if(a/3+2<=10)return a/3+2>=p;
            else return -5;
        }
    }
}

int main()
{
    int t;
    int N,S,P;
    int a[110];
    int ans,tmp,t1,t2,t3;
    cin>>t;
    for(int iii=1;iii<=t;iii++)
    {
        cin>>N>>S>>P;
        for(int i=0;i<N;i++)
          cin>>a[i];
        ans=0;
        if(N==1 && S==1)
        {
            ans=judge(a[0],1,P);
        }
        else if(N==1 && S==0)
        {
            ans=judge(a[0],0,P);
        }
        else if(N==2)
        {
            switch(S)
            {
                case 2:
                       ans=judge(a[0],1,P)+judge(a[1],1,P);break;
                case 1:
                       ans=judge(a[0],0,P)+judge(a[1],1,P);
                       tmp=judge(a[0],1,P)+judge(a[1],0,P);
                       if(ans<tmp)ans=tmp;
                       break;
                case 0:
                       ans=judge(a[0],0,P)+judge(a[1],0,P);
                       break;
            }
        }
        else if(N==3)
        {
            switch(S)
            {
                case 3:
                    ans=judge(a[0],1,P)+judge(a[1],1,P)+judge(a[2],1,P);break;
                case 2:
                    tmp=judge(a[0],1,P)+judge(a[1],1,P)+judge(a[2],0,P);
                    ans=judge(a[0],1,P)+judge(a[1],0,P)+judge(a[2],1,P);
                    if(ans<tmp)ans=tmp;
                    tmp=judge(a[0],0,P)+judge(a[1],1,P)+judge(a[2],1,P);
                    if(ans<tmp)ans=tmp;
                    break;
                case 1:
                    tmp=judge(a[0],1,P)+judge(a[1],0,P)+judge(a[2],0,P);
                    ans=judge(a[0],0,P)+judge(a[1],0,P)+judge(a[2],1,P);
                    if(ans<tmp)ans=tmp;
                    tmp=judge(a[0],0,P)+judge(a[1],1,P)+judge(a[2],0,P);
                    if(ans<tmp)ans=tmp;
                    break;
                case 0:
                    ans=judge(a[0],0,P)+judge(a[1],0,P)+judge(a[2],0,P);break;
            }
        }
        cout<<"Case #"<<iii<<": "<<ans<<endl;
    }
    //system("pause");
    return 0;
}
