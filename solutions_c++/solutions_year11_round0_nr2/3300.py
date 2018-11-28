#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
#define mx 110
vector < string > comb,opp;
char in[mx];
int c,d,pos;
int mil(char cc){
	int i;
	for(i=0;i<c;i++){
		if((comb[i][0]==cc && comb[i][1]==in[pos-1]) || (comb[i][1]==cc && comb[i][0]==in[pos-1]))
			return i;
	}
	return -1;
}
int oppchk(char cc){
	int cur,i,j;
	for(i=0;i<d;i++){
		if(opp[i][0]==cc)cur = 1;
		else if(opp[i][1]==cc)cur = 0;
		else cur = 2;
		if(cur!=2){
			for(j=0;j<pos;j++)if(in[j]==opp[i][cur])return j;
		}
	}
	return -1;
}

int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,cas,i,n,r;
	char cc;
	string str;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%d",&c);
		for(i=0;i<c;i++){
			cin >> str;
			comb.push_back(str);
		}
		scanf("%d",&d);
		for(i=0;i<d;i++){
			cin >> str;
			opp.push_back(str);
		}
		scanf("%d",&n);
		getchar();
		pos = 0;
		while(n--){
			scanf("%c",&cc);
			r = mil(cc);
			if(r!=-1){
				pos--;
				in[pos++] = comb[r][2];
				continue;
			}
			r = oppchk(cc);
			if(r!=-1){
				pos=0;
				continue;
			}
			in[pos++] = cc;
		}
		printf("Case #%d: ",cas);
		printf("[");
		if(pos)printf("%c",in[0]);
		for(i=1;i<pos;i++)printf(", %c",in[i]);
		printf("]\n");
		comb.clear();
		opp.clear();
	}
	return 0;
}