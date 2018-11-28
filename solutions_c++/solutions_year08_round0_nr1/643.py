#include <stdio.h>
#include <iostream>
#include <cstring>
#include <map>
#define maxs 110
#define maxl 110
#define maxq 1010
using namespace std;
int N,S,Q;
int op[2][maxs];
int minl[maxs];
int minr[maxs];
int num[maxq];
string se[maxs];
string qu[maxq];
map <string,int> pp;
int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> N;
	for (int cases = 1;cases <= N;cases++)
	{
		cin >> S;
		cin.get();
		for (int i = 0;i < S;i++) getline(cin,se[i]);
		cin >> Q;
		cin.get();
		for (int i = 0;i < Q;i++) getline(cin,qu[i]);
		for (int i = 0;i < S;i++) pp[se[i]] = i + 1;
		for (int i = 0;i < Q;i++) num[i] = pp[qu[i]] - 1;
		memset(op,0,sizeof(op));
		int now  = 0,pre;
		for (int i = 0;i < Q;i++)
		{
			pre = now;
			now = 1 - now;
			memset(op[now],-1,sizeof(op[now]));
			memset(minl,-1,sizeof(minl));
			memset(minr,-1,sizeof(minr));
			minl[0] = op[pre][0];
			for (int j = 1;j < S;j++)
			{
				minl[j] = minl[j - 1];
				if (op[pre][j] != -1 && minl[j] > op[pre][j]) minl[j] = op[pre][j];
			}
			minr[S - 1] = op[pre][S - 1];
			for (int j = S - 2;j >= 0;j--)
			{
				minr[j] = minr[j + 1];
				if (op[pre][j] != -1 && minr[j] > op[pre][j]) minr[j] = op[pre][j];
			}
			for (int j = 0;j < S;j++) if (j != num[i])
			{
				op[now][j] = -1;
				int temp = -1;
				if (j - 1 >= 0 && minl[j - 1] != -1 && (temp == -1 || temp > minl[j - 1])) temp = minl[j - 1];
				if (j - 1 < S && minr[j + 1] != -1 && (temp == -1 || temp > minr[j + 1])) temp = minr[j + 1];
				if (temp != -1 && (op[now][j] == -1 || op[now][j] > temp + 1)) op[now][j] = temp + 1;
				temp = op[pre][j];
				if (temp != -1 && (op[now][j] == -1 || op[now][j] > temp)) op[now][j] = temp;
			}
			else {op[now][j] = -1;}
		}
		int ans = Q;
		for (int i = 0;i < S;i++) if (op[now][i] != -1 && ans > op[now][i]) ans = op[now][i];
		cout << "Case #" << cases << ": " << ans << endl;
	}
	return 0;
}
