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

vector < string > ar;

int memo[5100*15];

int trie[5100*15][27];

int p=1;

FILE *in=fopen("A.in","r");
FILE *out=fopen("A.out","w");

void adds(string s)
{
	int node=0;
	for(int i=0;i<s.size();i++){
		if(trie[node][s[i]-'a']!=-1)node=trie[node][s[i]-'a'];
		else {
			trie[node][s[i]-'a']=p;
			node=p++;
		}
	}
}

int L;

int solve(int node,int pos)
{
	if(pos==L)return 1;
	int &ret=memo[node];
	if(ret!=-1)return ret;
	ret=0;
	int i;
	for(i=0;i<ar[pos].size();i++){
		if(trie[node][ar[pos][i]-'a']==-1)continue;
		ret+=solve(trie[node][ar[pos][i]-'a'],pos+1);
	}
	return ret;
}
vector<string> tokenize(string s, string ch)
{
	int p,p2;
	vector<string> ret;
	for( p = 0; p < s.size(); p = p2+1 )
	{
		if(s[p]=='('){
			p2=p;
			continue;
		}
		p2 = s.find_first_of(ch, p);
		if( p2 == -1 ) p2 = s.size();
		if( p2-p > 0 && s[p2]==')') ret.push_back( s.substr(p, p2-p) );
		else {
			p2=p;
			ret.push_back( s.substr(p, 1) );
		}

	}
	return ret;
}

int main()
{
	int i,j,k;
	int D,T,ret;
	fscanf(in,"%d%d%d",&L,&D,&T);
	CLR(trie,-1);
	char junk[5100];
	for(i=0;i<D;i++){
		fscanf(in,"%s",junk);
		string QQ=junk;
		adds(QQ);
	}
	for(int test=0;test<T;test++){
		fscanf(in,"%s",junk);
		string QQ=junk;
		ar=tokenize(QQ,"()");
		CLR(memo,-1);
		ret=solve(0,0);
		fprintf(out,"Case #%d: %d\n",test+1,ret);
	}
	return 0;
}



