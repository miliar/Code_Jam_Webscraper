#include<stdio.h>
#include<stdlib.h>
#include<string.h>


void sortback(char *arr,int index)
{
	for(int i=index+1;i<20;i++)
	for(int j=i+1;j<20;j++)
		{
		 if(arr[i]>arr[j])
			{char temp=arr[i];
			 arr[i]=arr[j];
			 arr[j]=temp;}
		}
}


main()
{
int test_case;
scanf("%d",&test_case);
	for(int i=0;i<test_case;i++)
	{char array[20]={'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'};
		char *string=new char[25];	 	
		scanf("%s",string);
		int length=strlen(string);

	for(int j=19;j>19-length;j--)
		array[j]=string[length-(19-j)-1];

		for(int j=18;j>=0;j--)
		for(int k=19;k>j;k--)
		{if(array[k]>array[j])
			{char temp=array[j];
			 array[j]=array[k];
			 array[k]=temp;
			 sortback(array,j);
			 j=-1;break;}
	 	else
			continue;
		}
		printf("Case #%d: ",i+1);
		bool flag=true;
		for(int j=0;j<20;j++)
		{if(array[j]=='0' && flag)
			continue;
		 flag=false;
		 printf("%c",array[j]);}
	printf("\n");
	}
}
