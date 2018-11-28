#include<fstream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<iomanip>

using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	cout.flags(std::ios::fixed);
	cout<<setprecision(6);

	int t;
	cin>>t;
	for(int tt=0; tt<t; tt++)
	{
		int n;
		cin>>n;
		int a[11000];
		int l[11000];
		int d[11000];
		int D;
		for(int i = 0; i<n; i++)
		{
			cin>>d[i]>>l[i];
			a[i] = -1;
		}
		cin>>D;
		d[n] = D;
		a[n] = -1;
		l[n] = 0;
		a[0] = d[0];
		for(int i = 0;i<n; i++)
		{
			int m = d[i]+a[i];
			int j = i+1;
			while(d[j]<=m && j<=n)
			{
				int t = min(l[j], d[j]-d[i]);
				if(t>a[j]) a[j] = t;
				j++;
			}
		}
		string res;
		if(a[n]==0) res = "YES"; else res = "NO";

		cout<<"Case #"<<tt+1<<": "<<res<<endl;
	}
	return 0;
}
