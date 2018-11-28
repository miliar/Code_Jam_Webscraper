#include <iostream>
#include <cstdio>
using namespace std;

char matrix[1001][5][5];
int recycled(int n, int A, int B) {

	int temp[8]={-1};
	int temp2[8]={-1,-1,-1,-1,-1,-1,-1,-1};
	int ncopy=n;
	int i=0;
	while(n>0) {

		temp[i]=n%10;
		n=n/10;
		i++;
	}

	

	int res = 0;
	int numb =0;
	for(int k=1; k<i;k++)
	{   
		numb=0;
		for(int j=k-1;j>=0;j--) {
			numb=10*numb+temp[j];

		}

		for(int j=i-1;j>k-1;j--) {
			numb=10*numb+temp[j];
		}

		int l=0;
		int flag=0;

			while(temp2[l]!=-1) {

				if(temp2[l]==numb)
					flag=1;

				l++;
			}

		if(numb>=A && numb<=B && numb>ncopy && flag==0)
		{
			
			
			//printf("%d %d %d %d\n", ncopy, numb, k,i);
			temp2[l]=numb;
			res++;
		}
	}

	return res;
}


int dot(int pos)
{
	
	for(int i=1;i<=4;i++)
	{
		
		for(int j=1;j<=4;j++)
			if(matrix[pos][i][j]=='.') return 1;

	}

	return 0;



}

int won(int pos, char let)
{
	int numlet=0;


	//Check rows
	for(int i=1;i<=4;i++)
	{
		numlet=0;
		for(int j=1;j<=4;j++)
			if(matrix[pos][i][j]==let || matrix[pos][i][j]=='T') numlet++;

		if(numlet==4)
			return 1;

	}

	//Check columns

	for(int i=1;i<=4;i++)
	{
		numlet=0;
		for(int j=1;j<=4;j++)
			if(matrix[pos][j][i]==let || matrix[pos][j][i]=='T') numlet++;

		if(numlet==4)
			return 1;

	}

	//Check diagonal
	numlet=0;
	for(int i=1;i<=4;i++)
	{
			
			if(matrix[pos][i][i]==let || matrix[pos][i][i]=='T') numlet++;
	}

	if(numlet==4)
			return 1;

	//Check other diagonal
	numlet=0;
	for(int i=1;i<=4;i++)
	{
			
			if(matrix[pos][4-i+1][i]==let || matrix[pos][4-i+1][i]=='T') numlet++;
	}

	if(numlet==4)
			return 1;


	return 0;


}

int main()
{
	FILE * fin;
    FILE * fout;

	char * xwon ="X won";
	char * owon ="O won";
	char * draw ="Draw";
	char * incp ="Game has not completed";

	fin=fopen("A-large.in","r");
	fout=fopen("A-large.out", "w");

	//O-0 X-1  .-2  T-3

	int iter=0;

	

	fscanf(fin,"%d\n", &iter);

	

	char * res;

	for(int j=0;j<iter;j++) {
      
    
	for(int i=1;i<=4;i++) {
		fscanf(fin, "%c %c %c %c\n", &matrix[j][i][1], &matrix[j][i][2], &matrix[j][i][3], &matrix[j][i][4]);
	}
    
	//fprintf(fout,"Case #%d: %d\n", j+1, res);
	}

	for(int j=0;j<iter;j++) {
      
    for(int i=1;i<=4;i++) {
		//printf("%c %c %c %c\n", matrix[j][i][1], matrix[j][i][2], matrix[j][i][3], matrix[j][i][4]);
	}
    
	//printf("\n");
	
	}


	for(int j=0;j<iter;j++) {
    
	if( won(j,'X'))
		res=xwon;
	else if (won(j,'O'))
		res=owon;
	else if (dot(j))
		res=incp;
	else
		res=draw;
    
	fprintf(fout,"Case #%d: %s\n", j+1, res);
	
	}

	fclose(fin);
	fclose(fout);

	return 0;
}

