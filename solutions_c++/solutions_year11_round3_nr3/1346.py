#include<iostream>
#include<vector>

using namespace std;
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int n,l,h,tmp;
		vector<int> freq;
		cin>>n>>l>>h;
		for(int j=0;j<n;j++){
			cin>>tmp;
			freq.push_back(tmp);
		}
		bool valid = false;
		for(int f=l;f<=h;f++){
			valid = true;
			for(int c=0;c<freq.size();c++) {
				if(!((freq[c]%f==0) || (f%freq[c]==0))){
					valid = false;
					break;
				}
			}
			if(valid) {
				
				cout<<"Case #"<<i<<": "<<f<<endl;
				break;
			}
		}
		if(!valid) {
			cout<<"Case #"<<i<<": NO"<<endl;
		}      
	}
}
