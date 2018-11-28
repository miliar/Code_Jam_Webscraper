#include <stdio.h>
#include <stdlib.h>
#include <Windows.h>
#include <vector>


using namespace std;



int data[500];
int num_count;
int data_count;
int data_location[500];

void main()
{
	FILE*	file1 = fopen("A-small-attempt1.in","r");
	FILE*	file2 = fopen("out.txt","w+");

	char test[500];
	char trans[500]; 
	int i=0;
	int j=0;
	int k=0;
	int l=0;

	fscanf(file1,"%d\n",&k);

	for(l=0; l<k;l++)
	{
		fgets(test,500,file1);
		
			for(i=0;i<500;i++)
			{
				 if(test[i]=='a') trans[i] = 'y';
			else if(test[i]=='b') trans[i] = 'h';
			else if(test[i]=='c') trans[i] = 'e';
			else if(test[i]=='d') trans[i] = 's';
			else if(test[i]=='e') trans[i] = 'o';
			else if(test[i]=='f') trans[i] = 'c';
			else if(test[i]=='g') trans[i] = 'v';
			else if(test[i]=='h') trans[i] = 'x';
			else if(test[i]=='i') trans[i] = 'd';
			else if(test[i]=='j') trans[i] = 'u';
			else if(test[i]=='k') trans[i] = 'i';
			else if(test[i]=='l') trans[i] = 'g';
			else if(test[i]=='m') trans[i] = 'l';
			else if(test[i]=='n') trans[i] = 'b';
			else if(test[i]=='o') trans[i] = 'k';
			else if(test[i]=='p') trans[i] = 'r';
			else if(test[i]=='q') trans[i] = 'z';
			else if(test[i]=='r') trans[i] = 't';
			else if(test[i]=='s') trans[i] = 'n';
			else if(test[i]=='t') trans[i] = 'w';
			else if(test[i]=='u') trans[i] = 'j';
			else if(test[i]=='v') trans[i] = 'p';
			else if(test[i]=='w') trans[i] = 'f';
			else if(test[i]=='x') trans[i] = 'm';
			else if(test[i]=='y') trans[i] = 'a';
			else if(test[i]=='z') trans[i] = 'q';
			else trans[i] = test[i];
		
		
		
		}fprintf(file2,"Case #%d: %s",l+1,trans);
	}

		


	
}