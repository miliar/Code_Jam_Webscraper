#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>
using namespace std;
int main(void)
{
	int t;
	freopen("r2.in","r",stdin);
	freopen("r2.out","w",stdout);
	scanf("%d",&t);
	vector<char> v;
	string a;
	char s[100];
	int q,i,j,tr,kl,si;
	long long res,mn,b[100];
	for (q=0;q<t;q++)
	{
		v.clear();
		scanf("%s",&s);
		a=string(s);
		for (i=0;i<a.size();i++)
		{
			tr=1;
			for (j=0;j<v.size();j++)
				if (a[i]==v[j])
					tr=0;
			if (tr)
				v.push_back(a[i]);
		}
		for (i=0;i<v.size();i++)
		{
			if (i==0)
				kl=1; else
				if (i==1)
					kl=0; else
					kl=i;
			for (j=0;j<a.size();j++)
				if (a[j]==v[i])
					b[j]=kl;
		}
		mn=1;
		res=0;
		if (v.size()==1)
			si=2; else
			si=v.size();
		for (i=a.size()-1;i>=0;i--)
		{
			res+=(mn*b[i]);
			mn*=si;
		}
		printf("Case #%d: %lld\n",q+1,res);
	}
	fclose(stdout);
	return 0;
}


