#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
 int i;
 int N; //number of cases
 char string[500][100]; //to store strings
 int count=0;
 cin>>N;
 for(i=0;i<=N;i++)
 {
  gets(string[i]);
 }
/*Tsting input
 for(int i=0;i<=N;i++)
 {
  cout<<i<<string[i]<<"\n";
 }
*/
//Checking logic

 for (i=1;i<=N;i++)
 {
  for (int j=0;string[i][j]!='\0';j++)
	if (string[i][j]=='w')					//w
	{
//cout<<string[i][j];			//testing
		 for (int j2=j+1;string[i][j2]!='\0';j2++)
	 	if (string[i][j2]=='e')					//e
		{
//cout<<string[i][j2];			//testing
		 for (int j3=j2+1;string[i][j3]!='\0';j3++)
	 	if (string[i][j3]=='l')					//l
		{
//cout<<string[i][j3];			//testing
		 for (int j4=j3+1;string[i][j4]!='\0';j4++)
	 	if (string[i][j4]=='c')					//c
		{
//cout<<string[i][j4];			//testing
	 	 for (int j5=j4+1;string[i][j5]!='\0';j5++)
	 	if (string[i][j5]=='o')					//o
		{
//cout<<string[i][j5];			//testing
		 for (int j6=j5+1;string[i][j6]!='\0';j6++)
	 	if (string[i][j6]=='m')					//m
		{
//cout<<string[i][j6];			//testing
		 for (int j7=j6+1;string[i][j7]!='\0';j7++)
	 	if (string[i][j7]=='e')					//e
		{
//cout<<string[i][j7];			//testing
		 for (int j8=j7+1;string[i][j8]!='\0';j8++)
	 	if (string[i][j8]==' ')					//space
		{
//cout<<string[i][j8];			//testing
		 for (int j9=j8+1;string[i][j9]!='\0';j9++)
	 	if (string[i][j9]=='t')					//t
		{
//cout<<string[i][j9];			//testing
		 for (int j10=j9+1;string[i][j10]!='\0';j10++)
	 	if (string[i][j10]=='o')					//o
		{
//cout<<string[i][j10];			//testing
		 for (int j11=j10+1;string[i][j11]!='\0';j11++)
	 	if (string[i][j11]==' ')					//space
		{
//cout<<string[i][j11];			//testing
		 for (int j12=j11+1;string[i][j12]!='\0';j12++)
	 	if (string[i][j12]=='c')					//c
		{
//cout<<string[i][j12];			//testing
		 for (int j13=j12+1;string[i][j13]!='\0';j13++)
	 	if (string[i][j13]=='o')					//o
		{
//cout<<string[i][j13];			//testing
		 for (int j14=j13+1;string[i][j14]!='\0';j14++)
	 	if (string[i][j14]=='d')					//d
		{
//cout<<string[i][j14];			//testing
		 for (int j15=j14+1;string[i][j15]!='\0';j15++)
	 	if (string[i][j15]=='e')					//e
		{
//cout<<string[i][j15];			//testing
		 for (int j16=j15+1;string[i][j16]!='\0';j16++)
	 	if (string[i][j16]==' ')					//space
		{
//cout<<string[i][j16];			//testing
		 for (int j17=j16+1;string[i][j17]!='\0';j17++)
	 	if (string[i][j17]=='j')					//j
		{
//cout<<string[i][j17];			//testing
		 for (int j18=j17+1;string[i][j18]!='\0';j18++)
	 	if (string[i][j18]=='a')					//a
		{
//cout<<string[i][j18];			//testing
		 for (int j19=j18+1;string[i][j19]!='\0';j19++)
	 	if (string[i][j19]=='m')					//m
		{
//cout<<string[i][j19];			//testing
		 count++;
		}
}}}}}
}}}}}
}}}}}
}}}	
  if(count<9)
  cout<<"Case #"<<i<<": 000"<<count<<"\n";
  else if(count<99)
  cout<<"Case #"<<i<<": 00"<<count<<"\n";
  else if(count<999)
  cout<<"Case #"<<i<<": 0"<<count<<"\n";
  else 
  cout<<"Case #"<<i<<": "<<count<<"\n";
  count=0;
 }
 return 0;
}

