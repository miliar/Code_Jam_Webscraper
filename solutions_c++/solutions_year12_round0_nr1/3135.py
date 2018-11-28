#include <iostream>
#include <cstdio>
using namespace std;

#define gout case_number++, printf("Case #%d: ", case_number), cout 

int case_number;
char from[] = {"abcdefghijklmnopqrstuvwxyz"};
char to[] =   {"yhesocvxduiglbkrztnwjpfmaq"};

int main()
{
	int t;
	char s[120];
	
	cin >> t;
	
	cin.get();
	while (t--){
		cin.getline (s, 120);
		for (int i = 0; s[i] != '\0'; i++){
			if (s[i] == ' ') continue;
			s[i] = to[ s[i] - 'a' ];
		}
		gout << s << endl;
	}
	
	return 0;
}
