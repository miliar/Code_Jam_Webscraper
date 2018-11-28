#include<stdio.h>
#include<stdlib.h>

void replace(char **map_array,char a,char b,int row,int col)
{
	for(int i=0;i<row;i++)
	for(int j=0;j<col;j++)
	if(map_array[i][j]==a)
		map_array[i][j]=b;
}


void label(int m,int n,int **array,char **map_array,int row,int col,int &count)
{
	int smallest_height=array[m][n],new_m,new_n;
		if(m>0 && smallest_height>array[m-1][n])
		{smallest_height=array[m-1][n],new_m=m-1,new_n=n;}

		if(n>0 && smallest_height>array[m][n-1])
		{smallest_height=array[m][n-1],new_m=m,new_n=n-1;}

		if(n<col-1 && smallest_height>array[m][n+1])
		{smallest_height=array[m][n+1],new_m=m,new_n=n+1;}

		if(m<row-1 && smallest_height>array[m+1][n])
		{smallest_height=array[m+1][n],new_m=m+1,new_n=n;}

	if(smallest_height==array[m][n])
	{count++;return;}

	if(map_array[new_m][new_n]=='.')
	{map_array[new_m][new_n]=97+count;label(new_m,new_n,array,map_array,row,col,count);}
	else
	{replace(map_array,97+count,map_array[new_m][new_n],row,col);return;}
}

	
main()
{
	int no_test_case;
	scanf("%d",&no_test_case);
	for(int i=0;i<no_test_case;i++)
	{
		int row,col,count=0;
		scanf("%d%d",&row,&col);

		int **array=new int* [row];
		for(int m=0;m<row;m++)
		{array[m]=new int[col];
		 for(int n=0;n<col;n++)
		 scanf("%d",&array[m][n]);}

		char **map_array=new char*[row];
		for(int m=0;m<row;m++)
		{map_array[m]=new char[col];
		 for(int n=0;n<col;n++)
		 map_array[m][n]='.';}

		 for(int m=0;m<row;m++)
		 for(int n=0;n<col;n++)
		 {
		  if(map_array[m][n]!='.')
			continue;
		  map_array[m][n]=97+count;
		  label(m,n,array,map_array,row,col,count);
		 }

		printf("Case #%d:\n",i+1);
		for(int m=0;m<row;m++)
		{for(int n=0;n<col;n++)
		 printf("%c ",map_array[m][n]);
		 printf("\n");}
	}
return 0;
}
