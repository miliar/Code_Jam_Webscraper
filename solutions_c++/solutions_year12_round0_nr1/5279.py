#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	char t[] = {'y', 'h', 'e', 's', 'o', 'c',  'v', 'x', 'd',  'u', 'i',  'g', 'l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int N;
	cin >> N;
	char* g = new char[101];
	char* s = new char[101];
	scanf("\n");
	
	for(int n = 0; n < N; n++)
	{
		cin.getline(g, 101);
		
		for(int i = 0; i < 101; i++)
		{
			if(g[i] == '\0')
			{
				s[i] = g[i];
				break;
			}
				
			
			if(g[i] != ' ')
			{
				s[i] = t[(int)g[i]-97];
			}
			else
				s[i] = g[i];
		}
		
		
		printf("Case #%d: %s\n", n+1, s);
	}	
	
	return 0;
}