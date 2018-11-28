#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

const int INF = 2147483647;
const int MAXN = 20005;
int T, N, M;

int next[MAXN];
void getNext(char *P)
{
	int len = strlen(P);
	int k = -1;
	next[0] = -1;
	for(int i = 1;i < len;++i)
	{
		while(k > -1 && P[k+1] != P[i])//注意k > -1而不是>0
			k = next[k];
		if(P[k+1] == P[i])	++k;
		next[i] = k;
	}
}

int KMP(char *T,char *P)//T为文本，P为模式串
{
	int cnt = 0;
	getNext(P);//若是一个模式串匹配多个文本串，要在KMP外调用
	int len_T = strlen(T);
	int len_P = strlen(P);
	int k = -1;
	for(int i = 0;i < len_T;++i)
	{
		while(k > -1 && P[k+1] != T[i])
			k = next[k];
		if(P[k+1] == T[i])	++k;
		if(k == len_P - 1)//P已匹配	
		{
			++cnt;
			k = next[k];//寻找下一个匹配
		}
	}
	return cnt;
}

char A[MAXN], B[MAXN];
bool ok(int a, int b)
{
	itoa(a, A, 10);
	itoa(b, B, 10);
	int len = strlen(A);
	for(int i = 0;i < len;++i)
	{
		B[len+i] = B[i];
	}
	B[len*2] = 0;
	//printf("%s %s\n", A, B);
	if(KMP(B, A))	return true;
	else return false;
	printf("%s %s\n", A, B);
}
int a, b;
int getlen(int a)
{
	char s[100];
	itoa(a, s, 10);
	return strlen(s);
}

int main()
{
	//freopen("out.txt","w", stdout);
	scanf("%d", &T);
	for(int t = 1;t <= T;++t)
	{
		bool stop = 0;
		int ans = 0;
		scanf("%d%d", &a, &b);
		for(int i = a;i < b;i++)
		{
			for(int j = i+1;j <= b;j++)
			{
				if(getlen(i) < getlen(j))	break;
				if(getlen(j) > getlen(i))
				{
					stop = 1;
					break;
				}
				if(ok(i, j))	++ans;
			}
			if(stop)	break;
			
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}

