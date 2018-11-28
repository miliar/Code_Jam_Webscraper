#include<iostream>
#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

string comb[100];
string oppo[100];
string seq;
int T,C,D,N;

bool isOpposed(char c, char d) {
	for(int i=0;i<D;i++)
		if(oppo[i][0]==c && oppo[i][1]==d || oppo[i][0]==d && oppo[i][1]==c)
			return true;
	return false;
}

char combine(char c, char d) {
	for(int i=0;i<C;i++)
		if(comb[i][0]==c && comb[i][1]==d || comb[i][0]==d && comb[i][1]==c)
			return comb[i][2];
	return '-';
}

vector<char> solve() {
	vector<char> ret;
	char last='-';
	char com;
	for(int i=0;i<N;i++) {
		ret.push_back(seq[i]);
//		printf("adding %c\n", seq[i]);
		if((com=combine(seq[i],last))!='-') {
			ret.pop_back(); ret.pop_back();
			ret.push_back(com);
//			printf("combining... %c %c = %c\n", seq[i], last, last);
			last=com;
		} else last=seq[i];

		for(int j=0;j<ret.size()-1;j++)
			if(isOpposed(last,ret[j])) {
//				printf("clearing\n");
				last='-';
				ret.clear();
				break;
			}
	}
	return ret;
}

int main() {
	int k = 0;
	scanf("%d", &T);
	while(T--) {
		scanf("%d", &C);
		for(int i=0;i<C;i++) cin>>comb[i];
		scanf("%d", &D);
		for(int i=0;i<D;i++) cin>>oppo[i];
		scanf("%d", &N);
		cin>>seq;
		vector<char> res = solve();
		if ( res.size() == 0 ) printf("Case #%d: []\n",++k);
		else {
			printf("Case #%d: [", ++k);
			for(int i=0;i<int(res.size()-1);i++) printf("%c, ", res[i]);
			printf("%c]\n",res[res.size()-1]);
		}
	}
}
