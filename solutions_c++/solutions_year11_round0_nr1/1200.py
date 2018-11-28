#include<cstdio>
#include<string>
#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

long long solve(vector<bool> bot,vector<int> seq[]) {
	int pos[]={1,1},id[]={0,0};
	long long rpta=0;
	for(int i=0;i<bot.size();i++) {
		int k=bot[i];
		int mv=abs(seq[k][id[k]]-pos[k])+1;
		if(id[1-k]<seq[1-k].size()) {
			int mv2=abs(seq[1-k][id[1-k]]-pos[1-k]);
			if(mv>mv2)
				pos[1-k]=seq[1-k][id[1-k]];
			else {
				if(pos[1-k]<seq[1-k][id[1-k]])
					pos[1-k]+=mv;
				else
					pos[1-k]-=mv;
			}
		}
		rpta+=mv;
		pos[k]=seq[k][id[k]];
		id[k]++;
	}
	return rpta;
}

int main() {
	int t;
	scanf("%d",&t);
	for(int caso=1;caso<=t;caso++) {
		int n;
		scanf("%d",&n);
		string tt;
		int ttt;
		vector<bool> bot;
		vector<int> seq[2];
		for(int i=0;i<n;i++) {
			cin>>tt;
			scanf("%d",&ttt);
			if(tt=="O") {
				bot.push_back(0);
				seq[0].push_back(ttt);
			}
			else {
				bot.push_back(1);
				seq[1].push_back(ttt);
			}
		}
		printf("Case #%d: %lli\n",caso,solve(bot,seq));
	}
}
