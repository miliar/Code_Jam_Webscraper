#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	char map[30] = {'y','h','e','s','o','c','v','x','d','u','i',
		'g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	string str;
	int t;

	cin >>t;

	cin.ignore();

	for (int i =1;i <= t;++i)
	{
		getline(cin,str);

		cout << "Case #"<<i<<": ";
		for (int i = 0;i < str.size();++i)
		{
			if (str[i] != ' ')
				cout << map[str[i] - 'a'];
			else 
				cout <<str[i];
		}
		cout <<endl;
	}
	return 0;
}