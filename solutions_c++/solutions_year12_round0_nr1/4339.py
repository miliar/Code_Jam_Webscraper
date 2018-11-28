#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int line=0, testCases;

int main()
{
	string buff;
	scanf("%d",&testCases);
	getline (cin, buff);
	for (line; line<testCases;line++)
	{
		char temp;
		string in;
		getline (cin, in);
		for(int i=0; i<in.length(); i++)
			{
				if (in[i] == 'e') { in[i] = 'o';}
				else if (in[i] == 'q') { in[i] = 'z';}
				else if (in[i] == 'z') { in[i] = 'q';}
				else if (in[i] == 'j') { in[i] = 'u';}
				else if (in[i] == 'p') { in[i] = 'r';}
				else if (in[i] == 'm') { in[i] = 'l';}
				else if (in[i] == 'y') { in[i] = 'a';}
				else if (in[i] == 's') { in[i] = 'n';}
				else if (in[i] == 'l') { in[i] = 'g';}
				else if (in[i] == 'c') { in[i] = 'e';}
				else if (in[i] == 'k') { in[i] = 'i';}
				else if (in[i] == 'd') { in[i] = 's';}
				else if (in[i] == 'x') { in[i] = 'm';}
				else if (in[i] == 'v') { in[i] = 'p';}
				else if (in[i] == 'n') { in[i] = 'b';}
				else if (in[i] == 'r') { in[i] = 't';}
				else if (in[i] == 'i') { in[i] = 'd';}
				else if (in[i] == 'b') { in[i] = 'h';}
				else if (in[i] == 't') { in[i] = 'w';}
				else if (in[i] == 'a') { in[i] = 'y';}
				else if (in[i] == 'h') { in[i] = 'x';}
				else if (in[i] == 'w') { in[i] = 'f';}
				else if (in[i] == 'f') { in[i] = 'c';}
				else if (in[i] == 'o') { in[i] = 'k';}
				else if (in[i] == 'u') { in[i] = 'j';}
				else if (in[i] == 'g') { in[i] = 'v';}
			}
		cout << "Case #" << line+1 << ": " << in << endl;
	}
	return 0;
}
