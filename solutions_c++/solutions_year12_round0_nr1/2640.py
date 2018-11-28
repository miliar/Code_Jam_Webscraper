#include<iostream.h>
#include<fstream.h>
#include<stdlib.h>
#include<string.h>
#include<conio.h>
int main()
{
	char out[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	fstream fin,fout;
	fin.open("A-small-attempt1.in",ios::in);
	fout.open("A-small.out",ios::out);
	int N;
	clrscr();
	char *str,tmp[100];
	fin>>N;
	str=(char*) malloc(1004*sizeof(char));
	fin.getline(str,100);
	for(int i=0;i<N;i++)
	{
	   fin.getline(str,1000);
	   fout<<"Case #"<<i+1<<": ";
	   for(int j=0;j<strlen(str);j++)
	   {
	      if(str[j]==' ')
		fout<<' ';
	      else
	      {
		int t=(int)str[j];
		fout<<out[t-97];
	      }
	   }
	   fout<<"\n";
	   cout<<"\n";
	}
	fin.close();
	return(0);
}