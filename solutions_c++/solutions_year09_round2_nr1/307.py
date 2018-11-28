// Author -Swarnaprakash.U
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>
#include<cstring>

using namespace std;

const bool debug=false;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define PB 			push_back
#define SZ(x)		((int)((x).size()))
#define TR(i,x) 	for(i=0;i<(x).size();++i)
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;
#define HELLO		if(debug) puts("hello");
#define LL 			long long
#define INF			0x3f3f3f3f
#define M 105;


set<string> animal;
string tree;
string whitespace;

vector<string> tokenize(string s,string delimiters)
{
	char ns[s.size()+1];
	char delim[delimiters.size()+1];
	char *token;
	
	strcpy(ns,s.c_str());
	strcpy(delim,delimiters.c_str());
	
	token=strtok(ns,delim);
	
	vector<string> ans;
	
	while(token!=NULL)
	{
		ans.push_back( (string) token);
		token=strtok(NULL,delim);
	}
	return ans;
}

double fun(int start,int end)
{
	DB(tree.substr(start,end-start));
	assert(start<end);
	while(isspace(tree[start]))
		++start;
	DB(tree[start]);	
	assert(tree[start]=='(');
	
	int i;
	double nodep;
	string val;
	i=start+1;
	while(isspace(tree[i]))
		++i;
		
	for(;i<end && (isdigit(tree[i]) || tree[i]=='.');++i)
		val+=tree[i];
	sscanf(val.c_str(),"%lf",&nodep);

		
	string features;
	for(;i<end && tree[i]!='(' && tree[i]!=')';++i)
		features+=tree[i];
		
	vector<string> f=tokenize(features,whitespace);
	
	int newstart,newend;
	if(tree[i]==')')
		return nodep;
	DB("here");
	int count=0;
	newstart=i;
	for(;;++i)
	{
		assert(i<end);
		if(tree[i]=='(')
			++count;
		else if(tree[i]==')')
			--count;
		if(count==0)
		{
			newend=i+1;
			break;
		}
	}
	
	TR(i,f)
		if(animal.find(f[i])!=animal.end())
			return nodep*fun(newstart,newend);
	return nodep*fun(newend,end);
}	

int main()
{
	whitespace=" \n\t";
	int t,tc;
	scanf("%d",&tc);
	for(t=1;t<=tc;++t)
	{
		int L;
		scanf("%d ",&L);
		tree="";
		int i;
		char buf[100];
		for(i=0;i<L;++i)
		{
			
			gets(buf);
			tree+=(string)buf;
		}
		int A;
		scanf("%d",&A);
		printf("Case #%d:\n",t);
		for(i=0;i<A;++i)
		{
			scanf("%s",buf);
			int num;
			scanf("%d",&num);
			animal.clear();
			while(num--)
			{
				scanf("%s",buf);
				animal.insert((string)buf);
			}
			printf("%lf\n",fun(0,SZ(tree)));
		}
		
	}
	return 0;
}
