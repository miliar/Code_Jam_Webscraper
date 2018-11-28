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

FILE *in=fopen("A.in","r");
FILE *out=fopen("A.out","w");

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
int solve(string s,int x)
{
	int i,ret=0;
	for(i=x;i<s.size();i++)
		if(s[i]=='1')return 0;
	return 1;
}
int n;
int main()
{
	int i,j,k,T,ret;
	fscanf(in,"%d\n",&T);
	for(int test=1;test<=T;test++){
		fscanf(in,"%d\n",&n);
		vector < string > ar;
		for(i=0;i<n;i++)
			ar.push_back(readline());
		ret=0;
		for(i=0;i<n;i++){
			for(j=i;j<n;j++){
				if(solve(ar[j],i+1)){
					string x=ar[j];
					ar.erase(ar.begin()+j);
					ar.insert(ar.begin()+i,x);
					ret+=j-i;
					break;
				}
			}
		}
		fprintf(out,"Case #%d: %d\n",test,ret);
	}
	return 0;
}
