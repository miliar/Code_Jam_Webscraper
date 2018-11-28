#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

#define N 100009
#define M 120
#define ll long long
#define inf 1<<30
#define lson (id<<1)
#define rson (id<<1|1)

#define eps 1e-8
#define pii pair<int,int>
#define pdd pair<double,double>
#define It map<unsigned,string>::iterator
#define MP(i,j) make_air(i,j)
#define PB push_back
#define VI vector<int>
#define lchild(id) (id<<1)
#define rchild(id) ((id<<1)|1)
#define base 2048

char a[]={"ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv"};
char b[]={"our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up"};
map<char,char> mp;
int n;
char ch[N];
int main() {
#ifndef	ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int len=strlen(a);
	for(int i=0;i<len;i++)
		mp[a[i]]=b[i];
	mp['z']='q';
	mp['q']='z';
	int cas,pcas=1;
	scanf("%d\n",&cas);
	while(cas--){
		gets(ch);
		len=strlen(ch);
		printf("Case #%d: ",pcas++);
		for(int i=0;i<len;i++)
			putchar(mp[ ch[i] ]);
		puts("");
	}
	return 0;
}