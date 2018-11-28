#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<cmath>

using namespace std;

vector<int>pr;

int main()
{
	FILE* fin = freopen("in.txt", "r", stdin);
	FILE* fout = fopen("out.txt", "w");
	
	long long k;
	int c,t,n;
	cin >> t;
	for(int i=0;i<t;++i)
	{
		int r, n,k;
		cin >> r >> k >> n;
		vector<int>g(n);
		for(int j=0;j<n;++j) cin >> g[j];
		
		int res = 0;
		for(int j=0;j<r;++j)
		{
			int s = 0, q=0;
			while(s<=k && q<n) {s+=g[q];++q;}
			if(s>k) {s-=g[q-1]; --q;}
			res+=s;
			for(int w=0;w<q;++w) {int t = g[0]; g.erase(g.begin()); g.push_back(t);}
//			cout << s << " ";
		}
		
		cout << "Case #" << i+1 << ": " << res << "\n";
		fprintf(fout, "Case #%d: %d\n", i+1, res);
	}
	fclose(fin);fclose(fout);
}
