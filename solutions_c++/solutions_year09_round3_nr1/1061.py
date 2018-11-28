#include <iostream>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

void Work(unsigned i);

int main()
{
	unsigned cases;
	cin >> cases;
	cin.ignore(); // New Line
	for (unsigned i = 1; i<= cases; i++)
	{
		Work(i);
	}
	return 0;
}

void Work(unsigned i)
{
	//cerr << "Working..." << endl;
	map <char, int> Map;
	int base = 0;


	string Number;
	
	getline(cin, Number);

	for (int j = 0; j < Number.length(); j++)
	{
		if (Map[Number[j]] != 100)
		{
			base++;
			Map[Number[j]] = 100;
		}
	}
	//cerr << "The base is " << base << endl;

	vector<uint8_t> NumHandled(Number.length(), 0);

	int NextNum = 0;
	//cerr << "Handled Number: ";
	if (Number.length() == 1)
	{
		cout << "Case #" << i << ": 1" << endl;
		return;
	}
	if (base == 1)
	{
		base++;
	}
//	for (int j = Number.length()-1; j >= 0; j--)
	for (int j = 0; j < Number.length(); j++)
	{
		if (Map[Number[j]] == 100)
		{
/*			// Get a number to fill in
			if (Number[j] == Number[0])
				Map[Number[j]] = 1;
			else if (NextNum == 1)
				Map[Number[j]] = --NextNum;
			else if (Number[j] == Number[1])
				Map[Number[j]] = 0;
			else
				Map[Number[j]] = NextNum--;*/
			if (NextNum == 0)
				Map[Number[j]] = ++NextNum; // 1
			else if (NextNum == 1)
			{
				Map[Number[j]] = 0;
				NextNum++;
			}
			else
			Map[Number[j]] = NextNum++;
		}
		NumHandled[j] = Map[Number[j]];
		//cerr << (int) NumHandled[j] << ' ';
	}
	//cerr << endl;

	uint64_t Ans = 0;
	for (int j = 0, k = NumHandled.size()-1; j < NumHandled.size(); j++,k--)
	{
		Ans += pow(base, j)*NumHandled[k];
	}

	cout << "Case #" << i << ": " << Ans << endl;
}
