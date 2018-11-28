#include <iostream>
#include <string>
using namespace std;
int compute (int a, int b){
	if (b>a||b==a){
		return 1;
	}
	else{
		return (a-b);
	}
}
int main(){
	int T, N, O[101], B[101];
	//string str;
	cin>> T;
	int color;
	for (int i=0; i<T;++i){
		cin >> N;

		char temp;
		int number;
		int total = 0;
		int oo = 0, bb = 0;
		int pre_o = 1;
		int pre_b = 1;
		for (int j=0; j<N;++j){
			cin >> temp;
			cin >> number;
			//cout << temp <<" "<< number << endl;
			if (temp == 'O'){
				//cout << "compute O"<<compute(abs(number-pre_o)+1,oo)<<endl;
				int step = abs(number-pre_o) + 1;
				int O = compute (step,oo);
				total += O;
// <<"c o "<< compute(step,oo)<<endl;
				bb += O;
				oo = 0;
				pre_o = number;
			}

			if (temp == 'B'){
				int step = abs(number-pre_b) + 1;
			//	cout << "compute B"<<compute(abs(number-pre_b)+1,bb)<<endl;
                int B = compute(step,bb);
				total += B;
				//cout <<"c b "<< compute(step,bb)<<endl;
				oo += B;
				bb = 0;
				pre_b = number;
			}

		}
		cout <<"Case #"<<i+1<<": "<< total <<endl;

	}
	//system("pause");
}
