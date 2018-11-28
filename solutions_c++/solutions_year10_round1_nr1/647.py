/*
 *  A.cpp
 *
 *  Created by Josh Deprez on 22/05/10.
 *
 */

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
typedef long long ll;
typedef unsigned int uint;
using namespace std;
#define MAX_T 100

void rotatot(vector<string>& B)
{
	uint N = B.size();
	vector<string> temp(N, string(N,'.'));
	
	for (int i=0; i<N; ++i)
		for (int j=0; j<N; ++j)
			temp[i][j] = B[N-j-1][i];
	
	for (int i=0; i<N; ++i)
		B[i] = temp[i];
}

void grav(vector<string>& B)
{
	uint N = B.size();

	for (int i=N-1; i>=0; --i)
	{
		for (int j=0; j<N; ++j)
		{
			if (B[i][j] == '.')
			{
				for (int k=i-1; k>=0; --k)
				{
					if (B[k][j] != '.')
					{
						B[i][j] = B[k][j];
						B[k][j] = '.';
						break;
					}
				}
			}
		}
	}
}



int main()
{
	int T;
	cin >> T;
	
	for (int t=0; t<T; ++t) {
		
		int K, N;
		cin >> N >> K;
		
		vector<string> B(N);
		for (int n=0; n<N; ++n)
		{
			cin >> B[n];
		}
		
		rotatot(B);
		grav(B);
		
		/*for (int n=0; n<N; ++n)
		{
			cout << B[n] << endl;
		}*/
		
		int winners = 0;
		static const int red=1, blue=2;
		
		for (int i=0; i<N; ++i)
		{
			for (int j=0; j<N; ++j)
			{
				int w=0;
				switch (B[i][j])
				{
					case 'B': w = blue; break;
					case 'R': w = red; break;
					default:break;
				}
				
				if (w>0 && (winners & w) != w)
				{
					int k;
					for (k=1; k<K && i+k<N && B[i+k][j]==B[i][j]; ++k);
					if (k==K) winners |= w;

					for (k=1; k<K && j+k<N && B[i][j+k]==B[i][j]; ++k);
					if (k==K) winners |= w;

					for (k=1; k<K && i+k<N && j+k<N && B[i+k][j+k]==B[i][j]; ++k);
					if (k==K) winners |= w;
				
					for (k=1; k<K && i+k<N && j-k>=0 && B[i+k][j-k]==B[i][j]; ++k);
					if (k==K) winners |= w;
					
				}		
			}
		}
			
		
		cout << "Case #" << (t+1) << ": ";
		switch (winners)
		{
			case 0: cout << "Neither"; break;
			case red: cout << "Red"; break;
			case blue: cout << "Blue"; break;
			case red|blue: cout << "Both"; break;
		}
		
		cout << endl;
	}
	
	return 0;
}

