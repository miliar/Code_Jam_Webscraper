#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A_out.txt","w",stdout);
	int t,i,j,k,ans,n,m,len;
	scanf("%d",&t);
	char s[150];
	string tmp;
	for(i=1;i<=t;i++) {
        printf("Case #%d: ",i);
		ans=0;
		map<string,int> my;
		scanf("%d%d",&n,&m);
		for (j=1;j<=n;j++) {
			scanf("%s",s);
			len=strlen(s);
			for (k=1;k<len;k++) {
				if (s[k]=='/') {
					s[k]='\0';
					tmp=s;
					if (my.count(tmp) == 0) {
						my[tmp] = 1;
					}
					s[k] = '/';
				}
			}
			tmp=s;
			if (my.count(tmp)==0) my[tmp] = 1;
		}
		for (j=1;j<=m;j++) {
			scanf("%s",s);
			len=strlen(s);
			for (k=1;k<len;k++) {
				if (s[k]=='/') {
					s[k]='\0';
					tmp=s;
					if (my.count(tmp) == 0) {
						my[tmp] = 1;
						ans++;
					}
					s[k]='/';
				}
			}
			tmp=s;
			if (my.count(tmp) == 0) {
				my[tmp] = 1;
				ans++;
			}
		}
		printf("%d\n",ans);
		my.clear();
	}
}
