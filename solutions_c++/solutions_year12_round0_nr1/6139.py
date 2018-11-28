#include<stdio.h>
#include<stdlib.h>
#include<string.h>



using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

      
	int n;
    char str[200];
    char str1[200];
    
	scanf("%d",&n);
	getchar();

	for(int i = 1 ; i <= n ; ++i)
	{
		
		gets(str);
	    int k = strlen(str);
	   
		for(int j = 0;j < k; j++)
		{
		   switch(str[j])
		   {
			case 'a':str1[j]='y';break;
			case 'b':str1[j]='h';break;
			case 'c':str1[j]='e';break;
			case 'd':str1[j]='s';break;
			case 'e':str1[j]='o';break;
			case 'f':str1[j]='c';break;
			case 'g':str1[j]='v';break;
			case 'h':str1[j]='x';break;
			case 'i':str1[j]='d';break;
			case 'j':str1[j]='u';break;
			case 'k':str1[j]='i';break;
			case 'l':str1[j]='g';break;
			case 'm':str1[j]='l';break;
			case 'n':str1[j]='b';break;
			case 'o':str1[j]='k';break;
			case 'p':str1[j]='r';break;
			case 'q':str1[j]='z';break;
			case 'r':str1[j]='t';break;
			case 's':str1[j]='n';break;
			case 't':str1[j]='w';break;
			case 'u':str1[j]='j';break;
			case 'v':str1[j]='p';break;
			case 'w':str1[j]='f';break;
			case 'x':str1[j]='m';break;
		    case 'y':str1[j]='a';break;
			case 'z':str1[j]='q';break;
			case ' ':str1[j]=' ';break;
		   }
		}
		    str1[k]='\0';
			printf("Case #%d: %s\n", i, str1);
	    
	}


}
