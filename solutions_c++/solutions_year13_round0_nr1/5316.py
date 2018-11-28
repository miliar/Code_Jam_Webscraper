#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define mp make_pair
#define F first
#define S second

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define rp(a,c) fr(a,0,c)
#define fr_(a,b,c) for( int a = b ; a > c ; --a )
#define rp_(a,b) fr_(a,b,-1)

#define cl(a,b) memset((a),(b), sizeof(a))
#define db(x) cerr << #x " == " << x << "\n"
#define _ << ", " <<
#define INF 0x3f3f3f3f

typedef long long 			ll;
typedef unsigned long long 	ull;
typedef vector<int> 		vi;
typedef pair<int,int> 		pii;

#define maxn 0

int n, t;
char s[4][5];
char m[256], r;
int caso = 1;
int main(){
	scanf("%d", &t);
	m['.']=0;
	m['O']=1;
	m['X']=2;
	m['T']=3;
	
	while(t--){
		scanf("%s%s%s%s", s[0], s[1], s[2], s[3]);
		r = 0;
		r |= m[s[0][0]] & m[s[0][1]]&m[s[0][2]]&m[s[0][3]];
		r |= m[s[1][0]] & m[s[1][1]]&m[s[1][2]]&m[s[1][3]];
		r |= m[s[2][0]] & m[s[2][1]]&m[s[2][2]]&m[s[2][3]];
		r |= m[s[3][0]] & m[s[3][1]]&m[s[3][2]]&m[s[3][3]];

		r |= m[s[0][0]] & m[s[1][0]]&m[s[2][0]]&m[s[3][0]];
		r |= m[s[0][1]] & m[s[1][1]]&m[s[2][1]]&m[s[3][1]];
		r |= m[s[0][2]] & m[s[1][2]]&m[s[2][2]]&m[s[3][2]];
		r |= m[s[0][3]] & m[s[1][3]]&m[s[2][3]]&m[s[3][3]];
		
		r |= m[s[0][0]] & m[s[1][1]]&m[s[2][2]]&m[s[3][3]];
		r |= m[s[0][3]] & m[s[1][2]]&m[s[2][1]]&m[s[3][0]];
		
		printf("Case #%d: ", caso++);
		if(r==1)printf("O won\n");
		else if(r==2)printf("X won\n");
		else {
			for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)if(s[i][j]=='.'){
				printf("Game has not completed\n");
				goto sai;
			}
			printf("Draw\n");
		}
		
		
		
		sai:;
		
		
	}
	
	return 0;
}
