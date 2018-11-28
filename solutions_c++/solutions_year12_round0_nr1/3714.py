#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>

using namespace std;

const int maxn = 1000;
int numbers[maxn];
int n;
string line;


void read() {
//	scanf("%d",&n);
//printf("n:%d\n",n);
//	for (int i=0;i<n;i++)
//	{
//		scanf("%d", &numbers[i]);	
//printf("i:%d numbers[i]:%d\n",i,numbers[i]);
//	}

	getline(cin,line);
}

int main()
{
	int i,t;
	int k;
	int outoforder;
	scanf("%d",&t);
	getline(cin,line);
	for(i = 1; i<=t; i++)
	{
		printf("Case #%d: ", i);
		read();
		for(k=0;k<line.length();k++)
		{
			switch(line[k])
			{
				case 'a':
				cout<<"y"; break;
				case 'b':
				cout<<"h"; break;
				case 'c':
				cout<<"e"; break;
				case 'd':
				cout<<"s"; break;
				case 'e':
				cout<<"o"; break;
				case 'f':
				cout<<"c"; break;
				case 'g':
				cout<<"v"; break;
				case 'h':
				cout<<"x"; break;
				case 'i':
				cout<<"d"; break;
				case 'j':
				cout<<"u"; break;
				case 'k':
				cout<<"i"; break;
				case 'l':
				cout<<"g"; break;
				case 'm':
				cout<<"l"; break;
				case 'n':
				cout<<"b"; break;
				case 'o':
				cout<<"k"; break;
				case 'p':
				cout<<"r"; break;
				case 'q':
				cout<<"z"; break;
				case 'r':
				cout<<"t"; break;
				case 's':
				cout<<"n"; break;
				case 't':
				cout<<"w"; break;
				case 'u':
				cout<<"j"; break;
				case 'v':
				cout<<"p"; break;
				case 'w':
				cout<<"f"; break;
				case 'x':
				cout<<"m"; break;
				case 'y':
				cout<<"a"; break;
				case 'z':
				cout<<"q"; break;
				
				default:
				cout<<line[k];
			}
		}
		//cout<<line;

		printf("\n");
	}
	return 0;
}
