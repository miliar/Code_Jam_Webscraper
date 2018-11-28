#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>

#define FOR(i,n) for(int i=0; i<(n); i++)
#define REP(i,n) for(int i=1; i<=(n); i++)
#define FORI(it,n) for(typeof((n).begin()) it=(n).begin(); it!=(n).end(); it++)
#define ALL(n) (n).begin(), (n).end()
#define psh push_back
#define mkp make_pair
#define frs first
#define sec second
using namespace std;
typedef pair<int,int> PII;
typedef long long LL;
typedef long double LD;
const int INF=1<<29;
const int xam=300;

vector<char> opp[xam];
char con[xam][xam];
vector<char> list;
int ile[xam];

void clear()
{
    for(int i='A'; i<='Z'; i++) opp[i].clear();
    for(int i='A'; i<='Z'; i++) ile[i]=0;
    for(int i='A'; i<='Z'; i++) for(int j='A'; j<='Z'; j++) con[i][j]=0;
    list.clear();
}
bool opposition(char c)
{
    FORI(it,opp[c]) {
	if(ile[*it]) return 1;
    }
    return 0;
}
bool connection(char c)
{
    if(con[c][list.back()]==0) return 0;
    ile[list.back()]--;
    c=con[c][list.back()];
    list.pop_back();
    list.psh(c);
    ile[c]++;
    return 1;
}
void play()
{
    int n;
    char ch;
    scanf("%d", &n);
    while(n--) {
	scanf(" %c", &ch);
	if(!list.size()) {list.psh(ch); ile[ch]++; continue;}
	if(connection(ch)) continue;
	if(opposition(ch)) {
	    list.clear();
	    for(int i='A'; i<='Z'; i++) ile[i]=0;
	    continue;
	}
	list.psh(ch);
	ile[ch]++;
    }
}
void read()
{
    int c,d,n;
    char a1,a2,a3;
    scanf("%d", &c);
    while(c-->0) {
	scanf(" %c%c%c", &a1,&a2,&a3);
	con[a1][a2]=a3;
	con[a2][a1]=a3;
    }
    scanf("%d", &d);
    while(d-->0) {
	scanf(" %c%c", &a1,&a2);
	opp[a1].psh(a2);
	opp[a2].psh(a1);
    }
}

int main()
{
    int t;
    scanf("%d", &t);
    REP(i,t) {
	printf("Case #%d: ", i);
	read();
	play();
// 	FORI(it,list) printf("%c", *it); printf("\n");
	if(!list.size()) printf("[]\n");
	else {
	    printf("["); printf("%c", list[0]);
	    for(int j=1; j<list.size(); j++) printf(", %c", list[j]);
	    printf("]\n");
	}
	clear();
    }
    

    return 0;
}
