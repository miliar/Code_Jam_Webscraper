/*
 * b.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: Sara Tarek
 */

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <utility>
#include <vector>

using namespace std;

int main()
{

	int T;
	int N;
	int S;
	int P;

	freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );


	cin>>T;
	int Case = 1;
	while(T > 0)
	{
		cin>>N>>S>>P;

		int NSC = P + (P - 1) + (P - 1);
		int SC = P + (P - 2) + (P - 2);

		int count = 0;
		int gog;
		for(int i = 0; i < N; i++)
		{
			cin>>gog;
			if(gog < P) continue;
			if(gog >= NSC)
				count++;
			else if (gog >= SC && S > 0){
				count++;
				S--;
			}
		}
		cout<<"Case #"<<Case<<": "<<count<<endl;
		T--;
		Case++;
	}
	return 0;
}	
	













