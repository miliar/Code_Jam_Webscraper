#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

void solve();
void runCase();

char ch_map[]="\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x20\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x0\x79\x68\x65\x73\x6f\x63\x76\x78\x64\x75\x69\x67\x6c\x62\x6b\x72\x7a\x74\x6e\x77\x6a\x70\x66\x6d\x61\x71\x0\x0\x0\x0\x0";

void runCase()
{
	string input;

	char buf[501] = {0};
	cin.getline(buf,501);
	input = buf;
#if 0
	cin.getline(buf,501);
	string ans2 = buf;
	
	for(int i = 0; i < (int)input.length(); i++) {
		ch_map[input[i]] = ans2[i];
	}
#else
	string ans2 = buf;
	for(int i = 0; i < (int)input.length(); i++) {
		ans2[i] = ch_map[input[i]];
	}
#endif
	cout << ans2 << endl;
	
	//printf("%04d\n",num[target.length()-1]);
}

void solve()
{
	int n;
	scanf("%d",&n);
	getchar();
	
	for(int i = 0; i < n; i++) {
		printf("Case #%d: ",i+1);
		runCase();
	}
#if 0
	for(int i = 0; i < 128; i++) {
		printf("\\x%x",ch_map[i]);
	}
#endif
}

int main()
{
	solve();
	return 0;
}
