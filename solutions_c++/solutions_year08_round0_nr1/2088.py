
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>

using namespace std;

#define P(X) /*{ cout<<#X<<"="<<(X)<<endl; }*/

int main(int argc, char* argv[])
{
	if (argc<2)
	 return 0;
   	ifstream fin(argv[1]);
    int ncases;
    fin>>ncases;
P(ncases)

	string tmp;
	for(int n=0; n<ncases; ++n)
	{
		cout<<"Case #"<<n+1<<": ";
		int nnodes;
		fin>>nnodes; getline(fin,tmp);
P(nnodes)

		vector<int> mins(nnodes);
		map<string, int> x;
		while(nnodes--) { string s; getline(fin,s); x[s]=nnodes; P(s)}
		int nreq;
		fin>>nreq; getline(fin,tmp);
P(nreq) 
		while(nreq--)
		{
			string s; getline(fin, s); int pos = x[s]; P(s) P(pos)
			int minelem = 1<<25;
			for(size_t i=0; i<mins.size(); ++i) if (i!=pos) minelem = min(minelem, mins[i]);
			mins[pos]=1+minelem;
		}

		cout<<*min_element(mins.begin(), mins.end())<<endl;
	}

	return 0;
}


