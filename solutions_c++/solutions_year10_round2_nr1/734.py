#include <iostream>
#include <set>
using namespace std;

set<string> paths;

int process_input(string s)
{
	if(s == "/")
		return 0;
	int result = paths.size();
	string x = "";
	for(int i = 1; i < s.size(); i++)
	{
		if(s[i] == '/')
			paths.insert(x);
		x += s[i];
	}
	paths.insert(x);
	return paths.size()-result;
}


void process_case(int t)
{
	int N,M;
	string s;

	paths.clear();

	cin >> N >> M;
	while(N--)
	{
		cin >> s;
		process_input(s);
	}			
	int result = 0;
	while(M--)
	{
		cin >> s;
		result += process_input(s);
	}	
	cout << "Case #" << t << ": " << result << endl;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
		process_case(i);
	return 0;
}
