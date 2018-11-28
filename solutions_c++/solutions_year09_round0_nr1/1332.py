#include<iostream>
#include<cstdio>
#include<string.h>
#include<set>
using namespace std;
char S[5002][20] , C[700] ;
bool used[15][26];

int main(){
	freopen("A-large.in","r", stdin);
	freopen("A-large.out","w", stdout);
	int L , D , N  , i , j ; 
	cin >> L >> D >> N ;
	gets(S[0]);
	for(i=0;i< D; i++){
		gets(S[i]);
	}
	for( i=0 ;i < N; i++){
		gets(C); 
		bool gam = false; 
		int n = strlen(C);
		
		for( j=0;j < L ;j++) 
			for( int k=0 ; k < 26; k++) used[j][k] = false; 
        int ind = 0;
		for( j= 0; j < n; j++){
			if( C[j] == '(' ) gam = true ; 
			else if ( C[j] == ')' ) { gam = false; ind++; }
			else {
				used[ind][ C[j]-'a' ] = true;
				if ( !gam ) ind++ ;  
			}
		}
		int res = 0;
		for( j=0;j < D ; j++){
			int mis = 1;
			for( int k=0 ;k < L; k++) 
				if( !used[ k ] [  S[j][k]-'a' ]){ mis = 0;  break;}
			res+= mis ; 
		}
		cout << "Case #" << i+1 << ": " <<    res << "\n" ;

	}
	return 0;
}