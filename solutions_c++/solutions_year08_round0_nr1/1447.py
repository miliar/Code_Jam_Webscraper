#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

int main()
{
	int N;
	int t = 0;
	cin >> N;
	vector<string> search;
	while(N--)
	{
		int S,Q;
		cin >> S;
		char str[101];
		string en;
		getchar();
		for(int i = 0; i< S; ++i) 
		{
			gets(str);
			en = str;
			search.push_back(en);
		}
		cin >> Q;
		int ans = 0;
		set<string> now_have;
		getchar();
		for(int i = 0; i< Q; ++i)
		{
			gets(str);
			en = str;
			if(now_have.find(en)==now_have.end())
			{
				if(now_have.size() == S-1)
				{
					ans ++;
					now_have.clear();
					now_have.insert(en);
				}
				else
				{
					now_have.insert(en);
				}
			}
		}
		cout << "Case #" << ++t << ": ";
		cout << ans << endl;
	}
	return 0;
}