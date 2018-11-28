/*
 * Round1C_A.cpp
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

int main( )
{
	int tt, R, C;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	cin >> tt;
	for(int t=0; t<tt;t++){
		int flag = 0;
		cin >> R;
		cin >> C;
		string ans[R+1];
		for(int i=0; i<R; i++) cin >> ans[i];
		cout << "Case #" << t+1 << ":" << endl;

		for(int i=0; i<R-1; i++){
			for(int j=0; j<C-1; j++){
				if(ans[i][j]=='#'){
					if(ans[i][j+1]!='#'||ans[i+1][j]!='#'||ans[i+1][j+1]!='#'){
						flag = 1;
						break;
					}
					ans[i][j] = '/';
					ans[i][j+1] = '-';
					ans[i+1][j] = '-';
					ans[i+1][j+1] = '/';
				}
			}
		}

		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				if(ans[i][j]=='#') flag = 1;
			}
		}

		if(flag == 1) cout << "Impossible" << endl;
		else
			for(int i=0; i<R; i++) cout << ans[i] << endl;


	}

	return 0;
}
