#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <cctype>
#include <algorithm>
#include <vector>
#include <numeric>
#include <set>
#include <queue>
#include <map>
#include <list>
#include <string>
#include <iostream>
#include <stack>
#include <sstream>
using namespace std; 
#define PB push_back
#define MP make_pair
#define F first
#define S second 
#define BE(a) a.begin(),a.end() 
#define CLS(a,b) memset(a,b,sizeof(a))
#define SZ(a) ((int)a.size())
const long double pi=acos(-1.0);
#define torad(a) ((a)*pi/180.0)
typedef vector<int> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 
typedef pair<int,int> pii ; 
typedef long long ll ; 
typedef long double ld ; 
typedef double dl ; 
class node {public:
};
typedef vector<node> vn ; 
int cases,g;
stringstream google("ejp mysljylc kd kxveddknmc re jsicpdrysi \
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd \
de kr kd eoya kw aej tysr re ujdr lkgc jv");
stringstream english("our language is impossible to understand \
there are twenty six factorial possibilities \
so it is okay if you want to just give up");
char cmap[26]={0};
bool vis[26]={0};
string readline() {
  string ret;
  char c;
  while(scanf("%c",&c)!=EOF) {
    if(c == '\n')
      return ret;
    ret+=c;
  }
  return ret;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
////////////////////////////////////////////
  char c1,c2;
  cmap['q'-'a']='z';
  cmap['z'-'a']='a'+16;
  while(google >> c1) {
    english >> c2;
    if(!isspace(c1)) {
      cmap[c1-'a'] = c2;
      vis[c2-'a']=1;
    }
  }
	scanf("%d\n",&cases);
	for(g=0;g<cases;g++)
	{
    printf("Case #%d: ",g+1);
    string line = readline();
    for(int i=0;i<line.size();++i) {
      if(!isspace(line[i])) {
        printf("%c",cmap[line[i]-'a']);
      } else {
        printf("%c",line[i]);
      }
    }
    printf("\n");
	}

	return 0;
}