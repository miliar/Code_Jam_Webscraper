#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <sstream>

using namespace std;

char a[12][20000000];
int b[12];
int q;

int f(int x,int y) {
	//cout<<q<<' '<<x<<endl;
	if (x>=20000000) return 2;
	if (y>=10000) return 2;
	if (a[q][x]>0) return a[q][x];
	a[q][x]=2;
	int s=0;
	int z=x;
	while(z) {
		int u=z%q;
		s+=u*u;
		z/=q;
	}
	if (s==x) s=2; else s=f(s,y+1);
	a[q][x]=s;
	return s;
}

int main() {
	memset(a,0,sizeof a);
	for(q=2;q<11;q++) {
		a[q][1]=1;
		//for(int i=2;i<q;i++) a[q][i]=2;
		for(int j=2;j<15000000;j++) a[q][j]=f(j,0);
		//cout<<"A"<<endl;
	}
	cerr<<"AAA"<<endl;
	int TT;
	cin>>TT;
	char ch[111];
	gets(ch);
	for(int T=1;T<=TT;T++) {
		char t[100];
		gets(t);
		istringstream iss(t);
		int s=0;
		int x;
		while(iss>>x) {
			b[s++]=x;
		}
		//for(int i=0;i<s;i++) cin>>b[i];
		for(int i=2;i<15000000;i++) {
			bool ok=true;
			for(int j=0;j<s;j++) if (a[b[j]][i]!=1) {
				ok=false;
				break;
			}
			if (ok) {
				cout<<"Case #"<<T<<": "<<i<<endl;
				break;
			}
		}
	}
	return 0;
}

