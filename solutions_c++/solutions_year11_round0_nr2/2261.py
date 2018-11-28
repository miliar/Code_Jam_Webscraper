#include <cstdio>
#include <deque>
#include <cstring>
using namespace std;

deque<char> p;
char trans[36][4];
char cann[36][4];
int has[255] = {0};
char inp[1024];

void solve(){
	int c,d,n;
	p.clear();
	scanf("%d", &c);
	
	memset(has, 0, sizeof has);
	for (int i=0;i<c;++i){
		scanf(" %s", trans[i]);
	}
	scanf(" %d", &d);
	for (int i=0;i<d;++i){
		scanf(" %s", cann[i]);
	}
	scanf(" %d", &n);
	scanf(" %s", inp);
	
	for (int i=0;i<n;++i){
		p.push_back( inp[i] );
		has[inp[i]]++;
		if (p.size() >= 2){
			int psize = p.size();
			for (int j=0;j<c;++j){
				if (psize <= 1) break;
				
				if ( (p[ psize-1] == trans[j][0] && p[psize-2] == trans[j][1]) || (p[psize-2]==trans[j][0]&&p[psize-1]==trans[j][1])){
					has[ p[psize-1] ]--;
					has[ p[psize-2] ]--;
					p.pop_back();
					p.pop_back();
					p.push_back( trans[j][2] );
					has[ trans[j][2] ]++;
					psize--;
					j=-1;
				}
				
			}
		}
		for (int j=0;j<d;++j){
			if (has[ cann[j][0] ] && has[ cann[j][1] ]){
				memset(has, 0, sizeof has);
				p.clear();
				break;
			}
		}
	}
	printf("[");
	for (int k=0;k<p.size();++k){
		if (k) printf(", ");
		printf("%c",p[k]);
	}
	printf("]\n");
}


int main(){
	int T;
	scanf("%d", &T);
	for (int tc=1;tc<=T;++tc){
		printf("Case #%d: ",tc);
		solve();
	}
	return 0;
}
