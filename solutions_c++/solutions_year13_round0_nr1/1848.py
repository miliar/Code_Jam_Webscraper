#include <iostream>
#include <string.h>
#include <fstream.h>
#include <algorithm>
#include<stdio.h>

using namespace std;

int main ()
{
ifstream file1;
ofstream file2;
file1.open("inp4.txt",ios::in);
file2.open("output4.txt");
int t;
file1>>t;
int cnt=t;
string str[4];
while (t)
{
	int flagx=0;
	int flago=0;
	int flagbrk=0;
	file1>>str[0];
	file1>>str[1];
	file1>>str[2];
	file1>>str[3];
	for (int i=0;i<4;++i)
	    {
             for (int j=0;j<4;++j)
                 {
               //  file2<<str[i][j]<<"\t";
                  }
            //      file2<<endl;
         }
	for (int i=0;i<4;++i) {
		for (int j=0;j<4;++j)
		{
			if (str[i][j]=='X')
			{ 
				flagx+=1;
			}
			else if (str[i][j]=='O')
			{
				flago+=1;
			}
			else if (str[i][j]=='T')
			{
				flagx+=1;
				flago+=1;
			}
		}
		if (flagx==4)
		{
			file2<<"Case #"<<cnt-t+1<<": X won\n";
			flagx=0;
			flago=0;
			flagbrk=1;
			break;
		}
		if (flago==4)
		{
			file2<<"Case #"<<cnt-t+1<<": O won\n";
			flagx=0;
			flago=0;
			flagbrk=1;
			break;
		}
			flagx=0;
			flago=0;
	}
if (flagbrk==0)
{
	for (int i=0;i<4;++i) {
		for (int j=0;j<4;++j)
		{
			if (str[j][i]=='X')
			{
				flagx+=1;
			}
			if (str[j][i]=='O')
			{
				flago+=1;
			}
			if (str[j][i]=='T')
			{
				flagx+=1;
				flago+=1;
			}
		}
		if (flagx==4)
		{
			file2<<"Case #"<<cnt-t+1<<": X won\n";
			flagx=0;
			flago=0;
			flagbrk=1;
			break;
		}
		if (flago==4)
		{
			file2<<"Case #"<<cnt-t+1<<": O won\n";
			flagx=0;
			flago=0;
			flagbrk=1;
			break;
		}
		flagx=0;
		flago=0;
	}
}
flago=0;
flagx=0;
if (flagbrk==0)
{
	for (int i=0; i<4;++i)
	{
		if (str[i][i]=='X')
		{
			flagx+=1;
		}
		if (str[i][i]=='O')
		{
			flago+=1;
		}
		if (str[i][i]=='T')
		{
			flagx+=1;
			flago+=1;
		}
	}
		if (flagx==4)
		{
			file2<<"Case #"<<cnt-t+1<<": X won\n";
			flagx=0;
			flago=0;
			flagbrk=1;
		}
		if (flago==4)
		{
			file2<<"Case #"<<cnt-t+1<<": O won\n";
			flagx=0;
			flago=0;
			flagbrk=1;
		}
		flagx=0;
		flago=0;

}
flagx=0;
flago=0;
if (flagbrk==0)
{
	for (int i=0; i<4;++i)
	{
		if (str[i][3-i]=='X')
		{
			flagx+=1;
		}
		if (str[i][3-i]=='O')
		{
			flago+=1;
		}
		if (str[i][3-i]=='T')
		{
			flagx+=1;
			flago+=1;
		}
		
	}
	if (flagx==4)
		{
			file2<<"Case #"<<cnt-t+1<<": X won\n";
			flagx=0;
			flago=0;
			flagbrk=1;
		}
		if (flago==4)
		{
			file2<<"Case #"<<cnt-t+1<<": O won\n";
			flagx=0;
			flago=0;
			flagbrk=1;
		}
		flagx=0;
		flago=0;

}

if (flagbrk==0)
{
	for (int i=0;i<4;++i)
	{
		for (int j=0;j<4;++j)
		{
			if (str[i][j]=='.')
			{
			file2<<"Case #"<<cnt-t+1<<": Game has not completed\n";
			flagbrk=1;
			break;
			}
		}
		if (flagbrk==1)
		{
			break;
		}
	}
}

if (flagbrk==0)
{
	file2<<"Case #"<<cnt-t+1<<": Draw\n";
}
	t--;
}
file1.close();
	return 0;
} 
