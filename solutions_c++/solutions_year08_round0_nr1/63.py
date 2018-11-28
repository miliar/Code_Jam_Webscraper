#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

int N,S,Q,memo[1010][110],inf=1000000000;
vector<int> arr;
char s[1000];

int rec(int idx, int cur){
	if (idx==arr.size()) return 0;
	int &ret = memo[idx][cur];
	if (ret!=-1) return ret;
	
	ret = inf;
	for (int i=0; i<S; i++) if (i!=arr[idx])
		ret = min(ret, rec(idx+1,i) + (cur==i?0:1));
	return ret;
}

int main(){
	sscanf(gets(s),"%d",&N);
	for (int TC=1; TC<=N; TC++){
		sscanf(gets(s),"%d",&S);

		map<string,int> engine; int eidx=0;
		for (int i=0; i<S; i++) engine[gets(s)] = eidx++;

		arr.clear();
		sscanf(gets(s),"%d",&Q);
		for (int i=0; i<Q; i++){
			string q = gets(s);
			if (engine.count(q))
				arr.push_back(engine[q]);
			else
				assert(false);
		}

		memset(memo,-1,sizeof(memo));
		int res = inf;
		for (int i=0; i<S; i++)
			res = min(res, rec(0,i));
		printf("Case #%d: %d\n",TC,res);
	}
}
