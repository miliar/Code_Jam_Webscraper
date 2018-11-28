#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
#define LET(x,a) typeof(a)x(a)
#define FOR(i,a,n) for(LET(i,a);i<n;++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define cs c_str()
#define GI ({int t; scanf("%d",&t); t;})
#define EACH(it,v) for(LET(it,v.begin()); it!=v.end(); ++it)
#define dbg(x) (fout << #x << ":" << (x) << "\t")
#define dbge(x) (dbg(x), fout << endl)

ifstream fin("input.txt");
ofstream fout("output.txt");


int main()
{

  	clock_t start=clock();
	
	int kases; fin>>kases;
	for(int kase = 0; kase<kases;++kase)
	{
		int P, Q; fin>>P>>Q;
		fin.ignore();
		char buff[1000];
		fin.getline(buff, 1000);
		stringstream sin(buff);
		vector<int> v; int val;
		while(sin>>val)v.pb(val-1);
		
		assert((int)v.sz == Q);
		
		vector<int> perm;
		REP(i, Q)perm.pb(i);
		
		int minval = INT_MAX;
		do
		{
			int cost = 0;
			int left[P], right[P];
			REP(i, P)left[i] = (i ? left[i-1]+1 : 0), right[P-i-1] = ( i ? right[P-i] + 1 : 0);			
			
			REP(i, Q)
			{
				cost += left[v[perm[i]]] + right[v[perm[i]]];
				
				left[v[perm[i]]]= right[v[perm[i]]] = 0;
				if(v[perm[i]]+1 < P)left[v[perm[i]] + 1] = 0;
				if(v[perm[i]]-1 >= 0)right[v[perm[i]]-1] = 0; 
				
				for(int j=v[perm[i]]+2; j<P && left[j] != 0; ++j)left[j] = left[j-1]+1;
				for(int j=v[perm[i]]-2; j>=0 && right[j] != 0; --j)right[j] = right[j+1] + 1;
			}
		
			minval <?= cost;
		}while(next_permutation(perm.begin(), perm.end()));
		
		fout<<"Case #"<<(kase+1)<<": "<<minval<<endl;
	}

	clock_t end=clock();
	cout <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
	
	return 0;
}
