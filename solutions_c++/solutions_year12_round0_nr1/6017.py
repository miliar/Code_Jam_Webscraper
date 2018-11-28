#include <iostream>
#include <string>
using namespace std;

int main()
{
	int N ; 
	cin >> N ; 
	cin.get() ; 

	string con = "yhesocvxduiglbkrztnwjpfmaq";
	for(int n = 1 ; n <= N ; n++) {
		string s ; 
		getline(cin, s) ;

		cout<<"Case #"<<n<<": " ;

		for(int i = 0 ;i < s.size() ; i++) {
			if( s[i] == ' ') cout<<" ";
			else cout<< con[ s[i]-'a'] ;
		}
		cout<<endl;
	}

	return 0 ; 
}