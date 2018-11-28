#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;



int main(int argc, char** argv)
{	
	if(argc < 2) {
		cout<<"Please pass input file name as argument"<<endl;
		return -1;
	}
	freopen(argv[1], "rt", stdin);

	int T;
	cin>>T;
	for(int i = 0; i < T; i++)
	{
		int P, K, L;
		cin>>P>>K>>L;
		vector<long> freqs;
		for(int f = 0; f < L; f++){
			long freq;
			cin>>freq;
			freqs.push_back(freq);
		}
  		sort(freqs.begin(), freqs.end());
		reverse(freqs.begin(), freqs.end());
		int l = 0, p = 1;
		int lonk = 0;
		int nump = 0;
		while(l != L) {
			nump += (p*freqs[l]);
			if((l+1) % K == 0) {
				p++;
				lonk ++;
				if(lonk == P && (l+1) < L) {
					nump = -1;
					break;
				}
			}	
			l++;
		}
		cout<<"Case #"<<i+1<<": "<<nump<<endl;
		
	}
	return 0;
}