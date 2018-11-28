#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<cstdio>
#include<sstream>

//#define LL long long
#define LL __int64
#define MAX 100000
#define eps 1e-9

using namespace std;

int testCase;
map<char,char> mp;
char a[100];
int main(){
	int i,j,k,l,n,ans;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d\n",&testCase);
	mp.clear();
	mp['a'] = 'y';
         mp['b'] = 'h';
         mp['c'] = 'e';
         mp['d'] = 's';
         mp['e'] = 'o';
         mp['f'] = 'c';
         mp['g'] = 'v';
         mp['h'] = 'x';
         mp['i'] = 'd';
         mp['j'] = 'u';
         mp['k'] = 'i';
         mp['l'] = 'g';
         mp['m'] = 'l';
         mp['n'] = 'b';
         mp['o'] = 'k';
         mp['p'] = 'r';
         mp['q'] = 'z';
         mp['r'] = 't';
         mp['s'] = 'n';
         mp['t'] = 'w';
         mp['u'] = 'j';
         mp['v'] = 'p';
         mp['w'] = 'f';
         mp['x'] = 'm';
         mp['y'] = 'a';
         mp['z'] = 'q';

	for(int case_Id = 1; case_Id <= testCase; case_Id ++){
        gets(a);
        printf("Case #%d: ",case_Id);
        for(i =0; i < strlen(a); i ++){
            if(a[i] >= 'a' && a[i] <= 'z') printf("%c",mp[a[i]]);
            else printf("%c",a[i]);
        }
        printf("\n");
	}


	return 0;
}
