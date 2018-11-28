#include <iostream>
#include <algorithm>
using namespace std;
int main(){
	int n;
	string str1,str2;
	cin>> n;
	for(int i=1;i<=n;i++){
		cin >> str1;
		str2 = str1;

		if(next_permutation(str1.begin(), str1.end())){
			cout<<"Case #"<<i<<": "<<str1<<endl;
		}else{
				str2 = "0" + str2;
				next_permutation(str2.begin(),str2.end());
				cout<<"Case #"<<i<<": "<<str2<<endl;
		}
		
	}
}
