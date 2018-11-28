#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{


	int T;
	long long L,P,C;
	cin >> T;
	for(int counter=0; counter<T; counter++)
	{
		cin >> L >> P >> C;
		
		long long tot=0;
		long long lower = L;
		long long higher = P;
		
		while(higher > lower*C)
		{
			tot++;
			higher = ceil((double)higher/(double)C);
		}
		if(higher == lower*C && tot!=0)
			tot+=2;
		else if(tot!=0) {
			tot+=2;
		}
		
		if(tot!=0)
			tot-=2;
		if(tot!=0)
			tot =1+ log(tot)/log(2);
		
		
		cout << "Case #" << counter+1 << ": " << tot<< endl;
		
		
	}
}