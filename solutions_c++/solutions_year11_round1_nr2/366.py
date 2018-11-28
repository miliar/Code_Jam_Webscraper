#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> ws;
int N, M;

bool toCheck(string a, string open, char ch){
	if(a.length() != open.length()) return false;
	for(int i=0; i<(int)open.length(); i++){
		if(open[i]!='*' && a[i]!=open[i]) return false;
	}
	bool ret = false;
	for(int i=0; i<(int)a.length(); i++){
		ret |= (a[i]==ch);
	}
	return ret;
}

int subsolve(int kk, string L){
	int ret = 0;
	int len = ws[kk].length();
	string open = string(len, '*');
	string answer = ws[kk];
	vector<bool> fs(N,true);
	for(int i=0; i<N; i++){
		if(ws[i].length() != open.length()) fs[i] = false;
	}
	for(int i=0; i<26; i++){
		if(open==answer) break;
		char c = L[i];
		bool f = false;
		for(int j=0; j<N; j++)if(fs[j]){
			f |= toCheck(ws[j], open, c);
		}
		if(f){
			bool found =  false;
			for(int j=0; j<N; j++)if(fs[j]){
				for(int k=0; k<len; k++){
					if(answer[k]!=c && ws[j][k]==c) fs[j]=false;
					if(answer[k]==c && ws[j][k]!=c) fs[j] = false;
				}
			}
			for(int k=0; k<len; k++)if(answer[k]==c && open[k]=='*'){
				found = true;
				open[k] = c;
			}
			if(!found) ret++;
		}
	}
	return ret;
}

string solve(string L){
	int best = -1;
	string ans = "zzzzzzzzzzzzzzzzz";
	for(int i=0; i<N; i++){
		int a = subsolve(i, L);
		if(a > best){
			ans = ws[i];
			best = a;
		}
	}
	return ans;
}

int main(){
	int T;
	scanf("%d",&T);
	for(int c=1; c<=T; c++){
		scanf("%d%d ",&N,&M);
		vector<string> ans;
		ws.clear();
		for(int i=0; i<N; i++){
			char buf[0x100];
			scanf("%s ",buf);
			ws.push_back(string(buf));
		}
		for(int i=0; i<M; i++){
			char buf[0x100];
			scanf("%s ",buf);
			ans.push_back(solve(string(buf)));
		}
		printf("Case #%d: ",c);
		for(int i=0; i<(int)ans.size(); i++){
			printf("%s%c",ans[i].c_str(), i==M-1?'\n':' ');
		}
	}
	return 0;
}
