#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;
int main()
{
 	FILE *fin=fopen("A.in","r");
 	FILE *fout=fopen("A.out","w");
	int T,N,K;
	fscanf(fin,"%d",&T);
	for(int i=1;i<=T;i++)
	{
	    fscanf(fin,"%d%d",&N,&K);
	    int M=(1<<N);
		if(K%M==(M-1))
		fprintf(fout,"Case #%d: ON\n",i);
		else
		fprintf(fout,"Case #%d: OFF\n",i);		
			 
    }
    getchar();
    return 0;
}


