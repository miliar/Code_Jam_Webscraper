#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <map>
#include <string>
using namespace std;

map<string, int> map1;
int f[2][100];
int swt;

int work()
{
	int S, Q, i, j, k, ret;
	char s[256];

	scanf("%d", &S);
	gets(s);

	for (i = 0; i < S; i++){
		gets(s);
		map1[s] = i;
	}

	scanf("%d", &Q);
	gets(s);

	if (Q == 0) return 0;

	int q;
	gets(s);
	q = map1[s];

	swt = 0;
	for (i = 0; i < S; i++) f[swt][i] = 0;
	f[swt][q] = -1;

	for (i = 1; i < Q; i++){
		gets(s);
		q = map1[s];
		
		swt = !swt;

		for (j = 0; j < S; j++){
			if (j == q){
				f[swt][j] = -1;
			}else{
				int min = 10000, t;
				for (k = 0; k < S; k++){
					if (f[!swt][k] == -1) continue;
					t = f[!swt][k] + (k != j);
					if (min > t) min = t;
				}
				if (min == 10000) min = -1;
				f[swt][j] = min;
			}
		}
	}
	

	ret = 10000;
	for (i =0; i < S; i++)
		if (f[swt][i]!= -1 && ret > f[swt][i]) 
			ret = f[swt][i];
	

	map1.clear();
	return ret;
}


int main()
{
	int T;
	
	//freopen("small.in", "r", stdin);

	scanf("%d", &T);

	for (int i = 1; i <= T; i++){
		printf("Case #%d: %d\n", i, work());
	}

	return 0;
}