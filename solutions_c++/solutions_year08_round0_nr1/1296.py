#include <stdio.h>
#include<string.h>
#include <stdlib.h>
#include <string>

int A[110][1100];
int min1(int j,int n){
	int min,i;
	min=10000;
	for(i=0;i<n;++i){
		if(min > A[i][j]) min =A[i][j];
	}
	return min;
}

	int last1(int i, int k){
		while (k>0&& A[i][k]>2000)
			--k;
		return k;
	}

int main()
{
	int x,y,area,i,j,k,n,run,iso,right,obt,min,last;
	FILE *fp;
	char in[110][110],to[1100][1100];
	FILE * pFile;
	char mystring [100],v[10],s[10];
	pFile = fopen ("input", "r");
	fgets (mystring , 100 , pFile);
	n=atoi(mystring);
	for(run=0;run<n;++run){
		fgets (v , 100 , pFile);
		x=atoi(v);
		for(i=0;i<x;++i)
			fgets (in[i] , 100 , pFile);
		fgets (s , 100 , pFile);
		y=atoi(s);
		for(i=0;i<y;++i)
			fgets (to[i] , 100 , pFile);
		for(i=0;i<x;++i)
			if(strcmp(in[i],to[0])) A[i][0]=0;
			else A[i][0]=3000;

			for(j=1;j<y;++j)
				for(i=0;i<x;++i)
					if(strcmp(in[i],to[j])){
						if(A[i][j-1] < 2000){ 
							A[i][j]=A[i][j-1];
						}
						else{
							min = min1(j-1,x)+1;
							last =last1(i,j-1)+2;
							if(min <last) A[i][j] =min;
							else A[i][j]=last;
						}
					}
					else
					{
						A[i][j]=3000;
					}
			min = min1(y-1,x);
			printf("Case #%d: %d\n",run+1,min);
	}
	fclose (pFile);
	return 0;
}
