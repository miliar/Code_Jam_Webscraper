#include <fstream>
#include <vector>
#include <string>
using namespace std;
ifstream in;
ofstream out;

int num(vector<vector<int> > & v, int i)
{
	int res = v.size();
	int j = res - 1;
	while(j>=0 && v[i][j]==0) --j;
	return j;
}

void Swap(vector<vector<int> > & v, int i1, int i2)
{
	vector<vector<int> > v1 = v;
	for(int j=0;j<v.size();++j)
	{
		v[i1][j] = v1[i2][j];
		for(int i = i1 + 1; i <= i2;++i)
			v[i][j] = v1[i-1][j];
	}
	return;
}

void solve(int test)
{
	int i,j,k,m,n,p;
	in >> n;
	getline(in, string());
	vector<vector<int> > v(n);
	for(i=0;i<n;++i) v[i].resize(n);
	string str;
	for(i=0;i<n;++i)
	{
		getline(in, str);
		for(j=0;j<n;++j)
			v[i][j] = str[j] - '0';
	}
	int res = 0;
	for(i=0;i<n;++i)
		if(num(v, i) > i)
		{
			for(j = i + 1; j < n; ++j)
				if(num(v, j) <= i)
				{
					res += j - i;
					Swap(v, i, j);
					break;
				}

		}
		out << "Case #" << test << ": " << res << endl;
}

int main()
{
	in.open("a");
	out.open("b");
	int i, n;
	in >> n;
	getline(in, string());
	for(i=0;i<n;++i)
		solve(i+1);
	in.close();
	out.close();
}