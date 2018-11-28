/*
 * Round1B_A.cpp
 *
 *  Created on: 2011/05/22
 *      Author: masamichi1222
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip.h>
using namespace std;

double ave(string m)
{
	int j=0;
	int sum=0;
	for(int i=0; i<(int)m.size(); i++){
		if(m[i]=='1'){
			sum++;
			j++;
		}
		if(m[i]=='0') j++;
	}
	return (double)sum/j;
}

int main( )
{
	int tt, N;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	cin >> tt;
	for(int t=0; t<tt;t++){
		cin >> N;
		string m[N];
		for(int i=0; i<N; i++) cin >> m[i];

		cout << "Case #" << t+1 << ":" << endl;

		double WP[N], OWP[N], OOWP[N], RPI;

		int count;
		for(int i=0; i<N; i++){
			count=0;
			int sum=0;
			for(int j=0; j<N; j++){
				if(m[i][j]=='1'){
					sum++;
					count++;
				}
				if(m[i][j]=='0') count++;
			}
			WP[i] = (double)sum/count;
		}


		for(int i=0; i<N; i++){
			int count2=0;
			for(int j=0; j<N; j++){
				if(m[i][j]!='.'){
					int sum=0;
					int count=0;
					for(int k=0; k<N; k++){
						if(m[j][k]=='1'&&k!=i){
						sum++;
						count++;
						}
						else if(m[j][k]=='0'&&k!=i){
						count++;
						}
					}
					OWP[i] += (double)sum/count;
					count2++;
				}
			}
			OWP[i] = (double)OWP[i]/count2;
		}

		for(int i=0; i<N; i++){
			int count=0;
			OOWP[i]=0;
			for(int j=0; j<N; j++){
				if(m[i][j]!='.'){
					OOWP[i] += OWP[j];
					count++;
				}
			}
			OOWP[i] = (double)OOWP[i]/count;
		}

		for(int i=0; i<N; i++){
			RPI = 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i];
			cout << setprecision(16) << RPI << endl;
		}

	}

	return 0;
}
