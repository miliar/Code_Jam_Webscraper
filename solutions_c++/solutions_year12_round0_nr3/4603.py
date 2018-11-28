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
		while(k > -1 && P[k+1] != P[i])//ע��k > -1������>0
			k = next[k];
		if(P[k+1] == P[i])	++k;
		next[i] = k;
	}
}

int KMP(char *T,char *P)//TΪ�ı���PΪģʽ��
{
	int cnt = 0;
	getNext(P);//����һ��ģʽ��ƥ�����ı�����Ҫ��KMP�����
	int len_T = strlen(T);
	int len_P = strlen(P);
	int k = -1;
	for(int i = 0;i < len_T;++i)
	{
		while(k > -1 && P[k+1] != T[i])
			k = next[k];
		if(P[k+1] == T[i])	++k;
		if(k == len_P - 1)//P��ƥ��	
		{
			++cnt;
			k = next[k];//Ѱ����һ��ƥ��
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

