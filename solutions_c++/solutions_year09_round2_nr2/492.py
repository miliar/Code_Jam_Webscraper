#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int main()
{
	string p,q;
	int T;
	cin >> T;
	for(int i = 1; i<= T; i++)
	{
		cin >> p;
		q = p;
		next_permutation(p.begin(),p.end());
		if(q>=p) 
		{
			p = "0" + p;
			int t = 0; 
			while(p[t] == '0') t++;
			swap(p[0],p[t]);
		}
		printf("Case #%d: %s\n",i,p.c_str());
	}
}