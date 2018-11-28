#include <iostream>
#include <deque>

using namespace std;

int main()
{
	int T;
	cin >> T;
	getchar();
	
	for(int i = 0; i < T; i++)
	{
		deque<char> input;
		char in[100];
		
		gets(in);
		for(int j = 0; in[j]; j++)
			input.push_back(in[j]);
		
		int znaki[input.size()];
		
		for(int j = 0; j < input.size(); j++)
			znaki[j] = -1;
		
		int licznik = 1;
		for(int j = 0; j < input.size(); j++)
			if(znaki[j] == -1)
			{
				for(int k = j; k < input.size(); k++)
					if(input[j] == input[k])
						znaki[k] = licznik;
			if(licznik == 1)
				licznik = 0;
			else if(licznik == 0)
				licznik = 2;
			else
				licznik++;
		}
		
		if(licznik == 0)
			licznik = 2;
		
		long long output = 0;
		for(int j = 0; j < input.size(); j++)
			output = output * licznik + znaki[j];
		
		printf("Case #%d: %lld\n", i + 1, output);
	}
	return 0;
}
