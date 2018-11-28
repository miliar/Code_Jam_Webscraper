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

char results[100][100];
float WP[100][101];
float OWP[100];
float OOWP[100];
float RPI[100];

int main(){
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
   
   int ncasos,teams;
   char result;
   int matches;
   
   cin >> ncasos;
   for(int r=0;r<ncasos;r++){		
		cout << "Case #" << r+1 << ": " << endl;
		cerr << "Case #" << r+1 << ": " << endl;;

		cin >> teams;
      
		for(int i=0;i<teams;i++){
			for(int j=0;j<teams;j++){
				cin >> result;
				results[i][j] = result;
			}	
		}
			
      float wins;
		float loses;
		for(int i=0;i<teams;i++){
			wins = 0;
			loses = 0;
			for(int j=0;j<teams;j++){
				if(results[i][j] == '1'){ wins ++;}
				if(results[i][j] == '0'){ loses ++; }	
			}
			WP[i][100] = wins / (wins + loses);
			for(int j=0;j<teams;j++){
				if(results[i][j] == '1'){ WP[i][j] = (wins-1) / (wins+loses-1); }
				if(results[i][j] == '0'){ WP[i][j] = (wins) / (wins+loses-1); }	
			}		
		}
		
		for(int i=0;i<teams;i++){
			OWP[i] = 0;
			matches = 0;
			for(int j=0;j<teams;j++){
				if((i!=j) && (results[i][j] == '1' || results[i][j] == '0')){ OWP[i] += WP[j][i];matches++;}	
			}
			OWP[i] *= (1.0/matches);
		}
      for(int i=0;i<teams;i++){
			OOWP[i] = 0;
			matches = 0;
			for(int j=0;j<teams;j++){
				if((i!=j) && (results[i][j] == '1' || results[i][j] == '0')){ OOWP[i] += OWP[j];matches++;}	
			}
			OOWP[i] *= (1.0/matches);
			RPI[i] = 0.25 * WP[i][100] +  0.5*OWP[i] + 0.25*OOWP[i];
			
			//cout << RPI[i] << endl;
			printf("%.8lf\n", RPI[i]);
			cerr << RPI[i] << endl;
		}
		               
	}
}

