#include<stdio.h>
#include<stdlib.h>
#include<string.h>

bool contains(char word,char *list,int size)
{
for(int i=0;i<size;i++)
	if(word==list[i])
	return true;

return false;
}


main()
{
	int L,D,N;
	scanf("%d%d%d",&L,&D,&N);

	char **array=new char* [D];

	for(int i=0;i<D;i++)
		{array[i]=new char[L];scanf("%s",array[i]);}

	for(int test_case=0;test_case<N;test_case++)
	{char pattern[400];

	 char **list=new char* [L];
		for(int i=0;i<L;i++)
		list[i]=new char[26];
		
	 int *list_count=new int[L];
	 scanf("%s",pattern);
	 int counter=0,list_no=-1;
	 bool create_new_list=true;
		
		while(counter<strlen(pattern))
		{
		 if(create_new_list==true)
			{
			 list_no++;
			 if(pattern[counter]=='(')
				{create_new_list=false;counter++;list_count[list_no]=0;continue;}
			 else
				{list_count[list_no]++;list[list_no][0]=pattern[counter];counter++;continue;}
			}

		 else
			{
			if(pattern[counter]==')')
				{create_new_list=true;counter++;continue;}
			else
				{list[list_no][list_count[list_no]]=pattern[counter];list_count[list_no]++;counter++;continue;}
			}
		}

	int match=0;
	for(int i=0;i<D;i++)
		{int k;
			for(k=0;k<L;k++)
			{if(contains(array[i][k],list[k],list_count[k]))
				continue;
			 else
				break;
			}
		 if(k==L) match++;
		}

	printf("Case #%d: %d\n",test_case+1,match);
	}

return 0;
}
		
