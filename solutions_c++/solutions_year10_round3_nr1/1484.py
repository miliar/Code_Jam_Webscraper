//by enitink
#include	<iostream>

using namespace std;

#define		SIZE	1000

int main(){
	int t, i, n, j, k;
	int result;
	int heights[SIZE][2];
	cin >> t;
	for(i = 1; i <= t; ++i){
		cin >> n;
		result = 0;
		for( j = 0; j < n; ++j){
			cin >> heights[j][0] >> heights[j][1];
			if(j == 0)
				continue;
			for(k = 0; k < i; ++k){
				if((heights[j][0] < heights[k][0]) && (heights[j][1] > heights[k][1]))
					++result;
				if((heights[j][0] > heights[k][0]) && (heights[j][1] < heights[k][1]))
					++result;
			}
		}
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}
