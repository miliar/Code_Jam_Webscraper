#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <valarray>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <queue>
using namespace std;

char s[100000];

char t[1000];
set<string> save;


struct node {
int a[2];
char f[12];
double w;
};

node b[10000];
int n;

int makenode(int no,char x) {
char c;
int i,j=0;
	b[no].a[0]=b[no].a[1]=-1;
	while (!isdigit(s[x])) {
		++x;
	}
	int y=x;
	while ((s[x]=='.') || isdigit(s[x])) {
		++x;
	}
	c=s[x];
	s[x]=0;
	sscanf(s+y,"%lf",&b[no].w);
	s[x]=c;
	for (;;++x) {
		if (s[x]==')') {
			return x;
		}
		if (isalpha(s[x])) {
			i=0;
			while (isalpha(s[x])) {
				b[no].f[i++]=s[x++];
			}
			b[no].f[i]=0;
		}
		if (s[x]=='(') {
			b[no].a[j++]=n;
			x=makenode(n++,x);
		}
	}
	return x;
}





int main() {
int i,j,z,zz;
double p;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&zz);
	gets(s);
	for (z=1;z<=zz;++z) {
		printf("Case #%d:\n",z);
		s[0]=0;
		scanf("%d",&i);
		gets(t);
		for (;i;--i) {
			gets(t);
			strcat(s,t);
			n=strlen(s);
			s[n]=' ';
			s[n+1]=0;
		}
		for (i=0;s[i]!='(';++i)
		;
		n=1;
		makenode(0,i);
		for (scanf("%d",&n);n;--n) {
			for (scanf("%s%d",s,&j),save.clear();j;--j) {
				scanf("%s",s);
				save.insert(s);
			}
			gets(s);
			for (i=0,p=1;i>=0;) {
				p*=b[i].w;
				i=(save.find(b[i].f)==save.end())?b[i].a[1]:b[i].a[0];
			}
			printf("%.7lf\n",p);
		}

	}

	return 0;
}




	
