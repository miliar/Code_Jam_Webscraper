#include <cstdio>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;


int ntc,L,n,nodes,c,act;
char cechy[200][200];
int tab[200][3];
char buff[100000];
stack<int> S;
char str[200][20];
double p[200],wyn;
bool leaf[200];


void dfs(int x) {
	wyn*=p[x];
	if(leaf[x]) return;
	bool okk=0;
	for(int i=0; i<c; ++i)  {
		act=0; bool ok=1;
		while(1) {
			if(str[x][act]!=cechy[i][act]) {ok=0; break; }
			if(str[x][act]=='\0') break;
			++act;
		}
		if(ok) { okk=1; break; }
	}
	if(okk) dfs(tab[x][0]);
	else dfs(tab[x][1]);
}
		


int main() {
	scanf("%d", &ntc);
	for(int cas=1; cas<=ntc; ++cas) {
		scanf("%d ", &L);
		n=0; nodes=0;
		while(L--) {
			cin.getline(&buff[n], 1000, '\n');
			while(buff[n]!='\0') ++n;
			buff[n]=' ';
			++n;
		}
		for(int i=0; i<n; ++i) {
			while(buff[i]==' ') ++i;
			if(buff[i]==')' || i>=n) continue;
			if(buff[i]=='(') ++i;
			if(!S.empty()) { if(tab[S.top()][0]==-1) tab[S.top()][0]=nodes; else tab[S.top()][1]=nodes; S.pop(); }
			while(buff[i]==' ') ++i;
				double m=1,w=0;			
			if(buff[i]=='1'){  w=1; ++i; ++i; while(buff[i]>='0' && buff[i]<='9') ++i; }
			else {
			i+=2;
			while(buff[i]>='0' && buff[i]<='9') {
				m/=(float)10;
				w+=m*(buff[i]-'0');
				++i;
			}}
			p[nodes]=w;
			while(buff[i]==' ') ++i;
			if(buff[i]==')') { leaf[nodes++]=1; continue;}
			leaf[nodes]=0;
			int sp=0;
			while(buff[i]>='a' && buff[i]<='z') {
				 str[nodes][sp++]=buff[i++];
			}
			str[nodes][sp]='\0';
			tab[nodes][0]=-1;
			tab[nodes][1]=-1;
			S.push(nodes); S.push(nodes);
			nodes++;
		}
		scanf("%d",&L);
		printf("Case #%d:\n", cas);
		while(L--) {
			scanf("%s", cechy[0]);
			scanf("%d", &c);
			for(int i=0; i<c; ++i) {
				scanf("%s", cechy[i]);
			}
			wyn=1;
			dfs(0);
			printf("%.7F\n", wyn);
			
		}
		
	}
}
