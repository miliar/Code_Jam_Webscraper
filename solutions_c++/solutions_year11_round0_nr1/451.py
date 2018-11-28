#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int p[2];
int next[2];
char rob[10];
int op[100 + 10][2];
int n;

int main(){
	int T;
	scanf("%d",&T);
	for(int tc = 1;tc<=T;tc++){
		int step = 0;
		p[0] = p[1] = 1;
		scanf("%d",&n);
		next[0] = next[1] = -1;
		for(int i=0;i<n;i++){
			scanf("%s%d",rob,&op[i][1]);
			op[i][0] = rob[0] == 'O';
			if(next[op[i][0]]<0)
				next[op[i][0]] = i;
		}
		for(int i=0;i<n;i++){
			int d = labs(p[op[i][0]] - op[i][1]) + 1;
			step += d;
			p[op[i][0]] = op[i][1];
			next[op[i][0]] = -1;
			for(int j = i + 1;j<n;j++)
				if(op[j][0]==op[i][0]){
					next[op[i][0]] = j;
					break;
				}
			int opp = op[i][0] ^ 1;
			if(next[opp]>=0){
				int td = labs(p[opp] - op[next[opp]][1]);
				if(d>=td)
					p[opp] = op[next[opp]][1];
				else
					p[opp] += d * (p[opp] > op[next[opp]][1] ? -1 : 1);
			}
		}
		printf("Case #%d: %d\n",tc,step);
	}
	return 0;
}
