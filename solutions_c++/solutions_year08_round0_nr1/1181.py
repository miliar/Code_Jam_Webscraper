#include <iostream>
#include <set>
using namespace std;

int nOfTest;
set<string> engine, query;

void work()
{
	int S, Q;
	scanf("%d\n", &S);
	string temp;

	engine.clear();
	for(int i=0; i<S; i++)
	{
		getline(cin, temp);
		engine.insert(temp);
	}

	scanf("%d\n", &Q);
	query.clear();
	int ans = 0;
	for(int i=0; i<Q; i++)
	{
		getline(cin, temp);
		if (engine.find(temp) != engine.end())
			query.insert(temp);
		if (query.size() == engine.size())
		{
			ans++;
			query.clear();
			query.insert(temp);
		}
	}
	if (query.size())
		ans++;
	cout << max(ans-1, 0) << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> nOfTest;
	for(int testCase=0; testCase<nOfTest; testCase++)
	{
		printf("Case #%d: ", testCase+1);
		work();
	}
}
