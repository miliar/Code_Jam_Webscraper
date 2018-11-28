#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define ABS(x) ((x<0)?(-(x)):(x))
#define equal(a,b) (ABS((a)-(b))<eps)
#define eps (1e-9)
#define mp make_pair
#define pb push_back
#define px first
#define py second
#define pair pair<int,int>

using namespace std;

int dx[8]={0, 0, 1,-1, 1, 1,-1,-1};
int dy[8]={1,-1, 0, 0,-1, 1,-1, 1};
int kx[8]={1, 1,-1,-1, 2, 2,-2,-2};
int ky[8]={2,-2, 2,-2, 1,-1, 1,-1};

int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	int T;
	char line[200];
	char s[200];
	char d[200];
	char map[26]= {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	gets(line);
	sscanf(line,"%d",&T);
	for(int t=1; t<=T; t++){
		gets(s);
		printf("Case #%d: ",t);
		for(int i=0; s[i]!='\0'; i++){
			if('a'<=s[i] && s[i]<='z'){
				printf("%c",map[s[i]-'a']);
			} else {
				printf("%c",s[i]);
			}
		}
		printf("\n");
	}
	return 0;
}
