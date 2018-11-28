#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <algorithm>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <set>

using namespace std;

string k="welcome to code jam";
int main()
{
	//freopen("C-small.in","r",stdin);
	//freopen("C-small.out","w",stdout);
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int n;
	cin >> n;
	getchar();
	for (int tc=1;tc<=n;tc++)
	{
		unsigned long long a[100][502];
		string t;
		getline(cin,t);
		while (t[0]!='w'&&!t.empty())
		{
			t.erase(0,1);
		}
		int ln=k.length();
		int lm=t.length();
		unsigned int ind=0;
		for (int j=0;j<lm;j++)
		{
			if (k[0]==t[j])
			{
				ind++;
				a[0][j]=ind;
			}else
				a[0][j]=ind;
		}
		a[0][0]=1;
		for (int i=1;i<ln;i++)
		{
			a[i][0]=0;
		}
		for (int i=1;i<ln;i++)
		{
			ind=0;
			for (int j=1;j<=lm;j++)
			{
				if (k[i]==t[j])
				{
					ind=(a[i-1][j]+a[i][j-1])%10000;
					a[i][j]=ind;
				}else
					a[i][j]=ind;
			}
		}
		ind%=10000;
		string res="0000";
		int g=3;
		while (ind!=0)
		{
			res[g]=ind%10+'0';
			ind/=10;
			g--;
		}
		cout << "Case #"<<tc<<": "<<res<<endl;
	}

	return 0;
}