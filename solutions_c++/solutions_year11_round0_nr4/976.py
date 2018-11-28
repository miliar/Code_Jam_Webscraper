#include <cstdio>
#include <vector>
#include <algorithm>
#include <memory.h>

bool was[2000];

using namespace std;

int main(){
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int z = 0; z < T; z++){
		vector<int> Start;
		int N;
		scanf("%d",&N);

		for(int i = 0; i < N; i++){
			int p;
			scanf("%d",&p);
			Start.push_back(p-1);
		}

		int res = 0;
		memset(was,0,sizeof(was));
		for(int i = 0; i < Start.size(); i++){
			if(was[i])
				continue;
			int k = 1;
			int cur = Start[i];
			was[i] = true;
			while(cur!=i){
				was[cur] = true;
				cur = Start[cur];
				k++;
			}
			res += k-1;
		}
		res*=2;

		res = 0;
		for(int i = 0; i < Start.size(); i++)
			if(Start[i]!=i)
				res++;
		printf("Case #%d: %0.6lf\n",z+1,(double)res);
	}
	return 0;
}