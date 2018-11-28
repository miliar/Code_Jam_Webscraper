#include <cstdio>
#include <string.h>

int main()
{
	int result[20];
	int case_count;
	scanf("%d\r\n", &case_count);
	
	for(int i=0;i<case_count;i++)
	{
		char engines[100][100];
		char querys[1000][100];

		int name_count;
		scanf("%d\r\n",&name_count);
		for(int x=0;x<name_count;x++)
			gets(engines[x]);

		int query_count;
		scanf("%d\r\n",&query_count);
		for(int x=0;x<query_count;x++)
			gets(querys[x]);

		int change_count = 0;
		char* current_engine = NULL;
		for(int x=0;x<query_count;x++)
		{	
			if(current_engine == NULL 
				|| (current_engine != NULL && strcmp(current_engine,querys[x])==0))
			{
				if(current_engine != NULL)
					change_count++;

				int max_pass = 0;
				for(int y=0;y<name_count;y++)
				{
					int pass = 0;
					char* last = NULL;
					for(int z=x;z<query_count;z++)
					{
						if(strcmp(engines[y] , querys[z]) != 0)
						{
							if(last == NULL || (last != NULL && strcmp(last , querys[z]) != 0))
								pass++;
						}
						else
							break;
					}

					if(max_pass <= pass)
					{
						current_engine = engines[y];
						max_pass = pass;
					}
				}
			}
		}
		
		result[i] = change_count;
	}

	for(int i=0;i<case_count;i++)
		printf("Case #%d: %d\r\n",i+1,result[i]);

	return 0;
}