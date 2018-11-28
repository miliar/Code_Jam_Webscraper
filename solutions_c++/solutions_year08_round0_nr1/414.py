#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

struct seg{
	int s, e;
	seg():s(0),e(0){}
	seg(int s, int e):s(s),e(e){}
	bool operator<(const seg & S)const{
		return s < S.s || (s==S.s && e > S.e);
	}
};

int main(){
	int T, Case=0;
	scanf("%d", &T);
	while (T--){
		int S, Q;
		scanf("%d", &S);
		char SE[S+1][102];
		gets(SE[0]);
		for (int i = 1 ; i <= S; ++i) gets(SE[i]);
		scanf("%d", &Q);
		char QE[Q+1][102];
		gets(QE[0]);
		for (int i = 1; i <= Q; ++i) gets(QE[i]);
		bool canquery[S+1][Q+1];
		memset(canquery, 0, sizeof(canquery));
		for (int i = 1; i <= S; ++i)
			for (int j = 1; j <= Q; ++j)
				if (strcmp(SE[i], QE[j]))
					canquery[i][j] = 1;
		vector<seg> sv;
		for (int i = 1 ; i <= S; ++i)
			for (int j = 1 ; j <= Q; ++j)
				if (canquery[i][j]){
					for (int k  = j; k <= Q; ++k)
						if (!canquery[i][k]){
							sv.push_back(seg(j, k-1));
							break;
						}else if (k == Q) sv.push_back(seg(j, Q));
				}
		sort(sv.begin(), sv.end());
		int ans = 0;
		int st = 0, ed = 0, N = sv.size();
		while (ed < Q){
			int ped = ed, ps=-1;
			for (int i = 0 ; i < N; ++i)
				if (sv[i].s <= ed+1)
					if (sv[i].e > ped)
						ped = sv[i].e, ps = i;
			ans++;
			if (ed >= Q) break;
			st = sv[ps].s;
			ed = sv[ps].e;
		}
		if (ans == 0 ) ans = 1;
		printf("Case #%d: %d\n", ++Case, ans-1);
	}
	return 0;
}
