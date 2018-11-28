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
		long long l,p;
		int c;
		cin >> l >> p>> c;
		vector<long long> v;

		long long l1;
		l1 = l*c;
		while(l1<p)
		{
			v.push_back(l1);
			l1*=c;
		}

//		long long p1 = p/c;
//		while(p1>l)
//		{
//			v.push_back(p1);
//			p1/=c;
//		}

//		sort(v.begin(),v.end());
		if(v.size()==0)
			cout << "Case #" << i+1 << ": " << "0\n";
		else
		{
			int res = 1, nres=0;
			while(res<v.size()+1){res*=2;++nres;}
			if(res==1)
				cout << "Case #" << i+1 << ": " << "1\n";
			else
				cout << "Case #" << i+1 << ": " << nres << "\n";
		}
	}

	fclose(fin);
	fclose(fout);

	return 1;
}
