#include<fstream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<iomanip>

using namespace std;

int p[300];
int v[300];
int d;

long long f(int l, int r)
{
	int V = 0;
	for (int i=l; i<=r; i++)
	{
		V+=v[i];
	}
	return max(0, (V-1)*d - (p[r]-p[l]));
}

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int t;
	cin>>t;
	cout.flags(std::ios::fixed);
	cout<<setprecision(8);
	for(int tt=0; tt<t; tt++)
	{
		int n;
		cin>>n;
		cin>>d;
		for(int i=0; i<n; i++)
		{
			cin>>p[i]>>v[i];
		}
		long long ma = 0;
		for(int i=0; i<n; i++)
		{
			for(int j=0; j<n-i; j++)
			{
				long long r = f(j, j+i);
				if (r>ma) ma=r;
			}
		}


		cout<<"Case #"<<tt+1<<": "<<ma/2.<<endl;

		
	}
	return 0;
}