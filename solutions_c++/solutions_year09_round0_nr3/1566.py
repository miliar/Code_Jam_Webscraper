#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <math.h> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <stack> 
#include <queue> 
#include <map> 
#include <set> 
#include <iterator> 
#include <iostream> 
#include <functional> 
#include <sstream> 
#include <numeric>

using namespace std;

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) ) 
#define EPS 1e-9

FILE *in=fopen("C.in","r");
FILE *out=fopen("C.out","w");

int visread=0;
string readline()
{
	string qwe;
	char junk;
	for(;;){
		if(fscanf(in,"%c",&junk)==EOF){visread=1;break;}
		if(junk=='\n')break;
		qwe+=junk;
	}
	return qwe;
}

string wel="welcome to code jam";
string ar;

int memo[510][20];

int solve(int pos,int p)
{
	if(p==wel.size())return 1;
	if(pos==ar.size())return 0;
	int &ret=memo[pos][p];
	if(ret!=-1)return ret;
	ret=solve(pos+1,p);
	if(ar[pos]==wel[p])ret+=solve(pos+1,p+1);
	ret%=1000;
	return ret;
}

int main()
{
	int i,j,k,T,ret;
	fscanf(in,"%d\n",&T);
	for(int test=1;test<=T;test++){
		ar=readline();
		CLR(memo,-1);
		ret=solve(0,0);
		fprintf(out,"Case #%d: %04d\n",test,ret);
	}
	return 0;
}
