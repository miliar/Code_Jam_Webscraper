#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#define MP make_pair

using namespace std;
typedef pair<int,int> Pair;
typedef vector<int> Vector;
typedef long long LL;
 
string a[210], b[22];
int n, m, score[210];
bool ok[210], lea[230];
int ret;

bool in(char k,int i){
	for(int j = 0;j < a[i].length(); ++j)
		if(a[i][j] == k) return true;
	return false;
}
bool com(int i,int j,char k){
	
		for(int jj = 0;jj < a[j].length(); ++jj){
			if((a[i][jj] == k) ^ (a[j][jj] == k))return false;
		}
	
	return true;
}

void guess(int i,char k){
	if(in(k,i)){
		vector<int> ve; ve.clear();
		for(int j = 0;j < a[i].length(); ++j)
			if(a[i][j] == k) ve.push_back(j);
		for(int j = 1;j <= n;++j){
			if(!ok[j]) continue;
			if(!in(k,j)) ok[j] = false;
			else{
				if(!com(i,j,k)) { ok[j] = false;} 
				
			}
		}
	}else{
		//cout << "guess " << k << " of word " << a[i] << endl;
		ret ++;
		for(int j = 1; j <= n; ++j){
			if(!ok[j]) continue;
			if(in(k,j)) ok[j] = false;
		}
	}
}
void choose(int i,int p){   // choose word i of list p
	int L = a[i].length();
	int l = b[p].length();
	for(int j = 1;j <= n; ++j)
		if(a[j].length() != L) ok[j] = false; // 
	
	for(int j = 0;j < l; ++j){
		for(int k = 1;k <= n; ++k){
			if(!ok[k]) continue;
			if(in(b[p][j],k)){
				guess(i,b[p][j]);
				break;
			}
		}
	}
}
void solve(int p){  // list-p
	for(int i = 1;i <= n; ++i){
		memset(ok,true,sizeof(ok));
		//memset(lea,true,sizeof(lea));
		ret = 0;
		choose(i,p);
		score[i] = ret;
		//cout << " when choose " << a[i] << "  score =  " << score[i] << endl;
		
	}
}
int main()
{
	freopen("B-small-attempt5.in","r",stdin);
	freopen("B-small-attempt5.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int it = 1;it <= T; ++it){
		scanf("%d%d",&n,&m);
		for(int i = 1;i <= n; ++i) cin >> a[i];
		for(int i = 1;i <= m; ++i) cin >> b[i];
		printf("Case #%d: ",it);
		for(int i = 1;i <= m; ++i){
			memset(score,0,sizeof(score));
			solve(i);
			int M = *max_element(score+1,score+1+n);
			for(int j = 1;j <= n; ++j){
				if(score[j] == M){
					cout << a[j];
					break;
				}
			}
			if(i != m) putchar(' ');
			else puts("");
		}
	}
	
}
