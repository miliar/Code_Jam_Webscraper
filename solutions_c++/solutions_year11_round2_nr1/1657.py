#include <iostream>
#include <string>
#include <cctype>
#include <cstdio>
#include <cstring>

using namespace std;

string b[101];

double WP[101];
double OWP[101];
double OOWP[101];

int main(){
	int T, N;
	
	cin >> T;
	for (int t=1; t<=T; t++){
		cout << "Case #" << t << ":" << endl;
		cin >>N;
		cin.ignore();
		for (int i=0; i<N; i++)
			getline( cin, b[i] );
		
		//WP
		for (int i=0; i<N; i++){
			WP[i] = 0;
			int C = 0;
			int W = 0;
			for (int j=0; j<N; j++)
				if ( isdigit( b[i][j] ) ){
					C++;
					if ( b[i][j] == '1' ) W++;
				}
			if (C) WP[i] = (double)W / (double)C;
		}
		
		//OWP
		for (int i=0; i<N; i++){
			int C = 0;
			OWP[i] = 0.0;
			for (int j=0; j<N; j++)
				if ( isdigit( b[i][j] ) ){
					C++;
					int CC = 0;
					int WW = 0;
					for (int k=0; k<N; k++)
						if ( k!=i && isdigit( b[j][k] ) ){
							CC++;
							if ( b[j][k] == '1' ) WW++;
						}
							
					OWP[i] += (double)WW/(double)CC;
				}
			if (C) OWP[i] /= (double)(C);
		}
		
		//OOWP
		for (int i=0; i<N; i++){
			int C = 0;
			OOWP[i] = 0;
			for (int j=0; j<N; j++){
				if ( isdigit( b[i][j] ) ){
					C++;
					OOWP[i] += OWP[j];
				}
			}
			if ( C ) OOWP[i] /= (double)(C);
		}
		
		for (int i=0; i<N; i++){
			char c[100];
			//printf("%lf %lf %lf\n",WP[i],OWP[i],OOWP[i]);
			sprintf(c,"%.12f",0.25*WP[i]+0.50*OWP[i]+0.25*OOWP[i]);
			for (int i=strlen(c)-1; i>0 && c[i-1]!='.'; i--)
				if ( c[i]=='0' ) c[i] = 0;
				else break;
			cout << string(c) << endl;
		}
	}
	
	return 0;
}
