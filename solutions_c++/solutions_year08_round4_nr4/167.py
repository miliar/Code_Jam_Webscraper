#include <iostream>
#include <cstdio>
#include <map>
#include <vector>
#include <set>
#include <numeric>
#include <iterator>
#include <sstream>
#include <list>

#define pb push_back
#define mp make_pair
#define foreach(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)

template<typename T> inline bool setmin(T &a, T b) { if(a>=b) { a=b; return true; } return false; }
template<typename T> inline bool setmax(T &a, T b) { if(a<=b) { a=b; return true; } return false; }

using namespace std;

void process(int tcase)
{
    int k;
    int ming=999999;
    string S;
    cin >> k >> S;
    vector<int> V;
    V.resize(k);
    for(int i=0;i<k;i++)
	V[i]=i;
    do
    {
	int ng=0;
	char nc=0;
	for(int i=0;i<S.length();i++)
	{
	    char tmp = S[(i/k*k) + V[i%k]];
	    if(nc != tmp)
	    {
		nc = tmp;
		ng++;
	    }
	}
	setmin(ming,ng);
    } while(next_permutation(V.begin(),V.end()));

    cout << "Case #" << tcase << ": " << ming << endl;
}

int main(void)
{
    int T;
    cin >> T;
    for(int t=1;t<=T;t++)
    {
        process(t);
    }
}
