#include <iostream>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <map>
#include <list>
#include <cstdio>
#include <cctype>
#include <sstream>
#include <fstream>

using namespace std;

#define ll long long
#define ms1(m) memset((m),-1,sizeof((m)))
#define ms0(m) memset((m),0,sizeof((m)))
#define SORT(v) sort((v).begin(),(v).end())
#define CINFASTER cin.sync_with_stdio(false)
#define sz size()
#define pb(x) push_back(x)
#define mp(a,b) make_pair((a),(b))
#define all(x) (x).begin(),(x).end()


int main (){
	CINFASTER ;
	ifstream fin("A-large.in") ;
	ofstream fout("output.txt") ;

	int tc; fin>>tc ;
	for(int t=0;t<tc;++t){
		vector<string> v(4, "xxxx") ;
		for(int i=0;i<4;++i) fin>>v[i] ;
		//for(int i=0;i<4;++i){
		//	cout<<v[i]<<endl;
		//}cout<<endl;
		//string dummy ; fin>>dummy;
		int whoWins=0 ; //0:end 1:O 2:X 

		for(int i=0;i<4;++i){
			int co=0,ro=0,cx=0,rx=0 ;
			for(int j=0;j<4;++j){
				if(v[i][j] == '.') whoWins = -1 ;
				if(v[i][j] == 'O' || v[i][j] == 'T') ro ++ ;
				if(v[i][j] == 'X' || v[i][j] == 'T') rx ++ ;
				if(v[j][i] == 'O' || v[j][i] == 'T') co ++ ;
				if(v[j][i] == 'X' || v[j][i] == 'T') cx ++ ;
			}
			if(co==4 || ro == 4){
				whoWins = 1 ;break ;
			}
			if(rx==4 || cx == 4){
				whoWins = 2 ;break ;
			}
		}


		int do1 = 0, do2 = 0, dx1 = 0, dx2 = 0;
		for(int i=0;i<4;++i){
			if(v[i][i] == 'O' || v[i][i] == 'T') do1 ++ ;
			if(v[i][3-i] == 'O' || v[i][3-i] == 'T') do2++ ;
			if(v[i][i] == 'X' || v[i][i] == 'T') dx1 ++ ;
			if(v[i][3-i] == 'X' || v[i][3-i] == 'T') dx2++ ;
		}
		if(do1 == 4 || do2 == 4) whoWins = 1 ;
		else if(dx1 == 4 || dx2 == 4) whoWins = 2 ;


		if(whoWins == 1){
			fout<<"Case #"<<t+1<<": O won"<<endl ;
		}
		else if(whoWins == 2){
			fout<<"Case #"<<t+1<<": X won"<<endl ;
		}
		else if(whoWins == 0){
			fout<<"Case #"<<t+1<<": Draw"<<endl ;
		}
		else{
			fout<<"Case #"<<t+1<<": Game has not completed"<<endl ;
		}

	}

	fin.close() ;
	fout.close() ;
	return 0;
}