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
		int n, k;
		cin >> n >> k;
//		string tmp('.',n+1);
//		tmp[n+1] = '\n';
		vector<string> m;
		for(int j=0;j<n;++j)
		{
			char *t1 = new char[n];
			fscanf(fin, "%s", t1);
			string t2(t1);
			m.push_back(t2);
//			delete[] t1;
		}
		
		for(int j=0;j<n;++j)
		{
			for(int k=0;k<n-1;++k)
				if(m[j][k]!='.' && m[j][k+1]=='.') { m[j].erase(m[j].begin()+k+1);m[j].insert(m[j].begin(),'.'); }
		}

		int red = 0, blue = 0;

		string fnd("R");
		for(int j=0;j<m.size();++j)
			while(m[j].find(fnd) != m[j].npos) fnd.push_back('R');
		if(fnd.size()-1>=k) red = 1;

		string fnb("B");
		for(int j=0;j<m.size();++j)
			while(m[j].find(fnb) != m[j].npos) fnb.push_back('B');
		if(fnb.size()-1>=k) blue = 1;

		if(red && blue) { cout << "Case #" << i+1 << ": " << "Both\n"; continue; }
//
		vector<string> m1(m);
		for(int j=0;j<m1.size();++j)
			for(int k=0;k<m1[0].size();++k) m1[j][k] = m[k][j];

		string fnd1("R");
		for(int j=0;j<m1.size();++j)
			while(m1[j].find(fnd1) != m1[j].npos) fnd1.push_back('R');
		if(fnd1.size()-1>=k) red = 1;

		string fnb1("B");
		for(int j=0;j<m1.size();++j)
			while(m1[j].find(fnb1) != m1[j].npos) fnb1.push_back('B');
		if(fnb1.size()-1>=k) blue = 1;

		if(red && blue) { cout << "Case #" << i+1 << ": " << "Both\n"; continue; }
//
		vector<string> m2(2*m.size());
		for(int j=0;j<m2.size();++j)
		{
			int q, c;
			q = max<int>(0,j-m.size());
			c = min<int>(j,m.size()-1);
			while(q<m1.size() && c>=0) { m2[j].push_back(m[c][q]); ++q; --c; }
		}

		string fnd2("R");
		for(int j=0;j<m2.size();++j)
			while(m2[j].find(fnd2) < m2.size()) fnd2.push_back('R');
		if(fnd2.size()-1>=k) red = 1;

		string fnb2("B");
		for(int j=0;j<m2.size();++j)
			while(m2[j].find(fnb2) < m2.size()) fnb2.push_back('B');
		if(fnb2.size()-1>=k) blue = 1;

		if(red && blue) { cout << "Case #" << i+1 << ": " << "Both\n"; continue; }
//
		vector<string> m3(2*m.size());
		for(int j=0;j<m3.size();++j)
		{
			int q, c;
			c = max<int>(0,j-m.size());
			q = max<int>(0,m.size()-1-j);
			while(c<m.size() && q<m.size()) { m3[j].push_back(m[c][q]); ++q; ++c; }
		}

		string fnd3("R");
		for(int j=0;j<m3.size();++j)
			while(m3[j].find(fnd3) != m2[j].npos) fnd3.push_back('R');
		if(fnd3.size()-1>=k) red = 1;

		string fnb3("B");
		for(int j=0;j<m3.size();++j)
			while(m3[j].find(fnb3) != m3[j].npos) fnb3.push_back('B');
		if(fnb3.size()-1>=k) blue = 1;

		if(red && blue) { cout << "Case #" << i+1 << ": " << "Both\n"; continue; }

		if(!red && blue) { cout << "Case #" << i+1 << ": " << "Blue\n"; continue; }
		if(red && !blue) { cout << "Case #" << i+1 << ": " << "Red\n"; continue; }
		if(!red && !blue) { cout << "Case #" << i+1 << ": " << "Neither\n"; continue; }


//		cout << "Case #" << i+1 << ": " << ;
	}

	fclose(fin);
	fclose(fout);

	return 1;
}
