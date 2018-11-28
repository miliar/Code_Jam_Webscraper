#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<cmath>
#include<map>
#include<string>
#include<set>
#include<cstring>
#include<iostream>
#include<sstream>
using namespace std;
 
#define PB push_back
#define FORE(i,t) for(typeof(t.begin())i=t.begin();i!=t.end();++i)
#define SZ(x) int((x).size())

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const int INF=1000111222;

int a[1<<10];

void inline jeden() {
	int p;
	scanf("%d",&p);
	int n=1<<p;
	for(int i=0;i<n;++i) {
		scanf("%d",a+i);
		a[i]=p-a[i];
	}
	for(int i=0,ile=n/2;i<p;++i,ile/=2) {
		for(int j=0;j<ile;++j)
			scanf("%*d");
	}
	int wynik=0;
	for(int k=0;k<p;++k) {
		int len=(1<<(p-k));
		int ile=n/len;
		for(int i=0;i<ile;++i) {
			bool any=false;
			for(int j=0;j<len;++j) {
				if(a[i*len+j]>0) {
					any=true;
					break;
				}
			}
			if(any) {
				++wynik;
				for(int j=0;j<len;++j) {
					--a[i*len+j];
				}
			}
		}
	}
	printf("%d\n",wynik);
}

int main() {
	int testow;
	scanf("%d",&testow);
	for(int z=1;z<=testow;++z) {
		printf("Case #%d: ",z);
		jeden();
	}
}
