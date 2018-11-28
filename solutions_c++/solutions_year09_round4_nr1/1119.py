/*
 *  A.cpp
 *
 *  Created by Josh Deprez on 27/09/09.
 *
 * This code was probably compiled using llvm-g++. The LLVM compiler infrastructure is freely 
 * available at http://llvm.org/
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
#define MAX_T 60

int main()
{
	
	int T;
	cin >> T;

	for (int t=0; t<T; ++t) {

		
		int N;
		cin >> N;
		vector<int> m(N);
		string x;
		for (int i=0; i<N; ++i) 
		{
			cin >> x;
			for (int j=0; j<N; ++j)
			{
				if (x[j] == '1') m[i] = j;
			}
		}
		
		/*for (int i=0; i<N; ++i)
		{
			cout << m[i] << endl;
		}
		*/
		int swp=0;
		for (int i=0; i<N; ++i)
		{
			if (m[i] > i)
			{
				for (int j=i+1; j<N; ++j)
				{
					if (m[j] <= i)
					{
						for (int k=j; k>i; --k)
						{
							swap(m[k], m[k-1]);
							swp++;
						}
						break;
					}
				}
			}
		}
		

		cout << "Case #" << (t+1) << ": " << swp << endl;
	}
	 
	return 0;
}

