#include <cstdio>

char dict[6000][50];
int main(void)
{
	int l,d,n,i,k;
	char token[10000];

	scanf("%d%d%d",&l,&d,&n);
	for (i=0; i<d; i++)
	{
		scanf("%s",dict[i]);
	}
	for (int j=0; j<n; j++)
	{
		k=0;
		scanf("%s",token);
		for (int t=0; t<d; t++)
		{
			int ind=0;
			bool abc = true;
			for (int r=0; token[r]; r++)
		   	{
				bool xyz = false;
				if (token[r] == '(') 
				{
					while (token[++r] != ')') 
					{
						if (token[r] == dict[t][ind]) 
						{
							xyz = true;
						}
					}
				} 
				else 
				{
					if (token[r] == dict[t][ind])
					{
						xyz = true;
					}
				}
				if (xyz == false) 
				{
					abc = false;
				}
				++ind;
			}	
			if (abc == true) 
			{
				k++;
			}
		}
		printf("Case #%d: %d\n",j+1,k);
	}
	return 0;
}
