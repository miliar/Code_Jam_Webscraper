//============================================================================
// Name        : 2010firstB.cpp
// Author      :
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
using namespace std;
#define MAXN 1002
#define INF 2000000000

int R,N,K,sum[2*MAXN][2*MAXN],num[MAXN];
bool flag[2*MAXN][2*MAXN],sim[MAXN],cyc;
vector<int> s,t;
queue<int> q;

int main(){
	freopen("C-small-attempt111.in", "r", stdin);
	FILE* out;
	out = fopen("out.txt", "w");
	int cas,tmp,now,index,output,i,cnt=0;
	scanf("%d", &cas);
	while(cas--){
		scanf("%d%d%d", &R, &K, &N);
		while(!q.empty())
			q.pop();
		for(i = 0; i < N; ++i){
			scanf("%d", &num[i]);
			q.push(num[i]);
		}
		output = 0;
		for(i = 1; i <= R; ++i){
			tmp = 0;
			index = 1;
			while(index <= N){
				now = q.front();
				if(tmp+now > K)
					break;
				tmp += now;
				q.pop();
				q.push(now);
				++index;
			}
			if(index > N){
				output = tmp*R;
				break;
			}
			else
				output += tmp;
		}
		fprintf(out, "Case #%d: %d\n", ++cnt, output);
	}
}

/*int main() {
	freopen("C-small-attempt1.in", "r", stdin);
	FILE* out;
	out = fopen("out.txt", "w");
	int cas,cnt=0,i,tmp,j,a,now;
	long long int output;
	scanf("%d", &cas);
	while(cas--){
		scanf("%d%d%d", &R, &K, &N);
		tmp = 0;
		memset(flag,false,sizeof(flag));
		memset(sim,false,sizeof(sim));
		cyc = false;
		s.clear();
		t.clear();
		for(i = 1; i <= N; ++i){
			scanf("%d", &sum[i][i]);
			if(sum[i][i] > K)
				sim[i] = true;
			tmp += sum[i][i];
			sum[1][i] = tmp;
		}
		if(N == 1){
			if(sum[1][1] > K)
				fprintf(out, "Case #%d: 0\n", ++cnt);
			else
				fprintf(out, "Case #%d: %lld\n", ++cnt, N*R);
			continue;
		}
		for(i = 2; i <= N; ++i){
			tmp = sum[i][i];
			for(j = i+1; j < i+N; ++j){
				if(j > N)
					tmp += sum[j-N][j-N];
				else
					tmp += sum[j][j];
				sum[i][j] = tmp;
				if(sum[i][j] > K){
					for(a = j; a < i+N; ++a)
						sum[i][a] = INF;
					break;
				}
			}
		}
		now = 1;
		output = 0;
		for(i = 1; i <= R; ++i){
			tmp = now;
			if(sim[now])
				break;
			for(j = now+1; j < now+N; ++j){
				if(sum[now][j] > K){
					if(flag[now][j-1]){
						cyc = true;
						--i;
						break;
					}
					flag[now][j-1] = true;
					output += sum[now][j-1];
					s.push_back(now);
					t.push_back(j-1);
					if(j > N)
						now = j-N;
					else
						now = j;
					break;
				}
			}
			if(j == tmp+N){
				flag[tmp][j-1] = true;
				output += sum[tmp][j-1];
				s.push_back(tmp);
				t.push_back(j-N-1);
				output += ((long long int)sum[tmp][j-1] * (long long int)(R-i));
				break;
			}
			if(cyc)
				break;
		}
		if(cyc){
			output *= (R/i);
			a = 0;
			for(j = 1, a = 0; j <= R%i && a < (int)s.size(); ++j, ++a){
				output += sum[s[a]][t[a]];
			}
		}
		fprintf(out, "Case #%d: %lld\n", ++cnt, output);
	}
	return 0;
}*/
