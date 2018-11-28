//in the name of ALLAH 
#include<iostream>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<fstream>
using namespace std;

int power[12];
bool is(int a,int b)
{
	int c,d,i=1;
	int pp=power[int(log((double)b)/log(10.0))];
	d=b;

	while(d>0)
	{
		c=b/power[i]+(b%power[i])*pp;
		if(c==a)
			return true;
		i++;
		d/=10;
		pp/=10;
	}
	return false;
}


int main()
{
	
	power[0]=1;
	for(int i=1;i<12;i++) power[i]=power[i-1]*10;

	freopen ("C.in","r",stdin);
	freopen ("C.out","w",stdout);
//////////////////////////////


	int t;
	cin>>t;

	int a,b;

	for(int tc=1;tc<=t;tc++)
	{
		int res=0;
		cin>>a>>b;
		for(int i=a;i<=b;i++)
		{
			for(int j=i+1;j<=b;j++)
			{
				if(is(i,j)) res++;
			}
		}

		printf("Case #%d: %d\n",tc,res);
	}

	return 0;
}
//AmzMohammad

