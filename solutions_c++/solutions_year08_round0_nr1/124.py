#include<string>
#include<vector>
#include<set>
#include<stdio.h>
using namespace std;

int main()
{
	FILE *in = fopen("A-large.in","r");
	FILE *out = freopen("A-large.out","w",stdout);
	int N,S,Q;
	char input[200];
	char empty[10] = {10,0};
	int n,s,q;
	fgets(input,200,in);
	while(strcmp(input,empty)==0)
			fgets(input,200,in);
	N = atoi(input);
	for(n=0;n<N;n++) {
		vector<string> engine;
		set<string> query;
		query.clear();
		int result = 0;
		fgets(input,200,in);
		while(strcmp(input,empty)==0)
			fgets(input,200,in);
		S = atoi(input);
		for(s=0;s<S;s++) {	
			fgets(input,200,in);
			while(strcmp(input,empty)==0)
				fgets(input,200,in);
			engine.push_back(string(input));
		}
		fgets(input,200,in);
		while(strcmp(input,empty)==0)
			fgets(input,200,in);
		Q = atoi(input);
		
		for(q=0;q<Q;q++) {
			fgets(input,200,in);
			while(strcmp(input,empty)==0)
				fgets(input,200,in);
			query.insert(string(input));
			if(query.size() == S) {
				query.clear();
				query.insert(string(input));
				result++;
			}
		}
		printf("Case #%d: %d\n",n+1,result);
	}
	return 0;
}