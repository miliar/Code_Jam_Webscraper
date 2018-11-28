#include <stdio.h>
#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

bool f(int a,int b)
{
    return a>b;
}


int get(int n,bool isSur)
{
    int i,j,k;
    for (i=0; i<=10; i++)
	{
	    for (j=i; j<=10; j++)
	    {
	        for (k=j; k<=10; k++)
	        {
	            if (i+j+k==n)
	            {
	                if (isSur && k-i==2)
	                {
	                    //cout<<"GETTING SUR"<<i<<j<<k<<endl;
	                    return k;
	                }
	                else if (!isSur && k-j<=1 && j-i<=1 && k-i<=1)
	                {
	                    //cout<<"GETTING NON SUR"<<i<<j<<k<<endl;
	                    return k;
	                }
	            }
	        }
	    }
	}
	return 0;
}

int main()
{
    int t,cas,n,s,p,data[200],i;
    int sur,nonsur,ans;
    freopen("codejamB.in","r",stdin);
    freopen("codejamB.out","w",stdout);
	cin>>t;
	for (cas=1; cas<=t; cas++)
	{
        cin>>n>>s>>p;
        int cnt=0;
        for (i=0; i<n; i++) cin>>data[i];
        sort(data,data+n,f);
        for (i=0; i<n; i++)
        {
            //cout<<"SIMULATE "<<data[i]<<endl;
            if (data[i]==0) ans=0;
            else if (data[i]==1) ans=1;
            else if (data[i]==29) ans=10;
            else if (data[i]==30) ans=10;
            else
            {
                if (s>0)
                {
                    sur = get(data[i],1);
                    nonsur = get(data[i],0);
                    //cout<<"SUR "<<sur<<" NONSUR "<<nonsur<<endl;
                    ans = max(sur,nonsur);
                    if (sur>nonsur && !(nonsur>=p))s--;
                }
                else
                {
                    ans=get(data[i],0);
                }
            }
            //cout<<"GOT "<<ans<<endl;
            if (ans>=p) cnt++;
        }
        printf("Case #%d: %d\n",cas,cnt);
	}

    return 0;
}
