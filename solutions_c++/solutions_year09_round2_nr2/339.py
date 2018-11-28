#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXD = 30;

char str[MAXD];
int str_len;

int main()
{
	int casi;


	cin >> casi;
	for (int caso = 1; caso <= casi; caso++)
	{
		cin >> str;
		str_len = strlen(str);
		cerr << "\"" << str << "\"\n";

		int smallerID = -1;
		for (int i = str_len-1; i >= 0; i--)
		{
			for (int j = i+1; j < str_len; j++)
			{
				if (str[j] > str[i] && (smallerID == -1 || str[j] < str[smallerID]))
					smallerID = j;
			}
	
			if (smallerID != -1) // Posso non aggiungere uno zero
			{
				// Swappa e ordina sulla destra in ordine crescente
				swap(str[smallerID], str[i]);
				sort(str + i+1, str + str_len);
				break;
			}
		}
		if (smallerID == -1) // Devo aggiungere uno zero
		{
			// Aggiungilo in coda, ordina e swappa col primo numero + grande
			str[str_len] = '0';
			str[++str_len] = '\0';
			sort(str, str + str_len);
			int j = 0;
			while (j < str_len && str[j] == '0') j++;
			if (j < str_len) swap(str[0], str[j]);
		}
		
		cout << "Case #" << caso << ": " << str << "\n";
	}

	return 0;
}

