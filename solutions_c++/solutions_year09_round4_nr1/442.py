#include <iostream>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath> 

#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x)) 


using namespace std;
int main()
{
	int N;
	ifstream inp("e:\\A-large.in");
	ofstream out("e:\\output.txt");
	inp>> N;
	int i,j;
	for (int nn = 1; nn <= N; nn++)
	{
		int p,i, j;
		inp>> p;
		string s;
		int last[100];
		for (  i = 0; i < p; i++)
		{
			inp >> s;
			last[i] = p - 1;
			while ( last[i] >= 0 && s[last[i]] =='0' ) last[i]--;
			//cout<<last[i]<<endl;
			
		}
		cout<<endl;
		int sum = 0;
		for ( i = 0; i < p; i++)
		{
		//	for ( j = 0; j < p; j++)
		//	cout<<last[j]<<" ";
		//	cout<<endl;
			for ( j = 0; j < p - i; j++)
				if ( last[j] <= i) break;
				

		    sum += j;
			for ( int jj = j + 1; jj < p - i; jj ++ )
				last[jj - 1] = last[jj];
		}
	

		out<<"Case #"<<nn<<": "<< sum<<endl;
	}// end of nn

}