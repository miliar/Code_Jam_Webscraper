#include <iostream>
#include <string.h>
using namespace std;
char temp[1000];
int ways[1000][25] = {0};

int main()
{
	string msg = "welcome to code jam";
	int T;
	cin>>T;
	cin.ignore();
	for(int t=1 ; t<=T ; t++)
	{
		cin.getline(temp,10000);
		string str = string(temp);
		
		memset(ways , 0 , sizeof(ways));

		ways[0][0] = 1;

		for(int i=1  ; i<=str.size() ; i++)
		{
			ways[i][0] = 1;
			for(int j=1 ; j<=19 ; j++)
			{
				ways[i][j] = ways[i-1][j];
			
				if(ways[i-1][j-1] && str[i-1] == msg[j-1])
					ways[i][j] += ways[i-1][j-1];

				ways[i][j] %= 10000;
			}
		}
	
		printf("Case #%d: %04d\n" , t , ways[str.size()][msg.size()]);
	}
	return 0;
}
