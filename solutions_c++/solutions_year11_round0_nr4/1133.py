/*
ID: ebappa11
PROG: solder
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>



#define MAXN 1005
using namespace std;

int main() {
	ofstream out ("D.out");
	ifstream in ("D.in");

	int ts, N, ans, a[MAXN], pos[MAXN];
	in >> ts;

	for (unsigned int t = 0; t < ts; t += 1)
	{
		ans = 0;
		in >> N;

		for (unsigned int i = 0; i < N; i += 1)
		{
			in >> a[i];
			--a[i];
		}

		for (unsigned int i = 0; i < N; i += 1)
		{
			if(i != a[i])
			{
				ans+=1;
			}
		}
		out << "Case #" << t+1 << ": " << ans << ".000000\n";
	}


	
	
	return 0;
}








