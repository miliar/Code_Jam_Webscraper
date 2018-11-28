#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;
char A[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
FILE *fp;
char *line = NULL;
size_t len = 0;int t=0,i=0;
ssize_t read = 0;
int cas =1;
//	fp = fopen("input","r");
//	if (fp == NULL)
  //             exit(EXIT_FAILURE);
	cin>>t;
	//cout << t;
           read = getline(&line, &len, stdin);
	while(t--)
	{
           read = getline(&line, &len, stdin);
		cout<<"Case #"<<cas<<": ";
		cas++;
           for(i=0;i<read;i++)
		{
			if(line[i]>='a'&&line[i]<='z')
				cout<<A[line[i]-'a'];
			else
				cout<<line[i];
		}
	}
}
