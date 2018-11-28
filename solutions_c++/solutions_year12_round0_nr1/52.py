#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int N;
	string line, translate = "yhesocvxduiglbkrztnwjpfmaq";//"yhesocvxduiglbkr?tnwjpfma?";
	
	scanf("%d\n", &N);
	for(int i = 0; i < N; i++)
	{
		getline(cin, line);
		for(int j = line.size() - 1; j >= 0; j--)
			if(line[j] <= 'z' && line[j] >= 'a')
				line[j] = translate[line[j] - 'a'];
		printf("Case #%d: %s\n", i + 1, line.c_str());
	}
	
	return 0;
}
