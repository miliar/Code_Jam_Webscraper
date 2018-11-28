
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <set>

using namespace std;

#define db(x) cout << #x " == " << x << endl
#define _ << ", " <<
#define Fr(a,b,c) for( int a = b ; a < c ; ++a )
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
#define F first
#define S second
#define MP make_pair
#define PB push_back

map<char,char> mapa;
char ent[200];
int t;

void p(){
	int l=strlen(ent);
//	printf("%s %d\n",ent, l);
	Fr(i,0,l) if(ent[i]>='a' && ent[i]<='z') { ent[i]=mapa[ent[i]];}
}

int main(){
	mapa['a'] = 'y';
	mapa['b'] = 'h';
	mapa['c'] = 'e';
	mapa['d'] = 's';
	mapa['e'] = 'o';
	mapa['f'] = 'c';
	mapa['g'] = 'v';
	mapa['h'] = 'x';
	mapa['i'] = 'd';
	mapa['j'] = 'u';
	mapa['k'] = 'i';
	mapa['l'] = 'g';
	mapa['m'] = 'l';
	mapa['n'] = 'b';
	mapa['o'] = 'k';
	mapa['p'] = 'r';
	mapa['q'] = 'z';
	mapa['r'] = 't';
	mapa['s'] = 'n';
	mapa['t'] = 'w';
	mapa['u'] = 'j';
	mapa['v'] = 'p';
	mapa['x'] = 'm';
	mapa['w'] = 'f';
	mapa['y'] = 'a';
	mapa['z'] = 'q';
	
	scanf("%d",&t);
	getchar();
	Fr(cas,1,t+1){
		gets(ent);
		p();
		printf("Case #%d: %s\n",cas,ent);
	}
	return 0;
}