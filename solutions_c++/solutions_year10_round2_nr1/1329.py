#include <cstdio>
#include <cstring>
typedef struct _s{
	_s* tab[1000];
	char name[201];
} folder;
bool is_f(folder* f, char *name)
{
	if(strcmp(f->name, name)==0) return true;
	
	return true;
};
int main()
{
	int z,w,y,t,n,m,k,i,j,a,b;
	char c;
	char str[201],str1[201],str2[201];
	char tab[1001][201];
	scanf("%d", &t);
	tab[1][0]='/';
	for(z=1;z<=t;z++)
	{
		k=0;
		scanf("%d %d", &n, &m);
		for(y=1;y<=n;y++)
		{
			scanf("%s", str);
			strcpy(tab[y],str);
		}
		for(w=1;w<=m;w++)
		{
			scanf("%s", str);
	
				for(i=1;i<strlen(str);i++)
				{
					//printf("ok3\n");
					if(str[i]=='/') 
					{
						str[i]=0;
						strcpy(str1,str);
						str[i]='/'; //sciezka poczatkowa
							for(j=1;j<=n;j++)
							{
								if(strcmp(str1, tab[j])==0)
								{
									break;
								}
							}
							if(strcmp(str1, tab[j])!=0 || n==0)
							{
								k++;
								strcpy(tab[n+1],str1);
								n++;
							}	
							//printf("ok2\n");
					}
				}	
								
				for(i=1;i<=n;i++)
				{
					if(strcmp(str, tab[i])==0)
					{
						break;
					}
				}
				if(strcmp(str, tab[i])!=0 || n==0)
				{
					k++;
					strcpy(tab[n+1],str);
					n++;
				}		
				
				
			 //printf("ok\n");
				
		}
			
		printf("Case #%d: %d\n",z,k);
	}	
	return 0;
}

