#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main()
{
	ifstream in("Input.txt");
	ofstream out("Output.txt");
	char Letters[30] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	int T, N;
	char Temp = 0;
	string Lines[30];
	string Trans[30];
	//cin >> T;
	in >> T;
	in.get(Temp);
	Temp = 0;
	for(int i = 0; i < T; i++)
	{
			//cin >> Lines[i];
		while(Temp != 10)
		{
			in.get(Temp);
			Lines[i] += Temp;
		}
		Temp = 0;
	}
	for(int i = 0; i < T; i++)
	{
		Trans[i] = Lines[i];
		for(int j = 0; j < Lines[i].length(); j++)
		{
			N = Lines[i][j];
			if(N > 96)
				Trans[i][j] = Letters[N - 97];
			else if(N == 32)
				Trans[i][j] = 32;
			else
				Trans[i][j] = 10;
		}
	}
	for(int i = 1; i <= T; i++)
	{
		//cout << "Case #" << i << ": " << Trans[i - 1] << endl;
		out << "Case #" << i << ": ";
		int j = 0;
		while(Trans[i - 1][j] != 10)
		{
			out << Trans[i - 1][j];
			j++;
		}
		out << endl;
	}
	out.close();
	in.close();
	return 0;
}