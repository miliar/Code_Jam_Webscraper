#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
	unsigned int t, caseNum, count;
	char G[105];
	
	scanf("%d", &t);
	cin.ignore(100, '\n');
	
	for (caseNum = 1; caseNum <= t; caseNum++)
	{
		//scanf("%s", G);
		cin.getline(G, 101);
		
		for (count = 0; count < strlen(G); count++)
		{
			switch (G[count])
			{
				case ' ':
					break;
				case 'a':
					G[count] = 'y';
					break;
				case 'b':
					G[count] = 'h';
					break;
				case 'c':
					G[count] = 'e';
					break;
				case 'd':
					G[count] = 's';
					break;
				case 'e':
					G[count] = 'o';
					break;
				case 'f':
					G[count] = 'c';
					break;
				case 'g':
					G[count] = 'v';
					break;
				case 'h':
					G[count] = 'x';
					break;
				case 'i':
					G[count] = 'd';
					break;
				case 'j':
					G[count] = 'u';
					break;
				case 'k':
					G[count] = 'i';
					break;
				case 'l':
					G[count] = 'g';
					break;
				case 'm':
					G[count] = 'l';
					break;
				case 'n':
					G[count] = 'b';
					break;
				case 'o':
					G[count] = 'k';
					break;
				case 'p':
					G[count] = 'r';
					break;
				case 'q':
					G[count] = 'z';
					break;
				case 'r':
					G[count] = 't';
					break;
				case 's':
					G[count] = 'n';
					break;
				case 't':
					G[count] = 'w';
					break;
				case 'u':
					G[count] = 'j';
					break;
				case 'v':
					G[count] = 'p';
					break;
				case 'w':
					G[count] = 'f';
					break;
				case 'x':
					G[count] = 'm';
					break;
				case 'y':
					G[count] = 'a';
					break;
				case 'z':
					G[count] = 'q';
					break;
			} // switch end
		} // count for end
		
		printf("Case #%d: %s\n", caseNum, G);
	} // caseNum for end
	
	return 0;
}
