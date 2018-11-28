#define CO(x) std::cout << #x" = " << x << std::endl
#define fori(i,start,sharpEnd) for(int i = start; i < sharpEnd; i++)
#define fora(i,start,End) for(int i = start; i >= End; i--)
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <climits>
#include <map>
#include <vector>
#include <cassert>
#include <limits>
#include <iomanip>


using namespace std;


#define mm(type,value) memset(type,value,sizeof(type))
#define mat(matrix,h,w) fori(i,0,h){fori(j,0,w)std::cout<<matrix[i][j]<<" ";std::cout<<std::endl;}
#define sw(matrix,h,w,value) fori(i,0,h)fori(j,0,w)matrix[i][j]=value
#define mt(matrix,s) fori(i,0,s)std::cout<<matrix[i]<<" ";std::cout<<std::endl;
#define EPS 10e-8




int p[4][4];


bool xw(int x){
	fori(i,0,4){
		int t = 0;
		int xs = 0;
		fori(j,0,4){
			if(p[i][j] == x)
				xs++;
			else if(p[i][j] == 'T')
				t++;
			}
		if((xs == 3 && t == 1)|| xs == 4)
			return true;
	
	}	
	fori(i,0,4){
		int t = 0;
		int xs = 0;
		fori(j,0,4){
			if(p[j][i] == x)
				xs++;
			else if(p[j][i] == 'T')
				t++;
			}
		if((xs == 3 && t == 1)|| xs == 4)
			return true;
	}
	
		int t = 0;
		int xs = 0;
	fori(i,0,4){
		if(p[i][i] == x)
			xs++;
		else if(p[i][i] == 'T')
			t++;
		if((xs == 3 && t == 1)|| xs == 4)
			return true;
	}
	t = xs = 0;
	fora(i,3,0){
		if(p[3-i][i] == x)
			xs++;
		else if(p[3-i][i] == 'T')
			t++;
		if((xs == 3 && t == 1)|| xs == 4)
			return true;
	}
	
	
		return false;
}

int main()
 {
	//freopen("t.in","r",stdin);
  	//freopen("t.out","w",stdout);
	int ts;
	cin >> ts;
	int cs = 1;
	string l;
	getchar();
	while(ts--){
		bool noty = false;
		fori(i,0,4){
			getline(cin,l);
			fori(j,0,4){
				p[i][j] = (int)l[j];
				if(p[i][j] == '.')
					noty = true;
			}
		}
		
		cout << "Case #"<<cs++<<": ";
		bool x = xw('X');
		bool o = xw('O');
		if(!x && !o && !noty){
			cout << "Draw" << endl;
		}	
		else if(x){
			cout << "X won" << endl;
		}
		else if(o){
			cout << "O won" << endl;
			
		}else
			cout << "Game has not completed" << endl;	
		getline(cin,l);
	}






 //system("PAUSE");
 return 0;
 }




