#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>
#include <algorithm>

using namespace std;
int main()
{
	int T;

	cin >> T;
	for(int t=1; t<=T; t++){
		int N, L, H;
		cin >> N;
		cin >> L;
		cin >> H;
		vector<unsigned long int> frequency;
		for(int i=0; i<N; i++){
			unsigned long int t;
			cin >> t;
			frequency.push_back(t);
			
		}
		
		long int res=-1;
		for(long int f=L; f<=H; f++){
			bool div = true;
			for(int i=0; i<N; i++){
				if (frequency[i]%f != 0  &&  f%frequency[i] !=0){
					div = false;
					break;
				}
			}
			if (div){
				res = f;
				break;
			}
		}
		
		cout << "Case #" << t << ": ";
		if (res > 0)  cout << res << endl;
		else  cout << "NO" << endl;
	}
	
	return 0;
}

