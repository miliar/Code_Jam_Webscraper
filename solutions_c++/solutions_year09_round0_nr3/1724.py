#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

const string welcome = "welcome to code jam";

int num_welcome(string &str, int i = 0)
{
	if (str.length() < welcome.length() - i)
	{
		return 0;
	}
	if (i == (int)welcome.length())
	{
		return 1;
	}

	int result = 0;
	int pos;

	string tmp = str;
	while ((pos = tmp.find(welcome[i])) != string::npos)
	{
		tmp = tmp.substr(pos + 1);
		result += num_welcome(tmp, i + 1);
	}

	return result;
}

int main()
{

	int n;
	cin >> n >> std::ws;

	for (int i = 0; i < n; ++i)
	{
		string in;
		getline(cin, in);
		
		cout << "Case #" << i + 1 << ": " << setw(4) << setfill('0') << num_welcome(in) << endl;
	}
	return 0;
}