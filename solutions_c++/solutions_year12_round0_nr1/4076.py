#include <iostream>
#include <fstream>
using namespace std;
int main ()
{
	char ch[200], expn[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	int n;
	
	cin>>n;
	cin.getline(ch, 200, '\n');
	for (int i = 0; i < n; i++)
	{
		cin.getline(ch, 200, '\n');
		
		cout<<"Case #"<<i+1<<": ";
		
		for (int j = 0; j < strlen(ch); j++)
		{
			if (isalpha(ch[j]))
				cout << expn[( (int)(ch[j]) ) % 97];
			else
				cout << ch[j];
		}
		cout<<endl;
	}
	return 0;
}
