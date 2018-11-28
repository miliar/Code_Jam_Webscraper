#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>

using namespace std;
int main()
{
	int T;

	cin >> T;
	for(int t=1; t<=T; t++){
		int R, C;
		vector<string> picture;
		
		cin >> R;  cin >> C;
		for(int i=0; i<R; i++){
			string str;
			cin >> str;
			picture.push_back(str);
		}

		bool impossible = false;
		for(int i=0; i<R; i++){
			for(int j=0; j<C; j++){
				if (picture[i][j] == '#'){
					if (i == R-1  ||  j == C-1 ||
						picture[i+1][j] != '#' ||
						picture[i][j+1] != '#' ||
						picture[i+1][j+1] != '#' 
					){
						impossible = true;
						break;
					}
					picture[i][j] = picture[i+1][j+1] = '/';
					picture[i+1][j] = picture[i][j+1] = '\\';
				}
			}
			if (impossible)  break;
		}
		
		
		
		cout << "Case #" << t << ": " << endl;
		if (impossible)  cout << "Impossible" << endl;
		else{
			for(int i=0; i<R; i++){
				cout << picture[i] << endl;
			}
		}
	}
	
	return 0;
}

