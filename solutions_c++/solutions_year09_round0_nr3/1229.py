//============================================================================
// Name        : welcome_to_code_jam.cpp
// Author      : Kinshul Verma
// Version     :
// Copyright   :
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int main() {
	int t,l,n, max_length,i,j,prev;
	scanf("%d",&t);
	string phrase("welcome to code jam");
	n= phrase.length();
	max_length=505;
	int mat[n][max_length];
	getchar();
	for(int case_num=1; case_num<=t; case_num++)
	{
		char buff[max_length];
		buff[max_length-1]='\0';
		scanf("%[^\n]",buff);
		getchar();
		string line(buff);
		l = line.length();
		memset(mat, 0, l*n*sizeof(int));
		prev=0;
		for(i=0;i<l;i++)
		{
			if(line.at(i)==phrase.at(0))
				mat[0][i]=++prev;
			else
				mat[0][i]=prev;
		}
		for(i=1; i<n; i++)
		{
			prev=0;
			for(j=0; j<l; j++)
			{
				if(line.at(j)==phrase.at(i))
				{
					mat[i][j]=(prev+mat[i-1][j])%10000;
					prev=mat[i][j];
				}
				else
					mat[i][j]=prev;
			}
		}
		printf("Case #%d: %04d\n",case_num,mat[n-1][l-1]);
	}
	return 0;
}
