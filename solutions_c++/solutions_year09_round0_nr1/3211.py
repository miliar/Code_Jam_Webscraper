#include<iostream>
#include<vector>
#include<string>
#include <algorithm>
using namespace std;
bool lookup(string ss, char c)
{
	for(int i=0; i<ss.length(); i++)
		if(ss[i]==c)
			return true;
	return false;
}
int main(){
	int L, D, N;
	cin >> L >> D >> N;
	vector <string> s(D);
	for(int i=0; i<D; i++){
		cin >> s[i];
	}
	for(int i=1; i<=N; i++){
		vector<string> t(L);
		printf("Case #%d: ", i);
		//cout << L << D << N;
		string test;
		cin >> test;
		int p=0;
		//cout << test;
		for(int k=0; k<test.length();)
		{
			//cout<<test[k];
			if(k<test.length() && test[k]=='('){
				k++;
				while(test[k]!=')'){
					t[p].push_back(test[k]);
					k++;			
				}
				k++;
				p++;
			}
			else if(k<test.length()){
				t[p].push_back(test[k]);
				k++;
				p++;
			}
		}
		int ans =0;
		for(int k=0; k<D; k++){
			string r = s[k];
			//cout << "String " << r << " is being tested ... \n";
			bool yes = true;
			for(p=0; p<L; p++){
				//cout << "is " << r[p] << " present in "<< t[p] << "?? \n";	
				if(!lookup(t[p], r[p])) {yes = false; break;}
			}		
			if(yes) ans++;
		}
		printf("%d\n", ans);	
	}	
	return 0;
}
