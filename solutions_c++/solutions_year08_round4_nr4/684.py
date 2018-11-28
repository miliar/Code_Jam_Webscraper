#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <cmath> 
#include <queue>
#include <fstream>
#include <map>

using namespace std;

#define FOR(i,a) for(int i=0; i<a.size(); i++) 
#define FR(i,n) for(int i=0; i<n; i++)
#define FR2(i,start,n) for(int i=start; i<n; i++)
#define VI vector <int>
#define VS vector <string>
#define SZ(a)  (int)((a).size())
#define SORT(a) sort(a.begin(),a.end())    
#define PB(a,b) ((a).push_back(b))

void main()
{
	ifstream in("D-small.in");
	ofstream out("D-small.out");
	int testCases; string temporary; getline(in,temporary); stringstream sinple(temporary); sinple>>testCases;
	for(int tst=0; tst<testCases; tst++)
	{	
		int k; in >> k;
		string S; in >> S; int best = SZ(S)+100;
		VI p(k,0); FOR(i,p) p[i] = i;
		do
		{
			
			string temp = "";
			FR(i,SZ(S)/k)
			{
				string toAdd = "";
				FR(j,k)
				{
					toAdd += S[i*k+p[j]];
				}
				temp += toAdd;
			}
			int cnt = 1;
			char cur = temp[0];
			for(int i=1; i<SZ(temp); i++)
			{
				if(temp[i]!=temp[i-1])
				{
					cnt++;
				}
			}
			best = min(best,cnt);
		}
		while(next_permutation(p.begin(),p.end()));
	
		
		
		out << "Case #" << tst+1 << ": " << best << endl;
	}
}
