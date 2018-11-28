#include <iostream>
#include <cstdlib>
#include <cstring>
#include <map>
#define maxn 101
#define maxm 10001

using namespace std;

struct node {
	node* next;
	int num;
};

string s[maxn];
map<string,int> rank[maxm];
node* g[maxm];
int i,n,m,tt,ii,a,b,j,num;

void maketree(int n) {
	for (i=1;i<=n;++i)
		getline(cin,s[i]);

	int k,last;
	node* p;
	string s1;
	for (i=1;i<=n;++i) {
		last=0;
		s[i]+='/';
		s[i].erase(0,1);
		while ((k=s[i].find('/'))!=(int)s[i].npos) {
			s1=s[i].substr(0,k);
			s[i].erase(0,k+1);
			if (!rank[last].count(s1)) {
				rank[last][s1]=++num; k=num;
				p=new node;
				p->next=g[last];
				p->num=k;
				g[last]=p;
				//cout << last << " " << k << endl;
				last=k;
			} else last=rank[last][s1];
		}
	}
}

int count(int x) {
	node* p=g[x];
	int cnt=1;
	while (p!=0) {
		cnt+=count(p->num);
		p=p->next;
	}
	return cnt;
}

int main() {
	freopen("fix.in","r",stdin);
	freopen("fix.out","w",stdout);

	scanf("%d\n",&tt);

	for (ii=1;ii<=tt;++ii) {
		scanf("%d%d\n",&n,&m);

		memset(g,0,sizeof(g));
		for (i=0;i<maxn;++i) rank[i].clear();
		num=0;
		maketree(n);
		a=count(0);
		maketree(m);
		b=count(0);
		if (b-a>0) printf("Case #%d: %d\n",ii,b-a);
		else printf("Case #%d: 0\n",ii);
	}
}
