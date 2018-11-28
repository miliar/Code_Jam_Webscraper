#include <iostream>
using namespace std;
int main(){
	int n;
	cin >> n;
	for(int kase=1; kase<=n; kase++){
		string s;
		cin >> s;
start:
		for(int i=s.size()-1; i>0; i--){
			if(s[i]>s[i-1]){
				for(int j=s.size()-1; ; j--){
					if(s[j]>s[i-1]){
						swap(s[j], s[i-1]);
						sort(s.begin()+i,s.end());
						goto find;
					}
				}
			}
		}
		s="0"+s;
		goto start;
find:
		cout<<"Case #"<<kase<<": "<<s;
		cout<<endl;
	}
}

