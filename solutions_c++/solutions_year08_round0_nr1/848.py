#include <iostream>
#include <set>
#include <string>

using namespace std;

int main()
{
	int N, S, Q, answer;
	set<string> available, current;
	char input[101];
	cin >> N;
	for(int casenum = 1; casenum <= N; ++casenum)
	{
		available.clear(); answer = 0;
		cin >> S; cin.get();
		for(int engines = 0; engines < S; ++engines)
		{
			cin.getline(input, 101);
			available.insert(input);
		}
		current = available;
		cin >> Q; cin.get();
		for(int i = 0; i < Q; ++ i)
		{
			cin.getline(input, 101);
			current.erase(input);
			if(current.empty())
			{
				current = available;
				current.erase(input);
				++answer;
			}
			
		}
		cout << "Case #" << casenum << ": " << answer << endl;
	}
	return 0;
}
