#include <fstream>
#include <iostream>
using namespace std;

int no=0;

int searchsub(char *thestring,char *tosearch)
{
	int i,j,k;
	int count=0;
	char newstring[501]={0};
	char newtosearch[20]={0};
	if(strlen(tosearch)==0)
	{
		return 1;
	}
	if(strlen(thestring)<strlen(tosearch))
	{
		return 0;
	}
	for(i=0;i<=(strlen(thestring)-strlen(tosearch));i++)
	{
		if(thestring[i]==tosearch[0])
		{
			for(j=1;j<strlen(tosearch);j++)
			{
				newtosearch[j-1]=tosearch[j];
			}
			newtosearch[j-1]='\0';
			k=0;
			for(j=i+1;j<strlen(thestring);j++)
			{
				newstring[k++]=thestring[j];
			}
			newstring[k]='\0';
			if(no==2)
			{
				int bp=1;
			}
			count+=searchsub(newstring,newtosearch);
		}
	}
	return count;
}

int main()
{
	ifstream fin("C-small-attempt0.in",ios::in);
	ofstream fout("output.txt",ios::out);
	int i,j,k;
	int n;
	int endpos=0;
	bool started;
	char tempstring[501];
	char newstring[501];
	int currentcount;
	fin>>n;
	fin.get();
	for(i=0;i<n;i++)
	{
		no=i;
		cout<<"Case #"<<i+1<<": ";
		//input
		fin.getline(tempstring,501);
		//process
		started=false;
		k=0;
		for(j=0;j<strlen(tempstring);j++)
		{
			if(!started)
			{
				if(tempstring[j]=='w')
				{
					started=true;
					newstring[k++]=tempstring[j];
				}
				continue;
			}
			if(tempstring[j]=='w'||tempstring[j]=='e'||tempstring[j]=='l'||tempstring[j]=='c'||tempstring[j]=='o'||tempstring[j]=='m'||tempstring[j]==' '||tempstring[j]=='t'||tempstring[j]=='d'||tempstring[j]=='j'||tempstring[j]=='a')
			{
				newstring[k++]=tempstring[j];
				if(tempstring[j]=='m')
				{
					endpos=k;
				}
			}
		}
		newstring[k]='\0';
		//test
		currentcount=searchsub(newstring,"welcome to code jam");
		//out
		printf("%04d\n",currentcount%1000);
	}
	fin.close();
	fout.close();
	system("pause");
	return 0;
}