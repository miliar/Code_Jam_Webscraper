#include<iostream>
#include<vector>
using namespace std;

vector<int> opr, opra, oprb;
int abss(int x){
	return x > 0 ? x : -x;
}

int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int p1, p2, tk1, tk2, time, dtime;
	int cas;
	scanf("%d", &cas);
	for(int t = 0; t < cas; t++){
		int n, tp; char buf[10]; scanf("%d", &n);
		opra.clear(); oprb.clear(); opr.clear();
		for(int i = 0; i < n; i++){
			scanf("%s%d", buf, &tp);
			if(buf[0] == 'O') {opr.push_back(1); opra.push_back(tp);}
			else if(buf[0] == 'B') {opr.push_back(2); oprb.push_back(tp);}
		}
		time = 0; p1 = p2 = 1; tk1 = tk2 = 0;
		for(int i = 0; i < n; i++){
			if(opr[i] == 1){
				dtime = abss(p1 - opra[tk1]) + 1;
				time += dtime;
				p1 = opra[tk1++];
				if(i == n - 1) break;
				if(oprb.size() > tk2){
					if(abss(p2 - oprb[tk2]) < dtime){
						p2 = oprb[tk2];
					}
					else{
						if(p2 > oprb[tk2]) p2 = p2 - dtime;
						else p2 = p2 + dtime;
					}
				}
			}
			else{
				dtime = abss(p2 - oprb[tk2]) + 1;
				time += dtime;
				p2 = oprb[tk2++];
				if(i == n - 1) break;
				if(opra.size() > tk1){
					if(abss(p1 - opra[tk1]) < dtime){
						p1 = opra[tk1];
					}
					else{
						if(p1 > opra[tk1]) p1 = p1 - dtime;
						else p1 = p1 + dtime;
					}
				}
			}
		}
		printf("Case #%d: %d\n", t + 1, time);
	}
	return 0;
}