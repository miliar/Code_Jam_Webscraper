#include <stdio.h>
#include <iostream>
#include <string.h>
#include <string>

using namespace std;


string translate(char *c)
{
	int l = strlen(c);
	string s = "";

	for(int i = 0; i < l; i++)
	{
		switch(c[i])
		{
		case 'a': s.append("y"); break;
		case 'b': s.append("h"); break;
		case 'c': s.append("e"); break;
		case 'd': s.append("s"); break;
		case 'e': s.append("o"); break;
		case 'f': s.append("c"); break;
		case 'g': s.append("v"); break;
		case 'h': s.append("x"); break;
		case 'i': s.append("d"); break;
		case 'j': s.append("u"); break;
		case 'k': s.append("i"); break;
		case 'l': s.append("g"); break;
		case 'm': s.append("l"); break;
		case 'n': s.append("b"); break;
		case 'o': s.append("k"); break;
		case 'p': s.append("r"); break;
		case 'q': s.append("z"); break;
		case 'r': s.append("t"); break;
		case 's': s.append("n"); break;
		case 't': s.append("w"); break;
		case 'u': s.append("j"); break;
		case 'v': s.append("p"); break;
		case 'w': s.append("f"); break;
		case 'x': s.append("m"); break;
		case 'y': s.append("a"); break;
		case 'z': s.append("q"); break;
		case ' ': s.append(" "); break;
		}
	}
	return s;
}

int main(int argc, char **argv)
{
	int cases = 0;
	char l[256];
	string result;
	
	scanf("%d", &cases);
	int i = 0;

	while(i < (cases +1))
	{
		memset(l,0x00,256);
		cin.getline(l,256);

		if(i != 0){

		result = translate(l);
		cout << "Case #" << i-1 <<": " << result << endl;
		}
		i++;
	}

	return 0;
}