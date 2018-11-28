#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<string>
#include<cmath>
using namespace std;
#define VI vector<int>
#define MP make_pair
#define PB push_back
#define FS first
#define SD second
#define PI pair<int,int>

#define MAX 24*62+4
#define MA 24*60

vector<int> czas[MAX];
int t;
void czysc() {
	for(int i=0;i<MAX;i++) czas[i].clear();
}

int n,s,b,q,na,nb;

PI ab[200];
PI ba[200];

int main() {
	scanf("%d",&n);
	int id=0;
	while(n--) {
		czysc();
		scanf("%d",&t);
		scanf("%d %d",&na,&nb);
		for(int i=0;i<na;i++) {
			int a,aa,b,bb;
			scanf("%d:%d %d:%d",&a,&aa,&b,&bb);
			ab[i]=MP(a*60+aa,b*60+bb+t);
			czas[ab[i].SD].push_back(2);
		}
		for(int i=0;i<nb;i++) {
			int a,aa,b,bb;
			scanf("%d:%d %d:%d",&a,&aa,&b,&bb);
			ba[i]=MP(a*60+aa,b*60+bb+t);
			czas[ba[i].SD].push_back(1);
		}
		for(int i=0;i<na;i++) {
			czas[ab[i].FS].push_back(-1);
		}
		for(int i=0;i<nb;i++) {
			czas[ba[i].FS].push_back(-2);
		}
		id++;
		int wyna=0,wynb=0;
		int akta=0,aktb=0;
		for(int i=0;i<MA;i++) {
			for(int i2=0;i2<czas[i].size();i2++) {
				int w=czas[i][i2];
				if(abs(w)==1) {
					if(w>0) akta++;
					else {
						if(akta>0) akta--;
						else wyna++;
					}
				}
				else {
					if(w>0) aktb++;
					else {
						if(aktb>0) aktb--;
						else wynb++;
					}
				}
			}
		}
		
		
		printf("Case #%d: %d %d\n",id,wyna,wynb);
	}

	return 0;
}

