
#include <fstream> 
using namespace std;
char a[26];
void init()
{
a[0]='y';
a[1]='h';
a[2]='e';
a[3]='s';
a[4]='o';
a[5]='c';
a[6]='v';
a[7]='x';
a[8]='d';
a[9]='u';
a[10]='i';
a[11]='g';
a[12]='l';
a[13]='b';
a[14]='k';
a[15]='r';
a[16]='z';
a[17]='t';
a[18]='n';
a[19]='w';
a[20]='j';
a[21]='p';
a[22]='f';
a[23]='m';
a[24]='a';
a[25]='q';

}

void convert(char *input,char *output)
{
	int i=0;
	for(i=0;input[i]!='\0';i++)
	{
		if(input[i]!=' ')
		{
			output[i]=a[input[i]-'a'];
		}
		else
		{
			output[i]=' ';
		}
	}
	output[i]='\0';
}
int main()
{
	init();
	ifstream obj("input.txt");
	ofstream obj2("output.txt");
	char buffer[102];
	int testcases;
	//obj>>testcases;
	obj.getline(buffer,102);
	testcases=atoi(buffer);
	char buffer2[102];
	for(int i=0;i<testcases;i++)
	{
		obj.getline(buffer,102);
		convert(buffer,buffer2);
		obj2<<"Case #"<<i+1<<": ";
		obj2<<buffer2;
		obj2<<endl;
	}
	return 0;
}

