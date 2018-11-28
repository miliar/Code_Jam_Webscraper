#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int num;
	int tmp;
	cin >> num;

	for(int c=1;c<=num;c++) {
		int total = 0;	
		int p,k,l;
		cin >> p >> k >> l;
		vector< int > keys(k,0);

		vector<int> freq;
		for(int j=0;j<l;j++) {
			cin >> tmp;
			freq.push_back(tmp);
		}
		sort(freq.begin(), freq.end());

		for(int j=freq.size()-1;j>=0;j--) {
			
			int leastused = 0;
			for(int m = 1; m<k;m++) {
				if(keys[m] <= keys[leastused]) 
					leastused = m;
			}
			
		        keys[leastused]++;
			int keynum = keys[leastused];		
			total += keynum*freq[j];
		}
		cout << "Case #" << c << ": " << total << endl;	
	}
}
