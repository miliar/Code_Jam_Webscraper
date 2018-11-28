#include<stdio.h>
#include<algorithm>
#include<map>
#include<vector>
#include<string>
using namespace std;
#define VI vector<int>
#define MP make_pair
#define PB push_back
#define FS first
#define SD second

map<string,int> nazwa;

vector<int>listy[200];

void czysc() {
	nazwa.clear();
	for(int i=0;i<200;i++) {
		listy[i].clear();
	}
}

int zwrocdodaj(string czar) {
	if(!nazwa.count(czar)) {
		nazwa[czar]=nazwa.size()-1;
	}
	return nazwa[czar];
}

char tmp[200];


int n,s,q;
int main() {
	scanf("%d",&n);
	int id=1;
	while(n--) {
		scanf("%d\n",&s);
		czysc();
		for(int i=0;i<s;i++) {
			gets(tmp);
			zwrocdodaj(string(tmp));
		}
		scanf("%d\n",&q);
		for(int i=0;i<q;i++) {
			gets(tmp);
			listy[nazwa[tmp]].push_back(i);
		}
		int wyn=0,jest=0;
		//printf("%d %d ",s,q);
		while(jest<q) {
			int maks=-100;
			for(int i=0;i<s;i++) {
				//for(int i2=0;i2<listy[i].size();i2++) printf("%d ",listy[i][i2]);printf("\n");
				VI::iterator t=lower_bound(listy[i].begin(),listy[i].end(),jest);
				if(t==listy[i].end()) maks=10000;
				else maks>?=*t;
			}
			wyn++;jest=maks;
		}
		if(wyn>0) wyn--;
		printf("Case #%d: %d\n",id++,wyn);
	}
	return 0;
}
