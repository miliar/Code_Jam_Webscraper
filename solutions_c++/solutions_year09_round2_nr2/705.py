#include<iostream>
#include<string>
#include<algorithm>
using namespace std;


int		main(){
		int t, T;
		string A,B;
		//freopen("in.txt","r",stdin);
		//freopen("out.txt","w",stdout);
		for(cin>>T,t=1; t<=T; t++){
			cin >> A;
			B = A;
			if (!next_permutation(A.begin(), A.end())){
				A = "0" + B;
				next_permutation(A.begin(), A.end());
			}
			cout<<"Case #"<<t<<": "<<A<<endl;
		}
		return 0;
}





