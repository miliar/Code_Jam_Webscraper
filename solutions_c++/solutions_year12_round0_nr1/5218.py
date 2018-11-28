// codejam2012.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <string>


using namespace std;

int main()
{
	int MAP[] = {24, 7, 4, 18, 14, 2, 21, 23, 3, 20, 8, 6, 11, 1, 10, 17, 25, 19, 13, 22, 9, 15, 5, 12, 0, 16};
	int T;
	cin >> T;
	string* G = new string[T];
	cout << "";
	
	int len;

	getline(cin, G[0]);
	for(int i = 0; i < T; i++)
	{
		getline(cin, G[i]);
	}

	for(int i = 0; i < T; i++)
	{
		len = strlen(G[i].c_str());
		for(int j = 0; j < len; j++)
		{
			if(G[i][j] != ' ')
			G[i][j] =  MAP[G[i][j] - 'a'] + 'a';
		}
		cout <<"Case #" << i + 1 << ": " << G[i] << endl;
	}
	//delete G;
	return 0;
}

