#include<iostream>
#include<string>
using namespace std;
char str[5005][20];
bool s[30][3000];
char w[100024];

int len;
void work()
{
	memset(s , 0 , sizeof(s));
	int i = 0;
	len = 0;
	while(w[i] != '\0')
	{
		if(w[i] == '(')
		{
			while(w[i] != ')')
			{
				if(w[i] >= 'a' && w[i] <= 'z')
				{
					s[w[i] - 'a'][len] = 1;
					
				}
				i++;
			}
			len++;
		}
		else
		{
			if(w[i]>='a' && w[i]<='z')
			{
				s[w[i] - 'a'][len] = 1;
				len++;
			}
			i++;
		}
	}
}
int main()
{
	freopen("A-large.in" , "r" , stdin);
	freopen("ans.out" , "w" , stdout);
	int L , D , N;
	while(3 == scanf("%d%d%d" , &L , &D , &N))
	{
		int i , j , k;
		for(i = 0 ; i < D; i++)
		{
			scanf("%s" , str[i]);
		}
		for(i = 0 ; i < N ; i++)
		{
			scanf("%s" , w);
			work();
			int ans = 0;
			for(j = 0 ; j < D ; j++)
			{
				int l = strlen(str[j]);
				for(k= 0 ; k < l ; k++)
				{
					if(!s[str[j][k] - 'a'][k])
						break;
				}
				if(k==l)
					ans++;
			}
			printf("Case #%d: %d\n",i+1,ans);
		}

	}
	return 0;
}