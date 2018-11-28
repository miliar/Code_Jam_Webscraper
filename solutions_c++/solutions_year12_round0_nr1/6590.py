#include<stdio.h>
#include<stdlib.h>
#include <fstream>
#include <iostream>


using namespace std;

// Golbal variables

char Input_Strings[40][120];
int T;
char Output_Strings[40][120];

char Google_Convert(char);
main()
{
	int i,j;
	char *File_Name;
	cin>>T;
	for(i=0;i<39;i++) 
	{
		for(j=0;j<39;j++) {Input_Strings[i][j]='\x0'; Output_Strings[i][j]='\x0';}
	}
/*
	for(i=0;i<=T;i++)
	{
		cin.getline (Input_Strings[i],100);
		//cout<<Input_Strings[i]<<'\n';		
	}
*/
	  
	//cout<<"\n\n\t Please enter the input file name :   ";
	//cin>>File_Name;
	File_Name="A-small-attempt0.in";
	ifstream file_op(File_Name,ios::in);
	
	//file_op.getline(Input_Strings[32],120);
i=0;
   		while(!file_op.eof())
		
{

		file_op.getline(Input_Strings[i],120);
		//cout<<Input_Strings[i];	
		i++;	
}
	for(i=1;i<=T;i++)
	{
		j=0;
		while(Input_Strings[i][j] != '\n' && Input_Strings[i][j] != '\x0' && j<101)
		{
			Output_Strings[i][j]=Google_Convert(Input_Strings[i][j]);
			j++;
		}
		Output_Strings[i][j]='\x0';
	}


	for(i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": "<<Output_Strings[i]<<'\n';		
	}


	return 0;
}


char Google_Convert(char in)
{
	char out;

	switch ( in ) 
	{
		case 'a':  out='y';  break;
		case 'b':  out='h';  break;
		case 'c':  out='e';  break;
		case 'd':  out='s';  break;
		case 'e':  out='o';  break;
		case 'f':  out='c';  break;
		case 'g':  out='v';  break;
		case 'h':  out='x';  break;
		case 'i':  out='d';  break;
		case 'j':  out='u';  break;
		case 'k':  out='i';  break;
		case 'l':  out='g';  break;
		case 'm':  out='l';  break;
		case 'n':  out='b';  break;
		case 'o':  out='k';  break;
		case 'p':  out='r';  break;
		case 'q':  out='z';  break;
		case 'r':  out='t';  break;
		case 's':  out='n';  break;
		case 't':  out='w';  break;
		case 'u':  out='j';  break;
		case 'v':  out='p';  break;
		case 'w':  out='f';  break;
		case 'x':  out='m';  break;
		case 'y':  out='a';  break;
		case 'z':  out='q';  break;
		
		default: out=in; break;
	}


	return out;

}
