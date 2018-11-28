#include <iostream>
using namespace std;


int main(){

	pair<char,char> a;
	int caseNumber;
	cin >> caseNumber;
	for(int i=0;i<caseNumber;i++){
		int n,number,min,sum,Sum;
		cin >> n >> number;
		min =number;
		sum =number;
		Sum =number;
		for(int j=1;j<n;j++){
			cin >> number;
			sum^=number;
			Sum+=number;
			if(number<min)
				min=number;
		}
		if(sum!=0)
			cout << "Case #" << i+1 << ": NO" <<endl;
		else
			cout << "Case #" << i+1 << ": " << Sum-min << endl;
	}
	
	return 0;
}
