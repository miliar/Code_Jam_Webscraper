#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <sstream>
using namespace std;

int N, M;
char dic[10000 + 10][12];
char L[100 + 10][30];

const int mask = 1 << 20;
vector<pair<int,int> >stack[30];
int bestN, res, bestID;

void solve(int id, int dep){
	
	if(stack[dep].size() == 1){
		int idx = stack[dep][0].second;
		//cout << res <<" "<< idx << endl;
		if(res > bestN || res == bestN && idx < bestID){
			bestN = res;
			bestID = idx;
		}
		return;
	}

	char c = L[id][dep-1];
	bool exist = false;
	for(int i = 0; i < stack[dep].size(); i++){
		int idx = stack[dep][i].second;
		int x = 0, len = 0;
		for(int j = 0; dic[idx][j]; j++){
			if(dic[idx][j] == c)
				x = (x<<1) + 1;
			else
				x = x<<1;
			len++;
		}
		if(x > 0)exist = true;
		stack[dep][i].first = x + mask * len;
	} 
	sort(stack[dep].begin(), stack[dep].end() );
	
	int k = stack[dep][0].first;
	stack[dep+1].clear();
	for(int i = 0; i < stack[dep].size(); i++){
		if(stack[dep][i].first != k){
			if(exist && k % mask == 0)res++;
			solve(id, dep + 1);
			if(exist && k % mask == 0)res--;
			stack[dep+1].clear();
			k = stack[dep][i].first;
		}
		stack[dep+1].push_back( stack[dep][i] );
	}
	if(exist && k % mask == 0)res++;
	solve(id, dep + 1);
	if(exist && k % mask == 0)res--;
	stack[dep+1].clear();
}


int main(){
	freopen("B-small-attempt2.in","r",stdin);
	freopen("ans.txt","w",stdout);
	
	int T; scanf("%d", &T);
	for(int cas = 1; cas <= T; cas++){
		scanf("%d %d",&N, &M);
		for(int i = 0; i < N; i++)
			scanf("%s", dic[i]);
		for(int i = 0; i < M; i++)
			scanf("%s", L[i]);

		printf("Case #%d:",cas);
		
		for(int id = 0; id < M; id++){
			stack[0].clear();
			bestN = -1;
			res = 0;
			bestID = 0;
			
			for(int j = 0; j < N; j++)
				stack[0].push_back( make_pair( (int)strlen(dic[j]), j) );

			sort(stack[0].begin(), stack[0].end() );
			
			int k = stack[0][0].first;
			stack[1].clear();
			for(int i = 0; i < stack[0].size(); i++){
				if(stack[0][i].first != k){
					solve(id, 1);
					stack[1].clear();
					k = stack[0][i].first;
				}
				stack[1].push_back( stack[0][i] );
			}
			solve(id, 1);
			printf(" %s",dic[bestID]);
		}

		printf("\n");
	}
}