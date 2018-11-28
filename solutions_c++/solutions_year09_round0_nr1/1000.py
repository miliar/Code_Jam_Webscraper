#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

int L, D, N;
map<string, int> m;


int Count(const vector<string> & v, const string & s, int index)
{
int ret = 0;
	
	if(index == L) return 1;
	
	for(int i = 0; i < v[index].size(); i ++)
		if(m[s + v[index][i]]) ret += Count(v, s + v[index][i], index + 1);
	
	return ret;
}

int main()
{
	cin >> L >> D >> N;
	
	for(int i = 0; i < D; i ++)
	{
	string buff;
		
		cin >> buff;
		
		for(int j = 1; j <= L; j ++)
		{
			m[buff.substr(0, j)] = 1;
//			cout << buff.substr(0, j) << "\n";
		}
		
//		system("pause");
	}
	
	for(int i = 0; i < N; i ++)
	{
	int idx = 0, flag = 0;
	string buff;
	vector<string> v(L, "");
		
		cin >> buff;
		
		for(int j = 0; j < buff.size(); j ++)
		{
			if(buff[j] == '(') {flag ++;}
			
			if(buff[j] == ')') {flag --; idx ++;}
			
			if('a' <= buff[j] && buff[j] <= 'z')
			{
				v[idx] += buff[j];
				
				if(flag == 0) idx ++;
			}
		}
		
		int ans = Count(v, "", 0);
		
		cout << "Case #" << i + 1 << ": " << ans<< "\n";
		cerr << ans << "\n";
	}
	
//	system("pause");
	
	return 0;
}

/*
TEST 0:
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc

*/
