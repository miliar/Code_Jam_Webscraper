#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <deque>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPA(i,a,n) for(int i=(a);i<((a)+(n));i++)
#define INITW(var,value,width) for(int whslkfje=0;whslkfje<(width);whslkfje++) var[whslkfje]=(value)
#define INITHW(var,value,height,width) for(int hwesaft=0;hwesaft<(height);hwesaft++) \
		 for(int whslkfje=0;whslkfje<(width);whslkfje++) var[hwesaft][whslkfje]=(value)

typedef long long lint;
using namespace std;
void solve();
void init();

int main(){
	init();

	int T;
	cin>>T;
	string str;
	getline(cin, str);
	
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		solve();
		cout<<"\n";
	}
}

void init(){
	
}

char field[4][4];
bool draw(){
	REP(i,4)REP(j,4){
		if(field[i][j]=='.')return false;
	}
	return true;
}

bool hits(char who,char a,char b,char c,char d){
	if((who!=a)&&('T'!=a))return false;
	if((who!=b)&&('T'!=b))return false;
	if((who!=c)&&('T'!=c))return false;
	if((who!=d)&&('T'!=d))return false;
	return true;
}

bool wins(char who){
	if(hits(who,field[0][0],field[1][1],field[2][2],field[3][3]))return true;
	if(hits(who,field[0][3],field[1][2],field[2][1],field[3][0]))return true;
	REP(i,4)if(hits(who,field[i][0],field[i][1],field[i][2],field[i][3]))return true;
	REP(i,4)if(hits(who,field[0][i],field[1][i],field[2][i],field[3][i]))return true;
	return false;
}
		
void solve(){
	REP(i,4)REP(j,4){
		cin>>field[i][j];
	}
	if(wins('X')){
		cout<<"X won";
		return;
	}
	if(wins('O')){
		cout<<"O won";
		return;
	}
	if(draw()){
		cout<<"Draw";
		return;
	}
	cout<<"Game has not completed";
}
