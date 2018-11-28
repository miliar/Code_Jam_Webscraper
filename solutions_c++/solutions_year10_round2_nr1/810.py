#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

void Output(const char *str)
{
	static int x = 0;
	x++;
	printf("Case #%d: %s\n", x, str);
}

void Output(long long ans)
{
	static int x = 0;
	x++;
	printf("Case #%d: %I64d\n", x, ans);
}

void solve()
{
	int N,M;
	scanf("%d%d", &N, &M);
	
	set<string> oldDir;
	vector<string> newDir;
	
	char buf[101];
	oldDir.insert(string(""));
	for(int i = 0; i < N; i++) {
		scanf("%s",buf);
		int len = strlen(buf);
		oldDir.insert(string(buf, buf+(len)));
		for(int j = 0; j < len; j++) {
			if( buf[len-1-j] == '/' ) {
				oldDir.insert(string(buf, buf+(len-1-j)));
			}
		}
	}
	for(int i = 0; i < M; i++) {
		scanf("%s",buf);
		int len = strlen(buf);
		newDir.push_back(string(buf, buf+(len)));
		for(int j = 0; j < len; j++) {
			if( buf[len-1-j] == '/' ) {
				newDir.push_back(string(buf, buf+(len-1-j)));
			}
		}
	}
	
	sort(newDir.begin(), newDir.end());
	int num = newDir.size();
	
	long long ans = 0;
	for(int i = 0; i < num; i++) {
		// Output(newDir[i].c_str());
		if( oldDir.count(newDir[i]) == 0 ) {
			oldDir.insert(newDir[i]);
			ans++;
		}
	}
	Output(ans);
}

void GCJ2010_R1B_A()
{
	int T;
	scanf("%d", &T);
	while(T--) {
		solve();
	}
}

int main()
{
	GCJ2010_R1B_A();
	return 0;
}

