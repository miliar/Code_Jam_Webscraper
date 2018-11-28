#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <math.h>
#include <set>
#include <vector>
#define abs(x) ((x) >= 0 ? (x) : -(x))
#define bit_clear (a, b) ((a) & ~((uinteger)1 << (b)))
#define bit_set (a, b) ((a) | ((uinteger)1 << (b)))
#define bit_test (a, b) ((a) >> (b) & 1)

#define max (a, b) ((a) >= (b) ? (a) : (b))
#define min (a, b) ((a) <= (b) ? (a) : (b))

using namespace std;

int main(int argc, char *argv[])
{
    int lines;
    std::cin >> lines;
    vector<int> pset;
    for (int i=0;i<lines;i++) {
	int P,K,L;
	cin >> P >> K >> L;
	int press=0;
	int tval;
	int KEYS[P];
	for(int k=0; k<K; k++)
		KEYS[k]=K;
	pset.clear();

	for(int k=0; k<L; k++)
		{
		cin >> tval;
		pset.push_back(tval);
		}

	sort(pset.begin(), pset.end());
	int count=0;
	int val=1;

	int pp[pset.size()];

	int c=pset.size()-1;

	for(vector<int>::iterator key=pset.begin(); key!=pset.end(); key++)
		{
		pp[c]=*key;
		c--;
		}

	for(int k=0; k<pset.size(); k++)
		{
		press+=(pp[k])*val;
		if((count+1)%K==0)
			val++;
		count++;
		}
	cout << "Case #"<<i+1<<": "<<press << endl;
    }
return 0;
}
