// c.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>


using namespace std;

string search = " welcome to code jam";

int nou[20], vechi[20];
int Result(string str)
{
	memset(nou, 0, sizeof(nou));
	memset(vechi, 0, sizeof(vechi));
	vechi[0] = 1;
	for(int i = 0; i < (int)str.size(); i++)
	{
		for(int j = 1; j < (int)search.size(); j++)
		{
			nou[j] = 0;
			if(search[j] == str[i])
				nou[j] += vechi[j - 1];
			nou[j] += vechi[j];
			while(nou[j] >= 10000)
				nou[j] -= 10000;
		}
		for(int j = 1; j < 20; j++)
			vechi[j] = nou[j];
	}
	return vechi[search.size() - 1];
}

int main()
{
	freopen("c.out", "w", stdout);
	ifstream in;
	in.open("c.in");
	int T;
	in >> T;
	string crtString;
	getline(in, crtString);
	for(int t = 1; t <= T; t++)
	{
		getline(in, crtString);
		cout << "Case #" << t << ": ";
		// modify on 4 digits
		int rez = Result(crtString);
		if(rez < 1000) cout << "0";
		if(rez < 100) cout << "0";
		if(rez < 10) cout << "0";
		cout << rez << endl;
	}
	return 0;
}

