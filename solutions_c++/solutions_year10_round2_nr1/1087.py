#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

struct TPath { string path; bool exist; };

class TComp { public: bool operator()(TPath a,TPath b){ return (a.path<b.path)||(a.path==b.path && a.exist); } } comp;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("answer.txt","w",stdout);

	int T;
	cin >> T;
	for(int ti=1;ti<=T;ti++)
	{
		int M,N;
		vector<TPath> a;

		cin >> M >> N;

		TPath t;
		t.path="/"; t.exist=true; a.push_back(t);

		for(int i(0);i<M;i++) { cin >> t.path; t.exist=true; a.push_back(t); }
		for(int i(0);i<N;i++) { cin >> t.path; t.exist=false; a.push_back(t); }

		sort(a.begin(),a.end(),comp);

		long num(0);
		for(int i(1);i<a.size();i++) if (!a[i].exist)
		{
			string &s1=a[i].path;
			string &s2=a[i-1].path;

			int k(0);

			while(k<s1.size() && k<s2.size() && s1[k]==s2[k]) k++;

			if(k==s2.size() && k<s1.size() && s1[k]=='/') k++;
			if(k<s1.size())
			{
				num++;
				while(k<s1.size())
				{
					if(s1[k]=='/') num++;
					k++;
				}

			}

			//cout << a[i].path << a[i].exist << num << endl;
		}

		cout << "Case #" << ti << ": " << num << endl;
}

	return 0;
}
