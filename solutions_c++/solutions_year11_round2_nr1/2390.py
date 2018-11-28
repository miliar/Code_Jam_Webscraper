#include <iostream>
#include <algorithm>    
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  

using namespace std;


int T,N;
int gcd(int a, int b)
{
    return b ? gcd(b, a % b) : a;
}

int factorial(int n) {
	
	if(n <= 1) return 1;
	return (n * factorial(n - 1));
}

int main () {
	int S[10][10]={-1};
	double RPI[10]={0};
	double WP[10]={0};
	double OWP[10]={0};
	double OOWP[10]={0};
	double wins[10] = {0};
	double played[10] = {0};
	double noopp[10] = {0};
	double oppwins[10][10] = {0};
	double oppplayed[10][10] = {0};
	string str;
    //freopen("input.in.txt", "r", stdin);
    //freopen("output.out.txt", "w", stdout);
	cin>>T;
    for (int i=1; i<=T; i++) {
		for (int k=0; k<N; k++) {
			WP[k] = 0;
			OWP[k] = 0;
			OOWP[k] = 0;
			RPI[k] = 0;
			wins[k] = 0;			
			played[k] = 0;
			noopp[k] = 0;
			for (int l=0; l<N; l++) {
				oppwins[k][l] = 0;
				oppplayed[k][l] = 0;
			}
			
		}
		cin>>N;
		for (int k=0; k<N; k++) {
			cin>>str;
			for (int l=0; l<N; l++) {
				
				if(str[l] == '.')
					S[k][l] = -1;
				else {
					S[k][l] = str[l] - '0';
					played[k]++;
					if(S[k][l] == 1)
						wins[k]++;
				}	
				//cout<<" " + S[k][l] <<" ";
				
			}	
			WP[k] = wins[k]/played[k];
			//cout<<"\nWins for "<<(k+1) <<": " <<wins[k]<<" ";
			//cout<<"Out of "<<played[k]<<" WP: "<<WP[k]<<"\n";
			
		}
		for (int k=0; k<N; k++) {
			
			for (int l=0; l<N; l++) {
				oppwins[k][l] = wins[l];
				oppplayed[k][l] = played[l];
				if (S[k][l]!=-1) {
					if(S[k][l]==0)
						oppwins[k][l]--;
					oppplayed[k][l]--;
				}
				//cout << "Opponents of "<<k+1;
				//cout<<"\nWins for "<<(l+1) <<": " <<oppwins[k][l]<<" ";
				//cout<<"Out of "<<oppplayed[k][l]<<" WP: "<<WP[k]<<"\n";
				if(S[k][l]!=-1)
				 OWP[k] = OWP[k] + (oppwins[k][l]/oppplayed[k][l]); 				
			}	
			OWP[k] = OWP[k]/played[k];
		}	
		for (int k=0; k<N; k++) {
			for (int l=0; l<N; l++) {
				if(S[k][l]!=-1) 
					OOWP[k] += OWP[l];
			}
				OOWP[k] = OOWP[k]/played[k];
		}
		cout<< "\nCase #" << i << ":\n";
		for (int j=0; j<N; ++j) {			
			RPI[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
			//cout<< WP[j] <<"\n";
			//cout<< OWP[j] <<"\n";
			cout<< RPI[j] << endl;
		}
	}
    
    return 0;
}
