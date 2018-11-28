#define inFileName "d-small-attempt0.in"
#define outFileName "d-small.out"

#include <cstdio>
#include <iostream>
#include <fstream>

//FILE * f = fopen(inFileName,"rt");
//FILE * g = fopen(outFileName,"wt");
std::ifstream f(inFileName,std::ifstream::in);
std::ofstream g(outFileName,std::ofstream::out);

#include <strstream>
#include <sstream>

#include <cmath>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>

#include <utility>
#include <algorithm>

using namespace std;

typedef pair<int,int> pii;
typedef vector<string> VS;
typedef vector<int> VI;
typedef __int64 ll;

#define all(v) (v).begin(),(v).end()
#define foreach(it, v, type) for(type::iterator it = (v).begin(); it != (v).end(); ++it)
#define forn(i,N) for(int i=0;i<(N); ++i)
#define pb push_back

//////////////////////////////////////////////////////////////////////////

int main()
{
	int nTests; f>>nTests;
	string s;

	forn(TestIndex,nTests)
	{
		//fprintf(g,"Case #%d: ",TestIndex+1);
		g<<"Case #"<<TestIndex+1<<": ";
		cout<<"Case #"<<TestIndex+1<<": ";
		int k;
		f>>k;
		getline(f,s);
		getline(f,s);
		
		VI p(k);
		forn(i,p.size()) p[i]=i;
		int bestRes = 1000000000;
		do{
			int res=0;
			for(int i=1;i<s.size();i++)
				if (s[k*(i/k)+p[i%k]]!=s[k*((i-1)/k)+p[(i-1)%k]]) res++;
			if (res<bestRes)
				bestRes = res;
		}
		while(next_permutation(all(p)));
		g<<bestRes+1;
		cout<<bestRes+1;

		g<<endl;
		cout<<endl;
	}
	return 0;
}
