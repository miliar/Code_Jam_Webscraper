#include <iostream>
#include <fstream>

using namespace std;

int num[30];
int res[]={0,0,1,2,3,5,8,14,24,43,77,140,256,472,874,1628,3045,5719,10780,20388,38674,73562,140268,268066,513350,984911};
int main ()
{
	freopen ("input", "r", stdin);
	freopen ("output", "w", stdout);

	/*
	for (int sz=2;sz<=25;sz++)
	{
		int res=0;
		for (int i=0;i<(1<<(sz)); i++)
			if (!(i&1))
		{
			int kk=0;
			for (int j=2;j<=sz;j++)
				if ((i>>(j-1)) &1)
				{
					kk++;
					num[j]=kk;
				}
				else
					num[j]=j;
			int now=sz;
			bool ok=1;
			while (now>1 && ok)
			{
				if (now==num[now]) ok=0;
				now=num[now];
			}
			if (ok) res++;
			
		}
		cout<<res<<',';
	}
	*/
	int t,n;
	cin>>t;
	for (int cas=1;cas<=t;cas++)
	{
		cin>>n;
		cout<<"Case #"<<cas<<": "<<res[n]%100003<<endl;
	}
	return 0;
}
