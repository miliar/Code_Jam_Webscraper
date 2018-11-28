#include<iostream>
#include<conio.h>
#include<sstream>
#include<string>

using namespace std;
void main()
{
	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
	int t;
	string message;
	cin>>t;
	getline(cin,message);
	for(int i=0;i<t;i++)
	{
		char outputmessage[110];
		cout<<"Case #"<<i+1<<": ";
		getline(cin,message);
		for(int j=0;j<message.length();j++)
		{
			switch(message[j])
			{
			case 'y':
				outputmessage[j]='a';
				break;
			case 'n':
				outputmessage[j]='b';
				break;
			case 'f':
				outputmessage[j]='c';
				break;
			case 'i':
				outputmessage[j]='d';
				break;
			case 'c':
				outputmessage[j]='e';
				break;
			case 'w':
				outputmessage[j]='f';
				break;
			case 'l':
				outputmessage[j]='g';
				break;
			case 'b':
				outputmessage[j]='h';
				break;
			case 'k':
				outputmessage[j]='i';
				break;
			case 'u':
				outputmessage[j]='j';
				break;
			case 'o':
				outputmessage[j]='k';
				break;
			case 'm':
				outputmessage[j]='l';
				break;
			case 'x':
				outputmessage[j]='m';
				break;
			case 's':
				outputmessage[j]='n';
				break;
			case 'e':
				outputmessage[j]='o';
				break;
			case 'v':
				outputmessage[j]='p';
				break;
			case 'z':
				outputmessage[j]='q';
				break;
			case 'p':
				outputmessage[j]='r';
				break;
			case 'd':
				outputmessage[j]='s';
				break;
			case 'r':
				outputmessage[j]='t';
				break;
			case 'j':
				outputmessage[j]='u';
				break;
			case 'g':
				outputmessage[j]='v';
				break;
			case 't':
				outputmessage[j]='w';
				break;
			case 'h':
				outputmessage[j]='x';
				break;
			case 'a':
				outputmessage[j]='y';
				break;
			case 'q':
				outputmessage[j]='z';
				break;
			case ' ':
				outputmessage[j]=' ';
				break;
		}
			
	}
		outputmessage[message.length () ]='\0';
		cout<<outputmessage;
		cout<<"\n";
				
}
}