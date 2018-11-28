#include <iostream>
#include <vector>

using namespace std;

vector <int> repr;

int rep (int a)
{
	if (repr[a]==a)
		return a;
	int b=rep(repr[a]);
	repr[a]=b;
	return b;
}

void une (int a, int b)
{
	repr[rep(a)]=rep(b);
}

int main()
{
	int C;
	cin >> C;
	//Criba
	vector <bool> prim (1001,true);
	vector <int> lp;
	for (int i=2;i<1001;i++)
	{
		if (not prim[i])
			continue;
		lp.push_back(i);
		for (int j=2;j*i<1001;j++)
		{
			prim[i*j]=false;
		}
	}
	for (int caso=1;caso<=C;caso++)
	{
		int A,B,P;
		cin >> A >> B >> P;
		int n=B-A+1;
		repr=vector <int> (n);
		for (int i=0;i<n;i++)
			repr[i]=i;
		int pm=0;
		while (lp[pm]<P)
			pm++;
		int sum=n;
		for (int i=0;i<n;i++)
		{
			for (int j=i+1;j<n;j++)
			{
				if (rep(i)==rep(j))
					continue;
				for (int k=pm;k<lp.size();k++)
				{
					if ((i+A)%lp[k]==0 and (j+A)%lp[k]==0)
					{
						une(i,j);
						sum--;
						break;
					}
				}
			}
		}
		cout << "Case #" << caso << ": " << sum << endl;
	}
}
