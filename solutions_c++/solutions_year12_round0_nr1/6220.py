// googlerese.cpp -MysticBoy

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int T; 
	char G[(30+1)][(100+10)];

	int i, j;

	cin >> T;
	
	for(i = 0; i <= T; i++)
		cin.getline(G[i], 105);
	
	char GtoE [26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	
	char Eng[31][110];
	for(i = 1; i <= T; i++)
	{
		for(j = 0; G[i][j] != '\0'; j++ )
		{
			Eng[i][j] = ' ';
			Eng[i][j] = ( G[i][j] != ' '? GtoE[(G[i][j]-'a')] : ' ');
		}

		Eng[i][j]='\0';
		cout <<"Case #"<<i <<": "<< Eng[i] << endl;
	}

	return 0;
}

