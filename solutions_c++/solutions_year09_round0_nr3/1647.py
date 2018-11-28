#include <iostream>
using namespace std;
char base[] = "welcome to code jam";//len = 19
char str[501];
int cnt;
int len;
void dfs(int id, int pos)
{
	if(id==19)
	{
		cnt++;
		return;
	}
	for(int i=pos; i<len; i++)
	{
		if(19-id > len-i) return;
		if(str[i]==base[id])
		{
			dfs(id+1, i+1);
		}
	}
}
int main()
{
	
	int t, k=0;
	cin >> t;
	cin.getline(str, 501);
	while(t--)
	{
		cin.getline(str, 501);
		len = strlen(str);
		cnt = 0;
		dfs(0, 0);
		cnt%=10000;
		printf("Case #%d: ", ++k);
		if(cnt<10) printf("000");
		else if(cnt<100) printf("00");
		else if(cnt<1000) printf("0");
		cout << cnt << endl;
	}
}
