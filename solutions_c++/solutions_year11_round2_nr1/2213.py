// jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "windows.h"
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{

	unsigned int T = 0;
	cin >> T;
	//Sleep(9000);
	for (int i = 0; i < T; ++i) {
		unsigned int N = 0;
		cin >> N;

		unsigned int wl[100][100];
		float wp[100];
		float owp[100][100];

		for (int j =0; j < N; ++j) {
			unsigned int won = 0;
			unsigned int lost = 0;
			for (int k = 0; k < N; ++k) {
				char ch;
				cin >> ch;
				if (ch == '.') {
					wl [j][k] = 2;
				}
				else if (ch == '0') {
					wl[j][k] = 0;
					lost++;
				}
				else {
					wl[j][k] = 1;
					won++;
				}
			}
			wp[j] = ((float)won)/((float)(won+lost));
			for (int k = 0; k < N; ++k) {
				if (k == j) {
					owp[j][k] = 0;
					continue;
				}
				if (wl[j][k]== 0)
					owp[j][k] = ((float)won)/((float)(won+lost-1));
				else if (wl[j][k] == 1)
					owp[j][k] = ((float)won-1)/((float)(won+lost-1));
				else
					owp[j][k] = 0;
			}
		}
		cout << "Case #" << i+1 << ": " << endl;
		
		float master[100];
		for (int j = 0; j < N; ++j) {
			int count  = 0;
			float oowpv =0;
			for (int k=0; k < N; ++k) {
				if(wl[k][j] != 2) {
					oowpv += owp[k][j];
					++count;
				}
			}
			master[j] = oowpv/count;
		}

		for (int j = 0; j < N; ++j) {
			float rpi = 0.25* wp[j];
			rpi += 0.50 * master[j];
			
			float final = 0;
			int count  = 0;
			for (int k = 0; k < N; ++k) {
				if ( k == j)
					continue;
				if (wl[k][j]== 2)
					continue;
				final += master[k];
				++count;
			}
			rpi += 0.25*final/count;
			std::cout << rpi << endl;

		}
	
	}
	return 0;
}

