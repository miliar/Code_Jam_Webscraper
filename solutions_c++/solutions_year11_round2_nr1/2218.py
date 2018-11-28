#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int map[101][101];
double played[101];
double RPI[101];
double wp[101], owp[101], oowp[101];


bool match(int i, int x, int n) {
	
	for(int j = 0; j < n; j++) {
	
		if(map[i][j] != -1 && j == x)
			return 1;
	
	}
	
	return 0;

}

void find_wp(int n) {

	double w,p;
	for(int i = 0; i < n; i++) {
			w = 0;
			p = 0;
			
			for(int j = 0; j < n; j++) {
				
				if(map[i][j] == 1) w++;
				if(map[i][j] > -1) p++;
				
			
			}
			played[i] = p;
			wp[i] = w/p;
			
		}

}

double find_owp(int n, int x) {

		double w,p,mwp[101]; // won, played
		double sum;
		
		//cout << "owp:\n";
		
		for(int i = 0; i < n; i++) {
			
			if(i == x) continue;
		
			w = 0;
			p = 0;
		
			for(int j = 0; j < n; j++) {
				if(j == x) continue;
				
				if(map[i][j] == 1) w++;
				if(map[i][j] > -1) p++;
				
			
			}
			
			mwp[i] = w/p;
		
			//cout << char(i+65) << ") WP = " << wp << endl;
		}
		
		sum = 0;
		for(int i = 0; i < n; i++) {
			if(match(i,x,n)) {
			//cout << "+ " << wp[i] << endl;
			sum += mwp[i];
			}
		}
		owp[x] = sum/played[x];
		
		//cout << "Final owp for " << char(x+65) << " = " << sum/(n-1) << endl; 
		//cout << played[x] << endl;
		return owp[x];

}

double find_oowp(int n, int x) {
		
		double sum;
		
		sum = 0;
		
		for(int i = 0; i < n; i++) {
			if(match(i,x,n)) {
		
				sum += owp[i];
				
			}
		}
		
		oowp[x] = sum/played[x];
		//cout << "Final owp for " << char(x+65) << " = " << sum/(n-1) << endl; 
		//cout << played[x] << endl;
		return oowp[x];

}


int main() {
	
	int T,N;
	
	char tmp;
	
	
	
	
	
	cin >> T;
	
	for(int c = 1; c <= T; c++) {
	
		cin >> N;
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				
				scanf("%c", &tmp);
				if(tmp == 10)	scanf("%c", &tmp);
				if(tmp == '.')
					map[i][j] = -1;
				else
					map[i][j] = tmp-48;
					

			}
		}
		
	
		find_wp(N);
		for(int i = 0; i < N; i++) {
			find_owp(N,i);
		}
		
		for(int i = 0; i < N; i++) {
			find_oowp(N,i);
		}
		
		for(int i = 0; i < N; i++) {
			RPI[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
		}
		
		/*
		for(int i = 0; i < N; i++) {
			
			cout << char(i+65) << ") WP = " << wp[i] << endl;
			cout << char(i+65) << ") OWP = " << owp[i] << endl;
			cout << char(i+65) << ") OOWP = " << oowp[i] << endl;
			cout << char(i+65) << ") RPI = " << RPI[i] << endl;
			cout << endl;
			
		}*/
		
		
		printf("Case #%d:\n", c);
		for(int i = 0; i < N; i++) {
			cout << setprecision (12) << RPI[i] << endl;
			//printf("%0.12f\n", RPI[i]);
		}
		
	}



return 0;
}
