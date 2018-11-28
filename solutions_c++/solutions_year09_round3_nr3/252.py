#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
ifstream inf;
ofstream outf;
#define FOR(i,a,b) for(int _b=(b),i=(a);i<=_b;i++)
#define FORD(i,a,b) for(int _b=(b),i=(a);i>=_b;i--)

char tmpb[100000];
int dp [600][600];
const int modd = 10000;
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	
	int tests;
	inf >> tests;
	
	

	for(int test = 0; test < tests; test++)
		{
			int n,q;
			inf >> n >> q;
			int anw = 100000000;
			vector<int> vis;
			vis.clear();
			for(int i = 0; i < q; i++) 
			{
				int tmp;
				inf >> tmp;
				vis.push_back(tmp - 1);
			}
			sort(vis.begin(), vis.end());
			do
			{
				int cur = 0;
				vector<int> free = vector<int>(n);
				for(int i = 0; i < q; i++)
				{
					int next = vis[i];
					free[next] = 1;
					for(int i = next -1; i >= 0; i--)
						if (free[i])
							break;
						else
							cur++;
					for(int i = next + 1; i < n; i++)
						if (free[i])
							break;
						else
							cur++;
				}
				if(cur < anw) anw = cur;

			}while (next_permutation(vis.begin(), vis.end()));

	
		
			outf << "Case #"  << test+1 << ": " ;
			outf <<  anw << endl;
			//if (test != tests-1) outf << endl;
		
	}
	
	outf.close();
	return 0;
}
