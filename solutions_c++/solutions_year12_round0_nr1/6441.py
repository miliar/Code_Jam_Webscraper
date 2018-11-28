#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


using namespace std;

int main()
{
	char b[100] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char a[100] = "our language is impossible to understand";
	int l = strlen(a);

	int i;
	int map[30];
	for(i=1; i<=26; i++)
	{
		map[i]=0;
	}

	int temp1, temp2;
	for(i=0; i<l; i++)
	{
		if(a[i]!=' ')
		{

			temp1 = int(b[i]-97+1);
			temp2 = int(a[i]-97+1);
			if(map[temp1]!=0 && map[temp1]!=temp2)
			{
				cout<<"1: clash occured at index "<<temp1<<endl;
				cout<<temp2<<" != "<<map[temp1]<<endl<<endl;
			}
			map[temp1] = temp2;
		}

		//cout<<int(a[i]-97+1)<<"\t"<<int(b[i]-97+1)<<endl;
	}

	char b1[100] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char a1[100] = "there are twenty six factorial possibilities";
	l = strlen(a1);

	for(i=0; i<l; i++)
	{
		if(a1[i]!=' ')
		{

			temp1 = int(b1[i]-97+1);
			temp2 = int(a1[i]-97+1);
			if(map[temp1]!=0 && map[temp1]!=temp2)
			{
				cout<<"2: clash occured at index "<<temp1<<endl;
				cout<<temp2<<" != "<<map[temp1]<<endl<<endl;
			}
			map[temp1] = temp2;
		}

		//cout<<int(a[i]-97+1)<<"\t"<<int(b[i]-97+1)<<endl;
	}

	char b2[100] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	char a2[100] = "so it is okay if you want to just give up";
	l = strlen(a2);
	for(i=0; i<l; i++)
	{
		if(a2[i]!=' ')
		{

			temp1 = int(b2[i]-97+1);
			temp2 = int(a2[i]-97+1);
			if(map[temp1]!=0 && map[temp1]!=temp2)
			{
				cout<<"clash occured at index "<<temp1<<endl;
				cout<<temp2<<" != "<<map[temp1]<<endl<<endl;
			}
			map[temp1] = temp2;
		}

		//cout<<int(a[i]-97+1)<<"\t"<<int(b[i]-97+1)<<endl;
	}

	map[17] = 26;
	map[26] = 17;

	int t;
	char input[300];
	scanf("%d\n", &t);
	int t1=t;
	while(t>0)
	{
		//scanf("%[a-z]", input);
		gets(input);
		//cout<<input;
		l = strlen(input);

		printf("Case #%d: ", t1-t+1);
		for(i=0; i<l; i++)
		{
			if(input[i]==' ')
				printf(" ");
			else
			{
				temp1 = int(input[i]-97+1);
				temp2 = map[temp1]+96;
				printf("%c",(char)temp2);
			}
		}
		printf("\n");
		t--;
	}
/*
	for(i=1; i<=26; i++)
	{
		cout<<i<<"\t"<<map[i]<<endl;
	}*/
	return 0;
}
