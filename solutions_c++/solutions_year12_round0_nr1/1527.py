#include<stdio.h>
#include<string.h>
#include<iostream>

using namespace std;

int main()
{
	char input1[50] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	char input2[50] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	char input3[50] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	
	char output1[50] = "our language is impossible to understand";
	char output2[50] = "there are twenty six factorial possibilities";
	char output3[50] = "so it is okay if you want to just give up";
	char G[102];
	
	int noc;
	char hash[27], ch;
	int i, count=0;
	
	for(i=0; i<27; i++)
	{
		hash[i] = '$';
	}
	
	for(i=0; input1[i]!='\0'; i++)
	{
		ch = input1[i];
		if(ch == ' ')
			hash[26] = output1[i];
		else
			hash[ch-'a'] = output1[i]; 
	}
	for(i=0; input2[i]!='\0'; i++)
	{
		ch = input2[i];
		if(ch == ' ')
			hash[26] = output2[i];
		else
			hash[ch-'a'] = output2[i]; 
	}
	for(i=0; input3[i]!='\0'; i++)
	{
		ch = input3[i];
		if(ch == ' ')
			hash[26] = output3[i];
		else
			hash[ch-'a'] = output3[i]; 
	}
	
	hash[25] = 'q';
	
	for(i=0; i<27; i++)
	{
		if(hash[i] == '$')
			hash[i] = 'z';
		//cout<<hash[i];
	}
	
	scanf("%d", &noc);
	getchar();
	while(noc--)
	{
		count++;
		gets(G);
		cout<<"Case #"<<count<<": ";
		for(i=0; G[i]!='\0'; i++)
		{
			if(G[i] == ' ')
				printf(" ");
			else
				printf("%c", hash[G[i]-'a']);
		}
		printf("\n");
	}
	return 0;
}