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
	int t;
	cin>>t;
	cout.flags(std::ios::fixed);
	cout<<setprecision(6);
	for(int tt=0; tt<t; tt++)
	{
		int n;
		cin>>n;
		vector<int> a;
		vector<int> b;
		for(int i=0; i<n; i++)
		{
			int p;
			cin>>p;
			a.push_back(p);
			b.push_back(p);
		}
		sort(a.begin(), a.end());
		int k=n;
		for (int i=0; i<n; i++)
			if (a[i]==b[i]) k--;
		cout<<"Case #"<<tt+1<<": "<<double(k)<<endl;
	}
	return 0;
}