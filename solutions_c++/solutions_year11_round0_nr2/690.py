#include <cstdio>
#include <limits.h>
#include <vector>
#include <string.h>
using namespace std;

#define SZ(v) ((int)(v).size())
#define PB push_back

int combine[26][26];
vector<int> opposed[26];

char s[1000];

void run(int casenr) {
	memset(combine,-1,sizeof(combine));
	int ncombine; scanf("%d",&ncombine);
	for(int i=0;i<ncombine;++i) {
		char a,b,c; scanf(" %c%c%c",&a,&b,&c);
		combine[a-'A'][b-'A']=c-'A';
		combine[b-'A'][a-'A']=c-'A';
	}
	for(int i=0;i<26;++i) opposed[i]=vector<int>();
	int noppose; scanf("%d",&noppose);
	for(int i=0;i<noppose;++i) {
		char a,b; scanf(" %c%c",&a,&b);
		opposed[a-'A'].PB(b-'A');
		opposed[b-'A'].PB(a-'A');
	}

	int n; scanf("%d %s",&n,s);
	vector<int> cnt(26,0);


	vector<int> have;
	for(int i=0;i<n;++i) {
		int cur=s[i]-'A';
		++cnt[cur]; have.PB(cur);
		while(SZ(have)>=2&&combine[have[SZ(have)-2]][have[SZ(have)-1]]!=-1) {
			cur=combine[have[SZ(have)-2]][have[SZ(have)-1]];
			--cnt[have.back()]; have.pop_back();
			--cnt[have.back()]; have.pop_back();
			++cnt[cur]; have.PB(cur);
		}
		for(int j=0;j<SZ(opposed[cur]);++j) if(cnt[opposed[cur][j]]!=0) {
			have.clear();
			cnt=vector<int>(26,0);
			break;
		}
	}
	printf("Case #%d: [",casenr);
	for(int i=0;i<SZ(have);++i) {
		if(i!=0) printf(", ");
		printf("%c",'A'+have[i]);
	}
	printf("]\n");
}

int main() {
	int n; scanf("%d",&n); for(int i=1;i<=n;++i) run(i);
	return 0;
}
