#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

#define sched pair<int ,int>

#define ARR_A 0
#define ARR_B 1
#define DEP_A 2
#define DEP_B 4

inline int convert(pair<int,int>& hour){
	return hour.first * 60 + hour.second;
}

int main(){	
	int n;
	scanf("%d",&n);
	for(int testCase = 1; testCase <=n; ++testCase){
		int t,na,nb;
		pair<int,int> tmp;
		vector<sched > v;
		scanf("%d %d %d",&t,&na,&nb);
		for(int i = 0; i < na; ++i){
			scanf("%d:%d",&tmp.first,&tmp.second);
			v.push_back(sched(convert(tmp), DEP_A));
			scanf("%d:%d",&tmp.first,&tmp.second);
			v.push_back(sched(convert(tmp)+t, ARR_B));
		}	
		for(int i = 0; i < nb; ++i){
			scanf("%d:%d",&tmp.first, &tmp.second);
			v.push_back(sched(convert(tmp), DEP_B));
			scanf("%d:%d",&tmp.first, &tmp.second);
			v.push_back(sched(convert(tmp)+t, ARR_A));
		}
		sort(v.begin(), v.end());
		//for(int i = 0; i < v.size(); ++i) printf("%.2d:%.2d\t%d\n", v[i].first / 60, v[i].first % 60, v[i].second);

		int retA=0,retB=0,curA=0,curB=0;
		for(int i = 0; i < v.size(); ++i){
			switch(v[i].second){
				case ARR_A: curA++; break;
				case ARR_B: curB++; break;
				case DEP_A: retA = max(retA, -(--curA)); break;
				case DEP_B: retB = max(retB, -(--curB)); break;
			}
		}
		printf("Case #%d: %d %d\n", testCase, retA, retB);
	}
}
