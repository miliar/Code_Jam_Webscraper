#include <iostream>
#define MAX 501

using namespace std;

int find_word(char* text, char* word, int index, int letter)
{
	if(letter > 18)
		return 1;

	int wynik = 0;
	for(int i = index; text[i] != 0; i++)
		if(text[i] == word[letter])
			wynik = (wynik + find_word(text, word, i + 1, letter + 1)) % 1000;

	return wynik;
}

int main()
{
	int N;
	cin >> N;
	
	getchar();
	for(int i = 0; i < N; i++)
	{
		char word[] = "welcome to code jam", text[MAX];
		gets(text);
		
		cout << "Case #" << i + 1 << ": ";
        printf("%04d\n", find_word(text, word, 0, 0));
	}
	return 0;
}
