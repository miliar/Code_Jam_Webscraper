#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<fstream>

using namespace std;

int main()
{
    int T,n,s,p,num[105],mod,c=1;

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    cin>>T;

    while(T--)
    {
        cin>>n>>s>>p;

        for(int i=0;i<n;i++)
        {
            cin>>num[i];
        }

            int number,cnt=0;

        for(int i=0;i<n;i++)
        {
            mod = num[i]%3;

            if(mod==0) number = num[i]/3;
            else number =  num[i]/3+1;


            if(number>=p) {
                cnt++;}
            else if(s && mod!=1 && number!=0)  //problem
            {

                if(number+1==p)
                {
                    cnt++;
                    s--;
                }
            }

        }

        cout<<"Case #"<<c++<<": "<<cnt<<endl;
    }

return (0);
}
