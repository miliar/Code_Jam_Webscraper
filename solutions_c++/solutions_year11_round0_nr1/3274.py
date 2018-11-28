#include <iostream>
using namespace std;
#include <vector>
int	main(){
	int m,n;
	vector<int> seq,next;
	cin >> n;
	for(int i = 0 ; i < n; i++){
		int lastO = -1;
		int lastB = -1;
		int firstO, firstB;
		cin >> m;
		seq.clear();
		seq.resize(m);
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
			seq[j]=k;
		}

//		cout << endl;
//		for(int l = 0; l < m; l++)
//			cout << " " << next[l];
//		cout << endl;

		int posB = 1;
		int posO = 1;
		int nextB = (-seq[firstB]);
		int nextO = seq[firstO];
		int directionB = 0;
		int directionO = 0;
		if( nextO > posO ) directionO = 1;
		else if( nextO < posO ) directionO = -1;
		else directionO = 0;
		if( nextB > posB ) directionB = 1;
		else if( nextB < posB ) directionB = -1;
		else directionB = 0;

		int sum = 0;


		for( int id = 0 ; id < m ; id++){
			if( seq[id] > 0 )// it is a O
			{
				int steplen =  abs(seq[id] - posO);
				posO = seq[id];
				sum += steplen+1;
				if( steplen+1 > abs(nextB-posB) ){
					posB = nextB;
				}
				else{
					posB += (steplen+1) * directionB;
				}
				nextO = seq[next[id]];
				if( nextO > posO ) directionO = 1;
				else if( nextO < posO ) directionO = -1;
				else directionO = 0;

			}else{//it is a B
				int steplen = abs(-seq[id] - posB);
				sum += steplen+1;
				posB = (-seq[id]);
				if( steplen+1 > abs(nextO - posO) ){
					posO = nextO;
				}
				else{
					posO += (steplen+1) * directionO;
				}
				nextB = (-seq[next[id]]);
				if( nextB > posB ) directionB = 1;
				else if( nextB < posB ) directionB = -1;
				else directionB = 0;
			}
//			cout << "PosO:" << posO << ","
//				 << "PosB:" << posB << ","
//				 << "nextO:" << nextO
//				 << ",nextB:" << nextB
//				 << ",sum:" << sum
//				 << endl;
		}
		cout << "Case #"<< i+1 <<": " << sum << endl;

	}
}