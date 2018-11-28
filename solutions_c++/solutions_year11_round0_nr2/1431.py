#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> Combine;
vector<string> Oppsoite;
vector<char> results;
string input;
int C, D, N;
bool Combined()
{
	int size = results.size();
	if (size < 2) return false;
	char s1 = results[size - 1], s2 = results[size - 2];
	for (int i = 0; i < C; i++)
	{
		const string &str = Combine[i];
		if (s1 == str.at(0) && s2 == str.at(1))
		{
			results.pop_back();
			results.pop_back();
			results.push_back(str.at(2));
			return true;
		}
		if (s1 == str.at(1) && s2 == str.at(0))
		{
			results.pop_back();
			results.pop_back();
			results.push_back(str.at(2));
			return true;
		}
	}
	return false;
}
bool Clear()
{
	bool visited[256];
	for (int i = 0; i < 256; i++) visited[i] = false;
	for (int i = 0; i < results.size(); i++) visited[results[i]] = true;
	for (int i = 0; i < D; i++) {
		const string &str = Oppsoite[i];
		char s1 = str.at(0), s2 = str.at(1);
		if (visited[s1] && visited[s2]) {
			results.clear();
			return true;
		}
	}
	return false;
}
int main()
{
	int t;
	cin >> t;
	for (int cases = 1; cases <= t; cases++)
	{
		cin >> C;
		Combine.resize(C);
		for (int i = 0; i < C; i++) cin >> Combine[i];
		cin >> D;
		Oppsoite.resize(D);
		for (int i = 0; i < D; i++) cin >> Oppsoite[i];
		cin >> N >> input;
		results.clear();
		for (int i = 0; i < N; i++)
		{
			results.push_back(input[i]);
			if (Combined()) continue;
			else if (Clear()) continue;
		}
		printf("Case #%d: [", cases);
		for (int i = 0; i < results.size(); i++)
		{
			if (i) printf(", ");
			printf("%c", results[i]);
		}
		printf("]\n");
	}
}