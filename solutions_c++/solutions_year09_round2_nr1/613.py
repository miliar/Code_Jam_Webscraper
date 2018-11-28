#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <map>
using namespace std;

map <string,int> mp;

bool f[100000],ok[100000];
double val[100000];
int p,m,n,x[100000];

double query(int num)
{
	if(f[num]) return val[num];
	else if(ok[x[num]]) return query(num*2) * val[num];
	else return query(num*2+1) * val[num];
}

void create(int num) 
{
	int i;
	char c;
	string str;
	
	while(1) {
		scanf("%c",&c);
		if(c=='(') break;
	}
	
	scanf("%lf",&val[num]);
	
	while(1) {
		scanf("%c",&c);
		if(c==')') break;
		else if(c>='a' && c<='z') str += c;
		else if(str.size()) break;
	}
	
	if(str.size()) {
		mp[str] = ++p;
		x[num] = p;
		
		create(num*2);
		create(num*2+1);
		
		while(1) {
			scanf("%c",&c);
			if(c==')') break;
		}
	}
	else f[num]=1;
	
	return;
}

int main()
{
	int T,t,i,j;
	string str;
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&T);
	
	for(t=1;t<=T;t++) {
		printf("Case #%d:\n",t);
		scanf("%d",&n);
		p=0;
		mp.clear();
		memset(f,0,sizeof(f));
		
		create(1);
		
		scanf("%d",&n);
		
		for(i=0;i<n;i++) {
			cin >> str;
			scanf("%d",&m);
			
			memset(ok,0,sizeof(ok));
			
			for(j=0;j<m;j++) {
				cin >> str;
				if(mp[str]==0) mp[str] = ++p;
				ok[mp[str]]=1;
			}
			
			printf("%lf\n",query(1));
		}
	}
}

