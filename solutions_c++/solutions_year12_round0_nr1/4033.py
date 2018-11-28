#include<iostream>
#include<cstdio>
using namespace std;

#define MAX 101

int main()
{
	char a[MAX];
	int t;
	scanf("%d",&t);
	getchar();
	for(int j=1;j<=t;j++)
	{	printf("Case #%d: ",j);
		cin.getline(a,101);
		//scanf("%[]",a);
		int i=0;
		while(a[i])
		{
			switch(a[i])
			{
				case 'a':
						putchar('y');
					break;
				case 'b':
						putchar('h');
					break;
				case 'c':
						putchar('e');
					break;
				case 'd':
						putchar('s');
					break;
				case 'e':
						putchar('o');
					break;
				case 'f':
						putchar('c');
					break;
				case 'g':
						putchar('v');
					break;
				case 'h':
						putchar('x');
					break;
				case 'i':
						putchar('d');
					break;
				case 'j':
						putchar('u');
					break;
				case 'k':
						putchar('i');
					break;
				case 'l':
						putchar('g');
					break;
				case 'm':
						putchar('l');
					break;
				case 'n':
						putchar('b');
					break;
				case 'o':
						putchar('k');
					break;
				case 'p':
						putchar('r');
					break;
				case 'q':
						putchar('z');
					break;
				case 'r':
						putchar('t');
					break;
				case 's':
						putchar('n');
					break;
				case 't':
						putchar('w');
					break;
				case 'u':
						putchar('j');
					break;

				case 'v':
						putchar('p');
					break;

				case 'w':
						putchar('f');
					break;

				case 'x':
						putchar('m');
					break;

				case 'y':
						putchar('a');
					break;

				case 'z':
						putchar('q');
					break;

				case ' ':
						putchar(' ');
					break;

				default :
						putchar(a[i]);
			
			}

			i++;
		}
			putchar('\n');
		
	}
return 0;
}
