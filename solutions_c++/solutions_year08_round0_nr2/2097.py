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
#include <fstream>
#define SZ(a) a.size()
#define PB push_back
#define FOR(i,s,n) for(int i=s; i<n; i++)
#define FORI(i,n) for(int i=0; i<n; i++)
#define FORSZ(i,n) for(int i=0; i<SZ(n); i++)
#define ALL(x) x.begin(),x.end()

using namespace std;
int main(int argc, char* argv[])
{
	int ninp;
	string s,s2;
	ifstream fin(argv[1]);
	fin >> ninp;
	getline(fin,s);
	for (int prob=1; prob <= ninp; prob++)
	{
		int SA=0;
		int SB=0;
		int T,NA,NB;
		int DA[1450]={0};
		int AA[1450]={0};
		int DB[1450]={0};
		int AB[1450]={0};

		fin >> T;
		getline(fin,s);
		fin >> NA;
		fin >> NB;
		getline(fin,s);
		FORI(i,NA)
		{
			getline(fin,s);
			int h1,m1,h2,m2;
			sscanf(s.c_str()  , "%d:%d %d:%d", &h1,&m1,&h2,&m2);
			DA[h1*60+m1]++;
			AB[h2*60+m2+T]++;
		}
		FORI(i,NB)
		{
			getline(fin,s);
			int h1,m1,h2,m2;
			sscanf(s.c_str()  ,"%d:%d %d:%d", &h1,&m1,&h2,&m2);
			DB[h1*60+m1]++;
			AA[h2*60+m2+T]++;
		}

		int A=0;
		int B=0;

		for (int t=0; t<=(23*60+59); t++)
		{
			A+=AA[t];
			B+=AB[t];
			A-=DA[t];
			B-=DB[t];
			if (A<0) 
			{
				SA += (-A);
				A = 0;
			}
			if (B<0) 
			{
				SB += (-B);
				B = 0;
			}

		}
		printf("Case #%d: %d %d\n", prob, SA, SB);
	
	}



	return 0;
}

