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

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("A-large.in","r");
FILE *out=fopen("A-large.out","w");

string names[110];

string query[1100];

map < string , int > mp;

vector < int > start[200];

string readline()
{
	string ret;
	char f;
	while(fscanf(in,"%c",&f)!=EOF){
		if(f=='\n')break;
		ret+=f;
	}
	return ret;
}

int main()
{
	int test,tests,i,j,q,n,maxx,pos;
	char name[200];
	fscanf(in,"%d\n",&test);
	for(tests=0;tests<test;tests++){
		fscanf(in,"%d\n",&n);
		for(i=0;i<n;i++){
			names[i]=readline();
			mp[names[i]]=i+1;
		}
		for(i=0;i<=n;i++)start[i].resize(0);
		fscanf(in,"%d\n",&q);
		for(i=0;i<q;i++){
			query[i]=readline();
		}
		for(i=0;i<q;i++)
			start[mp[query[i]]].push_back(i);
		for(i=1;i<=n;i++)
			start[i].push_back(q);
		int ret=0,p=-1;
		while(p<q-1){
			maxx=-1;
			for(i=1;i<=n;i++){
				for(j=0;j<start[i].size();j++){
					if(start[i][j]<=p)continue;
					if(start[i][j]>maxx){
						maxx=start[i][j];
						pos=i;
					}
					break;
				}
			}
			p=maxx-1;
			ret++;
		}
		fprintf(out,"Case #%d: %d\n",tests+1,ret-1);
	}
	return 0;
}


