#include "stdio.h"
#include "stdlib.h"
#include "string.h"

#pragma warning(disable:4786)
#include <set>
#include <string>

using namespace std;

typedef __int64 int64;
typedef unsigned __int64 u_int64;
typedef unsigned int     u_int;
typedef u_int64  Type;
typedef unsigned char u_char;

#define MAXLEN 128

set<string> paths;

int getcount(char* buf);
int main(int argc,char* argv[])
{
	if( argc <= 1)
		return printf("need file name as a  parameter!"); 
	FILE* pf = fopen(argv[1],"r");
	if( pf == NULL)
		return printf("cann't open file");
	
	u_int T = 0;
	fscanf(pf,"%d\n",&T);
	
	int  i=0,j=0,r=0,k=0;
	char buf[MAXLEN];
	for(i=0;i<T;i++)
	{
		paths.clear();
		paths.insert("/");

		u_int sum=0;
		u_int N,M;
		fscanf(pf,"%d %d\n",&N,&M);

		for(j=0;j<N;j++)
		{
			fgets(buf,MAXLEN,pf);
			r = strlen(buf);
			if( buf[r-1] == '\n')
				buf[r-1] = '\0';
			paths.insert(buf);
		}
		for(j=0;j<M;j++)
		{
			fgets(buf,MAXLEN,pf);
			r = strlen(buf);
			if( buf[r-1] == '\n')
				buf[r-1] = '\0';
			sum += getcount(buf);
		}
		printf("Case #%d: %u\n",i+1,sum);
	}
	
	fclose(pf);
	return 0;
}

int cutname(char* path)
{
	int len  = strlen(path);
	for(int j=len-1;j>=0;j--)
	{
		if( path[j] == '/' && j != 0 )
		{
			path[j] = '\0';
			return 0;
		}
	}
	return -1;
}

int getcount(char* buf)
{
	char path[MAXLEN];
	if( paths.find(buf) == paths.end() )
	{
		strcpy(path,buf);
		if( cutname(path) < 0)
		{
			paths.insert(buf);
			return 1;
		}
		int icount = getcount(path)+1;
		paths.insert(buf);
		return icount;
	}else
	{
		return 0;
	}
}