#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>
#include <conio.h>

using namespace std;

#define lint long long

#define ss stringstream
#define pb push_back
#define sz size()
#define FOR(i,n) for(i=0;i<n;i++)
#define SFOR(i,m,n) for(i=m;i<n;i++)
#define FORD(i,n) for(i=n-1;i>=0;i--)

int A[30][550];
int main()
{
	
	
	int i,j,k,l,n;
	FILE * f1 = fopen("C-large.in","r");
	FILE * f2 = fopen("C-large.out","w");
	fscanf(f1,"%d\n",&n);
	string str = "welcome to code jam";
	
	FOR(i,n)
	{
		char buf[550];
		memset(A,0,sizeof(A));
		char ch=' ';
		string s1;
		while(ch!='\n') { s1+=ch; fscanf(f1,"%c",&ch);}
	//	string s1=string(buf);
	//	printf("%s\n",s1.c_str());
		FOR(j,s1.sz) if (s1[j]=='w') A[0][j]=1;
		SFOR(j,1,str.sz) 
			SFOR(k,j,s1.sz) 
			if (s1[k]==str[j]) 
				FOR(l,k) { A[j][k]+=A[j-1][l]; A[j][k]%=10000;}
		int res = 0;
		FOR(j,s1.sz) { res+=A[str.sz -1][j]; res%=10000;}
		if (res<10) fprintf(f2,"Case #%d: 000%d\n",i+1,res);
		else if (res<100) fprintf(f2,"Case #%d: 00%d\n",i+1,res);
		else if (res<1000) fprintf(f2,"Case #%d: 0%d\n",i+1,res);
		else  fprintf(f2,"Case #%d: %d\n",i+1,res);

		
	//	FOR(k,str.sz) {FOR(j,s1.sz) cout<<A[k][j]<<" "; cout<<endl;}

	}
	fclose(f1);
	fclose(f2);

	return 0;
}
