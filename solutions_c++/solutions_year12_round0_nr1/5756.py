#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main(int argc, char **argv)
{
	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");
	int n;
	char arr[1000];
	in>>n;
	in.getline(arr,1000);
	for(int j=0;j<n;j++)
	{
		in.getline(arr,1000);
		int length=strlen(arr);
		for(int i=0;i<length;i++)
		{
			if(arr[i]=='y')
				arr[i]='a';
			else if(arr[i]=='n')
				arr[i]='b';
			else if(arr[i]=='f')
				arr[i]='c';
			else if(arr[i]=='i')
				arr[i]='d';
			else if(arr[i]=='c')
				arr[i]='e';
			else if(arr[i]=='w')
				arr[i]='f';
			else if(arr[i]=='l')
				arr[i]='g';
			else if(arr[i]=='b')
				arr[i]='h';
			else if(arr[i]=='k')
				arr[i]='i';
			else if(arr[i]=='u')
				arr[i]='j';
			else if(arr[i]=='o')
				arr[i]='k';
			else if(arr[i]=='m')
				arr[i]='l';
			else if(arr[i]=='x')
				arr[i]='m';
			else if(arr[i]=='s')
				arr[i]='n';
			else if(arr[i]=='e')
				arr[i]='o';
			else if(arr[i]=='v')
				arr[i]='p';
			else if(arr[i]=='z')
				arr[i]='q';
			else if(arr[i]=='p')
				arr[i]='r';
			else if(arr[i]=='d')
				arr[i]='s';
			else if(arr[i]=='r')
				arr[i]='t';
			else if(arr[i]=='j')
				arr[i]='u';
			else if(arr[i]=='g')
				arr[i]='v';
			else if(arr[i]=='t')
				arr[i]='w';
			else if(arr[i]=='h')
				arr[i]='x';
			else if(arr[i]=='a')
				arr[i]='y';
			else if(arr[i]=='q')
				arr[i]='z';
		}
		out<<"Case #";
		out<<j+1;
		out<<": ";
		out<<arr;
		out<<"\n";
	}
	in.close();
	out.close();
	return 0;
}

