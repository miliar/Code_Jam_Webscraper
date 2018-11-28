#include <iostream>
#define MAX_CHARS 501
using namespace std;

int main(void)
{
	int N;
	char key[] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};
	unsigned long long int solution[20][MAX_CHARS];
	
	for(int j = 0; j < MAX_CHARS; j++) solution[0][j] = 1;
	
	cin >> N;
	cin.get();
	for(int numCase = 1; numCase <= N; numCase++)
	{
		string line;
		
		getline(cin, line);
		for(int i = 1, max_i = sizeof(key)/sizeof(char); i <= max_i; i++)
		{
			for(int j = 1, max_j = line.size(); j <= max_j; j++)
			{
				if(key[i - 1] == line[j - 1]) solution[i][j] = (solution[i - 1][j] + solution[i][j - 1]) % 100000000;
				else solution[i][j] = solution[i][j - 1];
			}
		}
		
		printf("Case #%d: %04llu\n", numCase, solution[sizeof(key)/sizeof(char)][line.size()] % 10000);
	}
}
