#include <iostream>
#include <algorithm>
using namespace std;
char str[2000];
char p[2000];
int List[20];
int Path[20];
int k , length , Min ;
void solve()
{
	int i,j;
	int cnt = 0 ;
	int l = strlen(str);
	int s = 0 ;
	for(i = 0 ; i < l ;)
	{
		for(j = 0 ; j < length ; j ++)
			p[i++] = str[List[j]-1+s];
		s += k ;
	}
	for(i = 0 ; i < l ;)
	{
		j = i ;
		while( j+1 < l && p[j] == p[j+1])
			j ++ ;
		j ++ ;
		i = j ;
		cnt ++ ;
	}
	if(Min == -1 || cnt < Min)
		Min = cnt ;
}
void dfs()
{
	int i;
	if(length == k){
		solve();
		return ;
	}
	for(i = 1 ; i <= k ; i ++){
		if(Path[i])
			continue ;
		Path[i] = 1 ;
		List[length ++] = i ;
		dfs();
		length -- ;
		Path[i] = 0 ;
	}
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int test , t = 1 ;
	scanf("%d" , &test ) ;
	while( test -- )
	{
		scanf("%d",&k);
		scanf("%s",str);
		memset(Path,0,sizeof(Path));
		length = 0 ;
		Min = -1 ;
		dfs();
		printf("Case #%d: %d\n",t++,Min );
	}
	return 0;
}