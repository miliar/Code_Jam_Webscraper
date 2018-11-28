#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("infile.in");
ofstream fout("outfile.out");


const int SIZE = 105;
bool released[SIZE];


int main()
{
	int T; fin>>T;
	for(int t=1; t<=T; t++) {
		int P,Q; fin>>P>>Q;
		vector<int> toBeReleased;
		for(int i=0; i<Q; i++) {
			int x; fin>>x;
			toBeReleased.push_back(x);
		}

		sort(toBeReleased.begin(), toBeReleased.end());
		int minCoins=P*P*P;
		do {
			for(int i=1; i<=P; i++) released[i]=false;
			released[0]=released[P+1]=true;

			int coins=0;
			for(int i=0; i<Q; i++) {
				for(int j=toBeReleased[i]-1; !released[j]; j--)
					coins++;
				for(int j=toBeReleased[i]+1; !released[j]; j++)
					coins++;
				released[toBeReleased[i]]=true;
			}
			if(coins<minCoins) minCoins=coins;
		} while(next_permutation(toBeReleased.begin(), toBeReleased.end()));

		fout<<"Case #"<<t<<": "<<minCoins<<endl;
	}
	
	return 0;
}