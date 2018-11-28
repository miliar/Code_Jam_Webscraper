#include <fstream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

void go(int j, vector<int>& a, vector<bool>& b, list<int>& cycles, int k,double & ans)
{
	if (b[j]){ if (k!=1) ans+=k;/*cycles.push_back(k);*/}
	else
	{
		b[j]=true;
		go(a[j],a,b,cycles,k+1,ans);
	}
}

int main()
{
	ifstream fin;
	fin.open("test1.txt");
	ofstream fout;
	fout.open("test2.txt");
	
	int t;
	fin>>t;
	
	for (int i=0; i<t; i++)
	{
		int n;
		double ans(0);
		fin>>n;
		vector<int> a(n+1);
		vector<bool> b(n+1);
		list<int> cycles;

		for (int j=1; j<=n; j++) fin>>a[j];
		for (int j=1; j<=n; j++) if (!b[j]) go(j,a,b,cycles,0,ans);

		fout.precision(10);
		fout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	
	fin.close();
	fout.close();

	return 0;
}
