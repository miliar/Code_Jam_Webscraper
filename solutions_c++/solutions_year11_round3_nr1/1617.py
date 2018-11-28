#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std; 

char tablero[50][50];

int main(){
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
  
   int ncasos;
   int R,C;
   char aux;
   int blues;
   bool ok;
   int reds;
   
   cin >> ncasos;
   for(int r=0;r<ncasos;r++){		
		cout << "Case #" << r+1 << ": " << endl;
		cerr << "Case #" << r+1 << ": " << endl;
		
		blues = 0;
		reds = 0;
		ok = true;
		cin >> R >> C;
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				cin >> aux;
				tablero[i][j] = aux;
				if(aux == '#') blues++;
			}
		}
		
		if(blues%2!=0) ok = false;
		else{
			for(int i=R-1;i>0;i--){
				for(int j=C-1;j>0;j--){
					if(tablero[i][j] == '#'	 && tablero[i-1][j]=='#' && tablero[i][j-1]=='#' && tablero[i-1][j-1]=='#'){
						tablero[i][j] = '/';
						tablero[i-1][j-1] = '/';
						tablero[i-1][j] = '\\';
						tablero[i][j-1] = '\\';
						reds += 4;	
					}
				}
			}
		}
			
		if(!ok || reds != blues){
		  	cout << "Impossible" << endl;
			cerr << "Impossible" << endl;
		}else{
			for(int i=0;i<R;i++){
				for(int j=0;j<C;j++){
					cout << tablero[i][j];
					cerr << tablero[i][j];
				}
				cout << endl;
				cerr << endl;
			}	
		}
	
		               
	}
}

