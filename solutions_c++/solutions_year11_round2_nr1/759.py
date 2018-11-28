#include<iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<sstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define FOR1(i,n) for(i=1;i<=n;i++)
#define FORab(i,a,b) for(i=a;i<=b;i++)
int main()
{
    int t,n,i,j,cn=1;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	cin>>t;
	while(t--)
	{
	string str[110];
	int num[110]={0};
	double w[110]={0};
	double w1[110]={0};
	double w2[110]={0};
	double w3[110]={0};
	double ans[110]={0};
	cin>>n;
	FOR(i,n)
	{
	    cin>>str[i];
	    w[i]=0;
	    w1[i]=0;
	    w2[i]=0;
	    w3[i]=0;
	    ans[i]=0;
	}

    FOR(i,n)
    {
        FOR(j,n)
        {
            if(str[i][j]=='1')
            {
                num[i]++;
                w3[i]+=1.0;
            }
            else if(str[i][j]=='0') num[i]++;
        }
    }
    FOR(i,n)
    {
        //cout<<"W "<<w[i]<<endl;
        w[i]=w3[i]/num[i];
        //cout<<"W1 "<<w[i]<<endl;

    }
    FOR(i,n)
    {
        FOR(j,n)
        {
            if(str[i][j]=='0')
            {

                w1[i]+=(w3[j]-1)/(num[j]-1);
            }
            else if(str[i][j]=='1')w1[i]+=(w3[j])/(num[j]-1);

        }
    }
    FOR(i,n)
    {
       // cout<<"OW "<<w1[i]<<endl;
        w1[i]=w1[i]/num[i];
        //cout<<"OW "<<w1[i]<<endl;
    }
    FOR(i,n)
    {
        FOR(j,n)
        {
            if(str[i][j]!='.')
            {

                w2[i]+=w1[j];
            }

        }
    }
    FOR(i,n)
    {
         //  cout<<"OOW "<<w2[i]<<endl;
        w2[i]=w2[i]/num[i];
        //cout<<"OOW1 "<<w2[i]<<endl;
    }

    FOR(i,n)ans[i]=(w[i]*0.25)+(w1[i]*0.5)+(w2[i]*0.25);
    cout<<"Case #"<<cn++<<":"<<endl;
    FOR(i,n)printf("%.15lf\n",ans[i]);
	}
	return 0;
}
