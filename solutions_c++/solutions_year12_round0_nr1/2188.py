//BISMILLAHIRRAHMANIRRAHIM



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cctype>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define pii pair < int , int >
#define i64 long long
#define CLR(x) memset(x,0,sizeof x)
#define SET(x,y) memset(x,y,sizeof x)
#define PB(x) push_back(x)

char ln1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi\
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\
de kr kd eoya kw aej tysr re ujdr lkgc jv";

char ln2[]="our language is impossible to understand\
there are twenty six factorial possibilities\
so it is okay if you want to just give up";

int main() {
	freopen("A-small-attempt1.bin","r",stdin);
	freopen("out2.txt","w",stdout);
	char cv[130],ln[130];
	int i;
	for(i=0;i<128;i++) cv[i]=i;
	for(i=0;ln1[i];i++) if(ln1[i]>='a' && ln1[i]<='z') cv[ln1[i]]=ln2[i];
	//for(i=0;ln1[i];i++) if(ln1[i]>='a' && ln1[i]<='z') vis[ln2[i]]=1;
	cv['q']='z';
	cv['z']='q';
	//for(i='a';i<='z';i++) cout<<char(i)<<' '<<cv[i]<<'\n';
	//for(i='a';i<='z';i++) if(!vis[i]) cout<<char(i)<<' '<<cv[i]<<'\n';
	int I,T;
	cin>>T;
	gets(ln);
	for(I=1;I<=T;I++) {
		gets(ln);
		for(i=0;ln[i];i++) ln[i]=cv[ln[i]];
		printf("Case #%d: %s\n",I,ln);
	}
	return 0;
}
