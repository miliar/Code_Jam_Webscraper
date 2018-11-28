#include <stdio.h>
#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <memory.h>
#include <map>
#include <vector>
#include <set>
using namespace std;
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define repk(i,a,b) rep(i,a,(b)-1)
#define rrep(i,a,b) for(int i=(b);i>=(a);i--)
#define rrepk(i,a,b) rrep(i,a,(b)-1)
#define fe(e,x) for(edge *e = (x)->first;e;e = e->next)
#define foreach(tank_type,iterator_name,set_name) \
	for(tank_type::iterator iterator_name = (set_name).begin();iterator_name != (set_name).end();iterator_name++)
#define comp_def(cmp_name,type) bool cmp_name(type l,type r)
#define ifn(x) if(!(x))
#define vind(p_point) (p_point-points)
#define eind(p_edge) (p_edge-edges)
#define eopp(p_edge) (edges+(eind(p_edge)^1))
#define mp(x,y) make_pair((x),(y))
#define OIFILE(filename) freopen(filename##".in","r",stdin);freopen(filename##".out","w",stdout)
#define OICLOSE fclose(stdin);fclose(stdout)
typedef long long ll;
const int inf = 0x3fffffff,upinf = 0x7fffffff,geps = 10;
const double eps = 1e-12,dinf = 1e20;

char gamemap[5][5];
void Init(){
	repk(i,0,5) gets(gamemap[i]);
}

bool checkrow(int r,char player){
	repk(j,0,4) ifn(gamemap[r][j] == player || gamemap[r][j] == 'T') return false;
	return true;
}
bool checkcol(int c,char player){
	repk(i,0,4) ifn(gamemap[i][c] == player || gamemap[i][c] == 'T') return false;
	return true;
}
bool check_first(char player){
	repk(i,0,4) ifn(gamemap[i][i] == player || gamemap[i][i] == 'T') return false;
	return true;
}
bool check_second(char player){
	repk(i,0,4) ifn(gamemap[i][3-i] == player || gamemap[i][3-i] == 'T') return false;
	return true;
}
bool check(char player){
	repk(i,0,4) if(checkrow(i,player) || checkcol(i,player)) return true;
	if(check_first(player) || check_second(player)) return true;
	return false;
}
bool find_empty(){
	repk(i,0,4) repk(j,0,4) if(gamemap[i][j] == '.') return true;
	return false;
}
void solve(int case_ind){
	printf("Case #%d: ",case_ind);
	if(check('O')) printf("O won",case_ind);
	else if(check('X')) printf("X won");
	else if(find_empty()) printf("Game has not completed");
	else printf("Draw");
	printf("\n");
}

int main(){
#ifndef ONLINE_JUDGE
	OIFILE("A");
#endif

	char buff[255];gets(buff);
	int t;sscanf(buff,"%d",&t);
	rep(i,1,t){
		Init();
		solve(i);
	}

#ifndef ONLINE_JUDGE
	OICLOSE;
#endif
	return 0;
}
