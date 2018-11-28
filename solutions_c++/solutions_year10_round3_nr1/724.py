#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<cmath>

using namespace std;

int main()
{
	FILE *fin, *fout;
	freopen_s(&fin, "in.txt", "r", stdin);
	freopen_s(&fout, "out.txt", "w", stdout);
	
	int t;
	cin >> t;
	for(int i=0;i<t;++i)
	{
		int n,m;
		cin >> n;
		vector<int> a(n), b(n);
		for(int j=0;j<n;++j) cin >> a[j] >> b[j];

		int res=0;
		for(int j=0;j<n;++j)
			for(int k=j+1;k<n;++k)
				if(j!=k && (b[j]-b[k])*(a[j]-a[k])<0) ++res;

		cout << "Case #" << i+1 << ": " << res << "\n";
	}

	fclose(fin);
	fclose(fout);

	return 1;
}
