#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;

#define PII pair<int,int>
#define mkp(a,b) make_pair(a,b)
#define x first
#define y second
#define LL long long
#define CPX complex<double>
#define ME(a) memset(a,0,sizeof(a))
#define MM(a,b) memset(a,b,sizeof(a))
#define MCP(a,b) memcpy(a,b,sizeof(a))

#define ULL unsigned long long

const ULL pr = 27ull;

ULL pw [20];

map<ULL,vector<PII > > hash;

string S[11111];
int mask[11111];
int pos[11111][27];
int N, M;
ULL orig[11111], empt[11111];
char buf[10000];

ULL Deal(string &s, int marked) {
	ULL val = 0;
	int contain = 0, have = 0;
	for(int i=0;i<s.size();++i) {
		if(marked & 1 << i) {
			val += 26 * pw[i];
			contain |= (1 << s[i] - 'a');
		} else {
			
			val += (s[i]-'a') * pw[i];
		}
		have |= (1 << s[i] - 'a');
}
	//if(s=="ade") cout << "have = "<<have<<"  contain = "<<contain<<endl;
	//hash[val] |= contain;
	hash[val].push_back(mkp(have, contain));
	return val;
}

string L;

set<ULL > rec[11111];

int Run(int ind, bool flag = false) {
	flag=false;
	if(flag) cout << "Now Guess S = "<<S[ind]<<endl;
	
	string &s = S[ind];
	int unk = (1 << s.size() ) - 1;
	int contain = mask[ind];
	int ret = 0;
	int rem = 0;
	ULL cur = 0;
	for(int i=0;i<s.size();++i)
		cur = cur * pr + 26;
	for(int i=0;i<L.size() && unk;++i) {
		int c = L[i] - 'a';
		if(contain & 1 << c) {
			
			if(flag){
			cout << "--> Bingo "<<char('a'+c)<<"  : ";
			for(int k=0;k<s.size();++k)
				if(unk&1<<k) cout << "_";else cout << s[k];cout<<endl;
			}
		
			
			unk ^= pos[ind][c];
			for(int j=pos[ind][c];j>0;j&=j-1){
				int p = __builtin_ctz(j);
				cur -= pw[p] * 26;
				cur += pw[p] * c;
			}
		} else {
			/*
			if(hash[cur] & 1 << c) {
				++ ret;
				if(flag){
				cout << "   > c = "<<char ('a' + c) << " Loss!!!"<<endl;
				for(int k=0;k<N;++k)
				if(rec[k].find(cur) != rec[k].end() && (mask[k]&1<<c))
				cout <<"        --> "<<S[k]<<endl;
				}
				
			}*/
			if(hash.find(cur) != hash.end()) {
				vector<PII > & arr = hash[cur];
				bool ok=false;
				for(int k=0;k<arr.size()&&!ok;++k){
					if(arr[k].x & rem) continue;
					if(arr[k].y & 1<<c) ok=true;
				}
				if(ok) {rem |= 1<< c;
					++ ret;
					if(flag)cout << "---> guess "<<char('a'+c)<<endl; 
				}
			}
		}
	}
	
	
	if(flag)cout << "#### ret = "<<ret<<endl;
	return ret;
}

int Solve() {
	scanf("%d %d", &N, &M);
	hash.clear();
	ME(mask); ME(pos);
	for(int i=0;i<N;++i){
		scanf("%s", buf);
		S[i] = buf;
		mask[i] = 0;
		for(int j=0;j<S[i].size();++j) {
			mask[i] |= (1 << S[i][j] - 'a');
			pos[i][S[i][j]-'a']|=(1<<j);
		}
		orig[i]=Deal(S[i], 0);
		
		rec[i].clear();
		rec[i].insert(orig[i]);
		
		for(int sub = mask[i]; sub > 0; sub = mask[i] & sub - 1) {
			int totpos = 0;
			for(int j=sub;j>0;j=j&(j-1)){
				int p = __builtin_ctz(j);
				totpos |= pos[i][p];
			}
			ULL tmp = Deal(S[i], totpos);
			if(totpos == (1<<S[i].size())-1) empt[i] = tmp;
			
			rec[i].insert(tmp);
			
		}
	}
	
	for(int i=0;i<M;++i) {
		scanf("%s",  buf);
		L = buf;
		int res = -1, chs = -1;
		for(int j=0;j<N;++j) {
			int temp = Run(j);
			if(temp > res) {
				res = temp; chs = j;
			}
		}
		
	//	cout << "--> Res = "<<res<<endl;
		Run(chs, true);
	//	cout <<"#### STD ####"<<endl;
	//	if()
		printf(" %s", S[chs].c_str());
	}
	printf("\n");
}

int main() {
	pw[0] = 1;
	for(int i=1;i<20;++i) pw[i] = pw[i-1] * pr;
	
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int test;scanf("%d", &test);
	for(int no=1;no<=test;++no){
		printf("Case #%d:",no);
		Solve();
	}
}
