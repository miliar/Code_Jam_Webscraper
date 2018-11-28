#include<iostream>
#include<algorithm>

using namespace std;

string ssort(string n)
{
	string s;
	n += '0';
	sort(n.begin(), n.end());
	int i;
	for (i = 0; n[i] == '0'; i++);
	s += n[i];
	for (int j = 0; j < i; j++) s += '0';
	for (int j = i + 1; j < n.size(); j++) s += n[j];
	return s;
}
bool check(string n)
{
	int j = 0;
	for (int i = 1; i < n.size(); i++)
	{
		if (n[j++] < n[i]) return false;
	}
	return true;
}
int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		string n;
		cin >> n;
		if (check(n)) 
		{
			cout << "Case #" << i << ": " << ssort(n);

		}
		else 
		{
			next_permutation(n.begin(), n.end());
			cout << "Case #" << i << ": " << n;
		}
		cout << endl;
	}
	return 0;
}
