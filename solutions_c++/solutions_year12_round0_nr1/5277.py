#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int main()
{
	freopen("in.txt","rt",stdin);
    freopen("out.txt","wt",stdout);
	int t,j;
	cin>>t;
		getchar();
		for(j=1;j<=t;j++)
		{
			char st[200]={0};
			int i,len;
			
			gets(st);
		
			len=strlen(st);
			printf("Case #%d: ",j);
			for(i=0;i<len;i++)
			{
				switch(st[i])
				{
				case 'a':
					printf("y");
					break;
				case 'b': 
					printf("h");
					break;
				case 'c':
					printf("e");
					break;
				case 'd':
					printf("s");
					break;
				case 'e':
					printf("o");
					break;
				case 'f': 
					printf("c");
					break;
				case 'g':
					printf("v");
					break;
				case 'h':
					printf("x");
					break;
				case 'i':
					printf("d");
					break;
				case 'j':
					printf("u");
					break;
				case 'k':
					printf("i");
					break;
				case 'l': 
					printf("g");
					break;
				case 'm':
					printf("l");
					break;
				case 'n':
					printf("b");
					break;
				case 'o':
					printf("k");
					break;
				case 'p':
					printf("r");
					break;
				case 'q':            //////////q
					printf("z");
					break;
				case 'r':
					printf("t");
					break;
				case 's':
					printf("n");
					break;
				case 't':
					printf("w");
					break;
				case 'u':
					printf("j");
					break;
				case 'v': 
					printf("p");
					break;
				case 'w':
					printf("f");
					break;
				case 'x': 
					printf("m");
					break;
				case 'y':
					printf("a");
					break;
				case 'z':					//zzz
					printf("q");
					break;
				default:
					printf("%c",st[i]);
				}
			}
			printf("\n");
		}
	return 0;
	}
