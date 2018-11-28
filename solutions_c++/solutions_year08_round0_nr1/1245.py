//{{{
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <valarray> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <memory> 
#include <new> 
#include <iterator> 
#include <limits> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
#include <cctype> 
using namespace std;
//}}}

const int inf=1000000000;
string getS(){
	char ch;
	string ret;
	while((ch=getchar())=='\n');
	do
		ret+=ch;
	while((ch=getchar())!='\n');
	return ret;
}
vector<string> getVS(){
	int n;
	scanf("%d",&n);
	vector<string> ret;
	for(int i=0;i<n;i++)
		ret.push_back(getS());
	return ret;
}
int opt[100];
int main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		vector<string> S=getVS(),Q=getVS();
		sort(S.begin(),S.end());
		for(int i=0;i<S.size();i++)
			opt[i]=0;
		for(int i=0;i<Q.size();i++){
			int pos=lower_bound(S.begin(),S.end(),Q[i])-S.begin();
			if(pos==S.size()||S[pos]!=Q[i])
				continue;
			set<pair<int,int> > PQ;
			for(int i=0;i<S.size();i++)
				PQ.insert(make_pair(opt[i],i));
			for(int i=0;i<S.size();i++){
				PQ.erase(make_pair(opt[i],i));
				int tmp=PQ.begin()->first;
				PQ.insert(make_pair(opt[i],i));
				opt[i]<?=tmp+1;
				if(i==pos)
					opt[i]=inf;
			}
		}
		int ret=inf;
		for(int i=0;i<S.size();i++)
			ret<?=opt[i];
		printf("Case #%d: %d\n",t,ret);
	}
scanf("%*s");
	return 0;
}
