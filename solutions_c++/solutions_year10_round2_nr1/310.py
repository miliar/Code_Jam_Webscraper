
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

using namespace std;
int m, n;
char buf[19999];
struct dir { 
    string name;
    map<string,dir> d;
    int put() {
	char c = getchar();
	if( c == '/') {
	scanf("%[^\n/]",buf);
//	cout << buf << endl;
	string s (buf);
	if( d.count(buf) )
	   return d[buf].put();
       return 1 + d[buf].put();	
	}
	return 0;
    }
};
int main()
{
   int k, t, tests;
   scanf("%d",&tests);
   int g;
   long long answer;
   for(g = 1; g <= tests; g++) {
       dir root;
       answer = 0;
       scanf(" %d %d\n",&n,&m);
       while(n--) {
	   root.put();
       }
       while(m--) {
	   answer += root.put();
       }
       printf("Case #%d: %lld\n",g,answer);
   }
   return 0;
}
