#include <iostream>
using namespace std;

int main()
{
	int cc[26][26];
	int co[26][26];
	string ans;
	int cases;
	cin >> cases;
	int count;// steps
	char a, b, c;
	for (int i = 0 ; i < cases; i++)
	{
		for (int j = 0 ; j < 26 ; j ++)
			for (int k = 0 ; k < 26 ; k++)
				cc [j][k] = 0;
		for (int j = 0 ; j < 26 ; j ++)
			for (int k = 0 ; k < 26 ; k++)
				co [j][k] = 0;
		ans.clear();
		//Step 1
		cin >> count;
		for (int j = 0; j < count ; j++)
		{
			cin >> a >> b >> c;
			cc [a - 'A'][b - 'A'] = c ;
			cc [b - 'A'][a - 'A'] = c ;
		}
		//Step 2
		cin >> count;
		for (int j = 0; j < count ; j++)
		{
			cin >> a >> b;
			co [a - 'A'][b - 'A'] = -1;
			co [b - 'A'][a - 'A'] = -1;
		}
		//Step 3
		cin >> count;
		for (int j = 0; j < count ; j++)
		{
			cin >> a;
			ans.push_back(a);
			if (ans.size() == 1)
				continue;
			//Combine
			while ((ans.size() >= 2)
				&&(cc [ ans[ans.size()-1]-'A' ][ ans[ans.size()-2]-'A' ] != 0))
			{
				c = cc [ ans[ans.size()-1]-'A' ][ ans[ans.size()-2]-'A' ];
				ans.erase(ans.size()-1);
				ans.erase(ans.size()-1);
				ans.push_back(c);
			}
			//Oppose
			for (int k = 0 ; k < (ans.size() - 1) ; k++)
			{
				if ( co [ans[k] - 'A'][ans[ans.size()-1]-'A'] == -1)
				{
					ans.clear();
					break;
				}
			}
		}
		cout << "Case #" << i + 1 << ": [";
		bool flag = false;
		for (int j = 0 ; j < ans.size() ; j++)
		{
			if (flag) cout << ", ";
			cout << ans[j] ;
			flag = true;
		}
		cout << "]" << endl;
	}
}
