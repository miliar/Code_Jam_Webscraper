#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>

using namespace std;

int main()
{
	vector<string> inp;
	string hold;
	int cases = 0;
	ifstream myfile;
	myfile.open("case.txt");
	
	if (myfile.is_open())
	{
		getline(myfile,hold);
		inp.push_back(hold);
		cases = atoi(inp[0].c_str());
		while(!myfile.eof())
		{
			getline(myfile,hold);
			inp.push_back(hold);
		}
	}
	myfile.close();

	//convert
	for(int j=1; j<=cases; j++)
	{
		for(int k=0; k<inp[j].length(); k++)
		{
			if(inp[j][k] == 'y'){inp[j][k] = 'a';}
			else if(inp[j][k] == 'n'){inp[j][k] = 'b';}
			else if(inp[j][k] == 'f'){inp[j][k] = 'c';}
			else if(inp[j][k] == 'i'){inp[j][k] = 'd';}
			else if(inp[j][k] == 'c'){inp[j][k] = 'e';}
			else if(inp[j][k] == 'w'){inp[j][k] = 'f';}
			else if(inp[j][k] == 'l'){inp[j][k] = 'g';}
			else if(inp[j][k] == 'b'){inp[j][k] = 'h';}
			else if(inp[j][k] == 'k'){inp[j][k] = 'i';}
			else if(inp[j][k] == 'u'){inp[j][k] = 'j';}
			else if(inp[j][k] == 'o'){inp[j][k] = 'k';}
			else if(inp[j][k] == 'm'){inp[j][k] = 'l';}
			else if(inp[j][k] == 'x'){inp[j][k] = 'm';}
			else if(inp[j][k] == 's'){inp[j][k] = 'n';}
			else if(inp[j][k] == 'e'){inp[j][k] = 'o';}
			else if(inp[j][k] == 'v'){inp[j][k] = 'p';}
			else if(inp[j][k] == 'z'){inp[j][k] = 'q';}
			else if(inp[j][k] == 'p'){inp[j][k] = 'r';}
			else if(inp[j][k] == 'd'){inp[j][k] = 's';}
			else if(inp[j][k] == 'r'){inp[j][k] = 't';}
			else if(inp[j][k] == 'j'){inp[j][k] = 'u';}
			else if(inp[j][k] == 'g'){inp[j][k] = 'v';}
			else if(inp[j][k] == 't'){inp[j][k] = 'w';}
			else if(inp[j][k] == 'h'){inp[j][k] = 'x';}
			else if(inp[j][k] == 'a'){inp[j][k] = 'y';}
			else if(inp[j][k] == 'q'){inp[j][k] = 'z';}
		}
	}
	//cases
	for(int i=1; i<=cases; i++)
	{
		cout << "Case #" << i << ": ";
		cout << inp[i] << endl;
	}

	
	return 0;
}
