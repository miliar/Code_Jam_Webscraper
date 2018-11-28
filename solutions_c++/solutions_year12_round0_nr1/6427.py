#include<iostream>
#include<string>

#define T 30
#define N 27

using namespace std;

int main()
{
	string s;
	int t;
	char abc[N] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '};
	char goo[N] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q', ' '};
	cin >> t;
	
	for(int i = 0; i <= t; i++)
	{
		getline(cin, s);
		if(s.length() != 0){
			cout << "Case #" << i << ": ";
			for (int j = 0; j < s.length(); j++)
			{
				int z = 0;
				while(s[j] != goo[z])
				{
					z++;
				}
				cout << abc[z];
			}
			cout << endl;
		}
	}
	

return 0;
}
