#include<iostream>
#include<vector>
#include<stack>

using namespace std;

int main() {
	string str = "welcome to code jam";

	int n;
	cin>>n;
	cin.ignore();
	
	for(int i=0;i<n;i++) {
		string input;
		vector<int> arr(str.size(),0);
		getline(cin,input);
		for(int j=0;j<input.size();j++) {
			if(str[0]==input[j]) {
				arr[0] =  (arr[0]+1)%10000;
			}
			for(int k=1;k<str.size();k++) {
				if(str[k]==input[j]) {
					arr[k] = (arr[k]+arr[k-1])%10000;
				}
			}
		}
//		for(int j=0;j<arr.size();j++)
//		    cout<<arr[j]<<" ";
//		cout<<"\n";
		cout<<"Case #"<<i+1<<": ";
		stack<int> s;
		int num = arr[arr.size()-1];
		for(int j=0;j<4;j++) {
			s.push(num%10);
			num /= 10;
		}
		for(int j=0;j<4;j++) {
			cout<<s.top();
			s.pop();
		}
		cout<<'\n';
	}
}
