#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int main(int argc, char* argv[])
{
    int test_case,n,s,p,sum,sum1,sur,count,flag=0;
    int *ti=new int [100];
    string in;
    freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	cin>>test_case;
	getline(cin,in);
	for(int i=0;i<test_case;i++)
    {
        cin>>n>>s>>p;
        for(int j=0;j<n;j++)
            cin>>ti[j];
        sum=0;sur=0;count=0;
        for(int a=0;a<n;a++)
        {
           sum=ti[a];
           flag=0;
           for(int k=10;k>=p;k--)
            {
                sum1=sum;
                sum1-=k;
                if((k-1)>=0 || k==0)
                {
                   if((sum1-k)==k || (sum1-k)==(k-1) || (sum1-k+1)==(k-1))
                    {
                        count++;
                        flag=1;
                        break;
                    }
                }
            }

            if(flag==0)
            {
                for(int k=10;k>=p;k--)
                {
                    sum1=sum;
                    sum1-=k;
                    if((k-2)>=0 || k==0)
                    {
                        if((sum1-k)==(k-2) || (sum1-k+1)==(k-2) || (sum1-k+2)==(k-2))
                        {
                            sur++;
                            if(sur<=s)
                            {
                                count++;
                                break;
                            }
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<(i+1)<<": "<<count<<endl;
    }
}
