#include <iostream>
#include <string.h>
using namespace std;

int main()
{
	char lower[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	char upper[26] = {'Y','H','E','S','O','C','V','X','D','U','I','G','L','B','K','R','Z','T','N','W','J','P','F','M','A','Q'};
	int round = 0;
	cin>>round;
	cin.get();
	for (int n = 1; n <= round; n++){
		char str[101]; 
		cin.getline(str, 101);
		cout<<"Case #"<<n<<": ";
		for ( int i = 0; i < strlen(str); i++ ){
			if ( str[i] >= 'a' && str[i] <= 'z' ){
				cout<<lower[str[i] - 'a'];
			} else {
				if ( str[i] >= 'A' && str[i] <= 'Z' ){
					cout<<upper[str[i] - 'A'];
				} else {
					cout<<str[i];
				}
			}
		}
		cout<<endl;
	}
	return 0;
}