#include<vector>
#include<iostream>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<string>
#include<map>
#include<fstream>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define all(a) (a).begin(),(a).end()
bool cmp(pair<int,int> a,pair<int,int> b)
{
	if(a.first==b.first) return a.second<b.second;
	return a.first<b.first;
}
int main()
{
	ifstream fin("C:\\A-largeeee.in");
	ofstream fout("C:\\A-largeeee.out");
	int t;
	fin>>t;
	int rr=1;
	while(rr<=t)
	{
		int n;
		fin>>n;
		cout<<n<<endl;
		vector< pair<int,int> > v(n);
		FOR(i,0,n)
		{
			int a,b;
			fin>>a>>b;
			v[i]=make_pair(a,b);
		}
		sort(all(v),cmp);
		//FOR(i,0,v.size()) cout<<v[i].first<<" "<<v[i].second<<endl;
		int intersect=0;
		FOR(i,0,n)
		{
			FOR(j,i+1,n)
			{
				if(v[i].second>v[j].second)
					intersect++;
			}
		}
		fout<<"Case #"<<rr<<": "<<intersect<<endl;
		rr++;
	}
}