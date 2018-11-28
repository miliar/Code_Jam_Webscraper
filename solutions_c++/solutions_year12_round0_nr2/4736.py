#include <iostream>

using namespace std;

int main(){
	int number;
	cin >> number;
	for(int i=1; i<=number; i++){
		int g, S, p;
		cin >> g >> S >> p;
		int result = 0;
		for(int j=0; j<g;j++){
			int ti;
			cin >> ti;
			if(ti<=0){
				if(p==0)
					result++;
			}
			else if((ti-1)/3>=p-1){
				result++;
			}else if(ti%3!=1&&(ti-1)/3>=p-2&&ti>1&&S>0){
				result++;
				S--;
			}
		}
		cout << "Case #" << i << ": " << result << endl;
	}
}