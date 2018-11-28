#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int mp[250];

int mn;
int num;

int getNum(char ch)
{
	if (mp[ch] == -1)
	{
		mp[ch] = mn++;
		if (mn == 1)
			mn = 2;
		else if (mn == 2)
			mn = 0;
		num++;
	}
	return mp[ch];
}

int n;

int ar[100];


long long getResult()
{
	long long res = 0;
	num = max(num, 2);
	for (int i = 0; i < n; i++)
	{
		res = num * res + ar[i];
	}
	return res;
}

int main()
{
	ifstream input("Input.txt");
	ofstream output("output.txt");
	int tt;
	input >> tt;
	for (int ttt = 1; ttt <= tt; ttt++)
	{
		string st;
		input >> st;
		memset(mp, -1, 150 * 4);
		mn = 1;
		num = 0;
		n = st.length();
		for (int i = 0; i < n; i++)
			ar[i] = getNum(st[i]);
		output << "Case #" << ttt << ": " << getResult() << '\n';



	} 

	return 0;
}