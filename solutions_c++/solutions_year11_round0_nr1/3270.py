#include <iostream>
using namespace std;
#include <vector>


int	main(){
	int m,n;
	vector<int> input,next;
	cin >> n;
	for(int i = 1 ; i <= n; i++){
		int lastO = -1;
		int lastB = -1;
		int firstO, firstB;
		cin >> m;
		input.clear();
		input.resize(m);
		next.clear();
		next.resize(m);
		for(int j = 0 ; j < m; j++){
			char c;
			int	k;
			cin >> c >> k;
			if( c == 'B'){
				k = -k;
				if(lastB!= -1) next[lastB]=j;else firstB = j;
				lastB = j;
			}else{
				if(lastO!= -1) next[lastO]=j; else firstO = j;
				lastO = j;
			}
			input[j]=k;
		}

		int posB = 1;
		int posO = 1;
		int nextB = (-input[firstB]);
		int nextO = input[firstO];
		int increasementB = 0;
		int increasementO = 0;
		if( nextO > posO ) increasementO = 1;
		else if( nextO < posO ) increasementO = -1;
		else increasementO = 0;
		if( nextB > posB ) increasementB = 1;
		else if( nextB < posB ) increasementB = -1;
		else increasementB = 0;

		int sum = 0;


		for( int id = 0 ; id < m ; id++){
			if( input[id] > 0 )// it is a O
			{
				int steplen =  abs(input[id] - posO);
				posO = input[id];
				sum += steplen+1;
				if( steplen+1 > abs(nextB-posB) ){
					posB = nextB;
				}
				else{
					posB += (steplen+1) * increasementB;
				}
				nextO = input[next[id]];
				if( nextO > posO ) increasementO = 1;
				else if( nextO < posO ) increasementO = -1;
				else increasementO = 0;

			}else{//it is a B
				int steplen = abs(-input[id] - posB);
				sum += steplen+1;
				posB = (-input[id]);
				if( steplen+1 > abs(nextO - posO) ){
					posO = nextO;
				}
				else{
					posO += (steplen+1) * increasementO;
				}
				nextB = (-input[next[id]]);
				if( nextB > posB ) increasementB = 1;
				else if( nextB < posB ) increasementB = -1;
				else increasementB = 0;
			}
		}
		cout << "Case #"<< i <<": " << sum << endl;

	}
}