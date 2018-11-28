// B.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;
int C, D, N;
int appear[128];
string Solve()
{
	string ans, input;
	vector<string> Co;
	vector<string> Op;
	Co.resize(36);
	Op.resize(28);
	cin >> C;
	for(int i = 0; i<C; ++i)
		cin >> Co[i];
	cin >> D;
	for(int i = 0; i<D; ++i)
		cin >> Op[i];
	cin >> N;
	cin >> input;
	memset(appear, 0, sizeof(appear));
	ans = " ";
	for(int i = 0; i<N; ++i){
		char ch = input[i];
		bool flag = false;
		for(int j = 0; j < C; ++j)
			if(Co[j][0] == ans.back() && Co[j][1] == ch
				|| Co[j][1] == ans.back() && Co[j][0] == ch){
					appear[ans.back()]--;
					ans.pop_back();
					ans.push_back(Co[j][2]);
					flag = true;
					break;
			}
		if(flag)
			continue;
		for(int j = 0; j<D; ++j)
			if(appear[Op[j][0]]>0 && Op[j][1] == ch 
				|| appear[Op[j][1]]>0 && Op[j][0] == ch){
					ans = " ";
					memset(appear, 0, sizeof(appear));
					flag = true;
			}
		if(flag)
			continue;
		ans.push_back(ch);
		appear[ch]++;
	}
	string tmp = "[";
	for(int i = 1; i+1<ans.length(); ++i){
		tmp += ans[i];
		tmp += ", ";
	}
	if(ans.length() > 1)
		tmp += ans.back();
	tmp += ']';
	return tmp;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int nCase;
	cin >> nCase;
	for(int i = 1; i<=nCase; ++i){
		string ret = Solve();
		cout << "Case #" << i << ": " << ret << "\n" ;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}

