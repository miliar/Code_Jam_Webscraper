#include <cstdio>
#include <deque>

using namespace std;

int T;

deque<int> orange, blue;
int inps[128];
char inpb[128];
void solve(int tc){

	int n;
	scanf("%d", &n);
	
	orange.clear(); blue.clear();
	
	for (int i=0;i<n;++i){
		char b; int s;
		scanf(" %c %d", &b, &s);
		
		inpb[i] = b; inps[i] = s;
		if (b == 'O') orange.push_back(s);
		else	blue.push_back(s);
	}
	
	int co=1,cb=1;
	int t = 0;
	for (int i=0;i<n;++i){
		int d;
		if (inpb[i] == 'O'){
			d = abs( inps[i] - co )+1;
			co = inps[i];
			if (!orange.empty()) orange.pop_front();
			if (!blue.empty()){
				int nxt = blue.front();
				if (cb < nxt){
					cb += min( nxt - cb, d );
				}else{
					cb -= min( cb-nxt, d );
				}
			}
		}else{
			d = abs( inps[i] - cb )+1;
			cb = inps[i];
			if (!blue.empty()) blue.pop_front();
			if (!orange.empty()){
				int nxt = orange.front();
				if (co < nxt){
					co += min( nxt - co, d );
				}else{
					co -= min( co-nxt, d );
				}
			}
		}
		t += d;
	}
	printf("Case #%d: %d\n", tc, t);
}

int main(){
	scanf("%d", &T);
	
	for (int tc=1;tc<=T;++tc){
		solve(tc);
	}
	
	return 0;
}
