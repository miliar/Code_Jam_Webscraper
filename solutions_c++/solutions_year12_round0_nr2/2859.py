#include<iostream>
#include<cstdio>
using namespace std;



int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,ii=0;
    cin>>t;
    while(t--)
    {
        int n,s,p;
        cin>>n>>s>>p;
        int cnt=0;
        while(n--)
        {
            int score;
            cin>>score;
            int num1=score/3;
            int num2=num1,num3=num1;
            int yu=score%3;
            if(yu==1) ++num1;
            else if(yu==2){++num1;++num2;}
            if(num1>=p) cnt++;
            else if(s)
            {

                if( (yu==2||yu==0)&&num1<10&&num2>0 )
                {
                    if(num1+1>=p)
                    {
                        s--;
                        cnt++;
                    }
                }
            }
        }
        cout<<"Case #"<<++ii<<": "<<cnt<<endl;
    }

    return 0;
}
