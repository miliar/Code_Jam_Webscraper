#include <iostream>
#include <fstream>
using namespace std;

ifstream Inp("A-small-attempt0.in");
ofstream Out("output.io");

char change(char tar)
{
	int x;
	char google[27]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
    char normal[27]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q',' '};

	for(x = 0; x < 27; x++)
	{
		if(google[x] == tar) {return normal[x];}
	}
}

int main()
{	
	int i, j, n;
	string line;
	
	Inp >> n;
	getline(Inp, line);

	for(j = 1; j <= n; j++)
	{
		getline(Inp, line);
		Out << "Case #" << j << ": ";
		for(i = 0; i < line.length(); i++)
		{
			Out << change(line[i]);
		}
		Out << endl;
	}
}
