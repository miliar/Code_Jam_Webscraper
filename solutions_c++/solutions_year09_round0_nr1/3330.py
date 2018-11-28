#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("A-small-attempt3.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	char word[25][20];
	int L,D,N;
	int test,l,d;
	scanf("%d %d %d",&L,&D,&N);
		int ans;
		for(d=0;d<D;d++){
				scanf("%s",&word[d]);
		}
		int count[25];
		char buf;
		int i,m,n;
		char word2[1000];
		for(i=0;i<25;i++)
			count[i]=0;
	for(test=1;test<=N;test++) {	
		scanf("%s",word2);
		m=0;
		ans=0;
		for(i=0;i<25;i++)
			count[i]=0;		
		i=0;
		do{
			if(word2[m]=='(')
			{
				m++;
				while(word2[m]!=')')
				{
					for(n=0;n<D;n++)
					{
						if(word2[m]==word[n][i])
						{
							count[n]++;
						}
					}
					m++;
				}
				if(word2[m]==')')
					m++;
				i++;
			}
			else 
			{
				for(n=0;n<D;n++)
					{
						if(word2[m]==word[n][i])
						{
							count[n]++;
						}
					}
				i++;m++;
			}
			}while(i<=L);
		for(i=0;i<D;i++)
		{
			if(count[i]>L)
				ans++;
		}
		printf("Case #%d: %d\n", test, ans);
	}

	exit(0);
}