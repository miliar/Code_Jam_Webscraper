#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

const char* google = "abcdefghijklmnopqrstuvwxyz";
const char* riktig = "yhesocvxduiglbkrztnwjpfmaq";
const int MAX = 110;

int main()	{
	int rounds;
	char str[MAX];
	cin >> rounds;	cin.ignore();
	for(int i = 0; i < rounds; i++)	{
		cin.getline(str, MAX);
		for(int j = 0; j < strlen(str); j++)	{
			for(int k = 0; k < strlen(google); k++)	{
				if(str[j] == google[k])	{
					str[j] = riktig[k];
					break;
				}
			}
		}
		cout <<"Case #" << i+1 <<": " << str <<"\n";
	}
	return 0;
}
