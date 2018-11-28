#include<iostream>
#include<sstream>
#include<string>
#include<set>
using namespace std;
char *o;
char buf[1000000], str[1000000];
int sz;

char tt[10000];

struct node {
	double val;
	string tar;
	bool mark;
	int l, r;
}t[1000000];
int n;

double getf() {
	while(!isdigit(*o)) ++o;
	double a=0;
	while(isdigit(*o)) a=a*10+(*o++-'0');
	if(*o!='.') return a;
	else {
		++o;
		double b = 0, y = 1;
		while(isdigit(*o)) {
			y/=10;
			b+=y*(*o++-'0');
		}
		return a+b;
	}
}

int Dfs(int L, int R) {
	int p = n++;
	t[p].mark=true;t[p].val=0;t[p].l=t[p].r=-1;
	o = str+L;
	t[p].val = getf();
	while(*o<'a'||*o>'z') {
		if(*o==')') break;
		++o;
	}
	if(*o==')') return p;
	string s;
	while(*o<'a'||*o>'z')++o;
	while(*o>='a'&&*o<='z')s.push_back(*o++);
	t[p].tar=s;
	t[p].mark=false;
	int k = 0;
	int prel = -1;
	for(int i=L+1;i<R;++i) {
		if(str[i]=='(') {
			++k;
			if(k == 1) prel = i;
		}
		if(str[i]==')') {
			--k;
			if(!k) {
				if(t[p].l<0) t[p].l=Dfs(prel, i);
				else t[p].r=Dfs(prel,i);
				prel = -1;
			}
		}
	}
	return p;
}

int run() {
	memset(buf,0,sizeof(buf));
	memset(str,0,sizeof(str));
	int L;
	sz=0;
	sscanf(gets(tt),"%d", &L);
	for(int i=0;i<L;++i) {
		gets(tt);
		int l = strlen(tt);
		for(int j=0;j<l;++j) {
			str[sz++] = tt[j];
		}
	}
	
	n=0;
	int R;
	L = 0; R = sz-1;
	for(;str[L]!='(';++L);for(;str[R]!=')';--R);
	int rt=Dfs(L, R);
	int N;
	sscanf(gets(tt),"%d", &N);
	for(int i=0;i<N;++i) {
		string a;
		gets(tt);
		stringstream ss;
		ss<<tt;
		ss>>a;
		int m;
		ss>>m;
		set<string> h;
		while(m--) {
			ss>>a;
			h.insert(a);
		}
		double val = 1;
		int p = rt;
		while(1) {
			val *= t[p].val;
			if(t[p].mark) break;
			if(h.find(t[p].tar)!=h.end()) p=t[p].l;
			else p=t[p].r;
		}
		printf("%.7lf\n", val);
	}
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int test; 
	sscanf(gets(tt),"%d", &test);
	for(int no=1;no<=test;++no) {
		printf("Case #%d:\n", no);
		run();
	}
}
