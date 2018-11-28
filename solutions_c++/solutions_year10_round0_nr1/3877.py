#include <iostream>
#include <stdio.h>
#include <string>
#include <sstream>

using namespace std;

int getLine(char s[],int n,FILE *f) //read a char* line
{
   int i=0;
   while (1)
   {
      s[i] = (char) fgetc(f);
      if((s[i] == '\n')||(s[i] == '\r')||(i==(n-1)))
      {
		s[i] = '\0';
		return (feof(f) ? 1 : 0);
      }
      else if((s[i] == '\0')) continue;
      ++i;
   }
}

void splitline(char line[], int length, FILE *fp)
{
	string str1,str2;
	int N, K;
	int temp = 1;
	int flag = 0;

	for(int i=0;i<length;i++)
	{
	  if(line[i] != ' '&&flag == 0)
	  {
		  str1.append(1,line[i]);
	  }
	  else if(line[i] !=' '&&flag == 1) {
	      str2.append(1,line[i]);
	  }
	  else if(line[i] == ' ')
	  {
		flag = 1;
	  }
	}
	stringstream(str1) >> N;
	stringstream(str2) >> K;

	for(int i=0;i<N;i++)
	{
		temp = temp * 2;
	}
	if((K+1)%temp == 0)
		//cout<<"ON"<<endl;
		fprintf(fp,"%s\n","ON");
	else
		//cout<<"OFF"<<endl;
		fprintf(fp,"%s\n","OFF");
}


int main()
{
	char line[256];
	int T;
	string str;
	FILE* fp1 = fopen("A-large.in","r");
	FILE *fp2 = fopen("A-large.out","wt+");
	if( fp1!=NULL)
	{
	  getLine(line,sizeof(line),fp1);
	  str = line;
	}
	stringstream(str) >> T;

	for(int i=0;i<T;i++)
	{
		getLine(line,sizeof(line),fp1);
		str = line;
		//cout<<"Case #"<<(i+1)<<": ";
		fprintf(fp2,"%s%d%s","Case #",i+1,": ");
		splitline(line,str.size(),fp2);
	}
	fclose(fp1);
	fclose(fp2);

}
