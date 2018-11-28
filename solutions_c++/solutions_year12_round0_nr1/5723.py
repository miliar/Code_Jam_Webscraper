#include<fstream.h>
#include<conio.h>
#include<string.h>
void main()
{
clrscr();
ifstream file;
file.open("input.txt");
char str[999],str1[999];
int ascii[200]={0};
while(!file.eof())
{
file.getline(str1,999);
file.getline(str,999);
for(int i=0;i<=strlen(str);i++)
	{
	ascii[int(str1[i])]=int(str[i]);
	}
}
ascii[122]=113;
ascii[113]=122;
file.close();
ifstream file2;
ofstream final;
final.open("final.txt",ios::trunc);
file2.open("input2.txt");
int p=1;
while(!file2.eof())
{
file2.getline(str1,999);
final<<"\n";
final<<"Case #"<<p<<": ";
p++;
for(int i=0;i<=strlen(str1);i++)
{
if(int(str1[i])<=122 && int(str1[i])>=97)
final<<char(ascii[str1[i]]);
else
final<<str1[i];
}
}
getch();
}