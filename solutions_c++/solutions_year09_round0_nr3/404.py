//#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

ifstream cin("C-large.in",ios::in);
ofstream cout("C-large.out",ios::out);

string gcj = "welcome to code jam";
map < pair < int, int >, int > mem;

int rec(string str, int gcji, int stri)
{
	if (mem.count(make_pair(gcji,stri))) return mem[make_pair(gcji,stri)];
	if (gcji == 19) return 1;
	int n = str.length();
	int cnt = 0;
	for (int i = stri; i < n; i++)
		if (str[i] == gcj[gcji])
			cnt += rec(str, gcji+1, i+1) % 10000;
	cnt = cnt % 10000;
	mem[make_pair(gcji,stri)] = cnt;
	return cnt;
}

void welcome()
{
	string str;
	ws(cin);
	getline(cin, str);
	int ans = rec(str, 0, 0);
	if (ans/1000 == 0) cout<<0;
	if (ans/100 == 0) cout<<0;
	if (ans/10 == 0) cout<<0;
	cout<<ans;
}

int main()
{
	int N;
	cin>>N;
	for (int i=1; i<=N; i++) {
		mem.clear();
		cout<<"Case #"<<i<<": ";
		welcome();
		cout<<endl;
	}
	return 0;
}