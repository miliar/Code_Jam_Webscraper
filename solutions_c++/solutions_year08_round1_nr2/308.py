#include<stdio.h>
#include<string.h>

int mm[102][12] , ret , ch , n , m;

bool check(int k){
	int i , j , l;
	bool flag[112];
	memset(flag , false , sizeof(flag));
	for(i = 0;i<n;i++){
		l = (k&(1<<i))>0;
		ch += l;
		for(j = 0;j<m;j++)
			if(mm[j][i] == l)
				flag[j] = true;
	}
	for(i = 0;i<m;i++)
		if(!flag[i])
			return false;
	return true;
}

int main()
{
	freopen("b.in" , "r" , stdin);
	freopen("b.out" , "w" , stdout);
	int test , i , j , k , kase = 1 , a;
	scanf("%d" , &test);
	while(test--)
	{
		scanf("%d%d" , &n , &m);
		memset(mm , -1 , sizeof(mm));
		for(i = 0;i<m;i++){
			scanf("%d" , &a);
			while(a--)
			{
				scanf("%d%d" , &j ,&k);
				mm[i][j-1] = k;
			}
		}
		ret = (1<<10);
		k = -1;
		for(i = 0;i<(1<<n);i++){
			ch = 0;
			if(check(i) && ch < ret){
				ret = ch;
				k = i;
			}
		}
		printf("Case #%d:" , kase++);
		if(k == -1){
			printf(" IMPOSSIBLE\n");
			continue;
		}
		for(i = 0;i<n;i++)
			printf(" %d" , (k&(1<<i)) > 0);
		printf("\n");
	}
	return 0;
}
