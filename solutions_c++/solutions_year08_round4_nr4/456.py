//////////
//
//	Auther: hazy
//	Pro ID:	
//	Pro Profile:  
//	Attention!!: 	
//	Created @ 2008_8
//
//////////
#include <stdio.h>
#include <string.h>

#include <vector>

#include <iostream>
#include <utility>
#include <algorithm>

typedef 	long long 	i64;
using namespace std;
const int MAXN = 100;

int 	cas, T = 0;
int 	K;
char 	txt[1010];	// K <= 5;
	char 	str[1010];

int 	MI;
int 	cnt = 0;
int 	per[100];

int 	Run()
{

	int		i, j;
	int 	len = strlen(txt);
	
	//memcpy(str, txt, sizeof(str));
	memset(str, 0, sizeof(str));
	for (i=0; i<len; i+=K)
	{
		for (j=0; j<K; j++)
			str[i + j] = txt[i + per[j]];
	}
	
//	printf("S = %s\n", str);
	
	int 	rnt = 0;
	char 	pre = 0;
	
	for (i=0; i<len; i++)
	{
		if (str[i] != pre)
		{
			rnt++;
		}
		pre = str[i];
	}
	return rnt;
}

void Perm(int p[], int k, int m)
{
	int 	i;
	if (k == m) 
	{
	/*
		cnt++;
		for (i = 0; i <= m; i++) 
	  	{
   			printf(" %d", p[i]);
        }	
        cout << endl;*/
		///////////
		
		MI <?= Run();
 	}
  	else  
  	{
  		for (i = k; i <= m; i++) 
	  	{
    		swap(p[k], p[i]);
            Perm(p, k+1, m);
            swap(p[k], p[i]);
        }
  	}
}


int main()
{
	int 	i, j,k;
	
	freopen("D-small-attempt1.in", "r", stdin);
		freopen("d_small111111.out", "w", stdout);
	
	
	for (scanf("%d", &cas); cas; cas--)
	{
		scanf("%d %s", &K, txt);
		for (i=0; i<K; i++)	per[i] = i;
		
		MI = 1 << 26;
		Perm(per, 0, K-1);	
		printf("Case #%d: %d\n", ++T, MI);
		
		//printf("cnt = %d\n", cnt);
	}
	return 0;
}
