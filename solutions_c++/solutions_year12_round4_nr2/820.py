#include<iostream>
#include<vector>
#include<map>
#include<fstream>
#include<iomanip>
#include<algorithm>
#include<queue>
#include<set>

using namespace std;

int posi[] = {1,0,-1,0};
int posj[] = {0,1,0,-1};

typedef pair<int,int> pii;
typedef pair<pii,int> pipii;
typedef vector<pii > vpii;
typedef pair<double,double> pdd;
typedef pair<double,pii > pdpii;
typedef vector<bool> vb;
typedef vector<vb > vvb;

long double EPS = 0.000000001;

int main()
{
	ifstream fin ("in.in");
	ofstream fout ("out.out");
	int caso = 1;
	int T;
	fin >> T;
	for (; T > 0; T--)
	{
		fout << "Case #" << caso << ":";
		caso++;
		long long n, w, l;
		fin >> n >> w >> l;
		int maxim = -1;
		vector<int> v (n);
		for (int i = 0; i < n; i++)
		{
			fin >> v[i];
			maxim = max(maxim,v[i]);
		}
		int ct = 0;
		vpii res (n);
		int lasti;
		for (int i = 0; i <= min(w,l) && ct < n; i+=(2*maxim))
		{
			lasti = i;
			for (int j = 0; j <= i && ct < n; j+=(2*maxim))
			{
				res[ct] = pii(i,j);
				ct++;
				res[ct] = pii(j,i);
				ct++;
				if (i == j) ct--;
			}
		}
		if (ct < n)
		{
			for (int i = lasti+2*maxim; i <= max(w,l) && ct < n; i+=(2*maxim))
			{
				for (int j = 0; j <= min(w,l) && ct < n; j+=(2*maxim))
				{
					if (w > l) res[ct] = pii(i,j);
					else res[ct] = pii(j,i);
					ct++;
				}
			}
		}
		for (int i = 0; i < n; i++)
		{
			fout << " " << res[i].first << " " << res[i].second;
		}
		fout << endl;
	}
	
}
