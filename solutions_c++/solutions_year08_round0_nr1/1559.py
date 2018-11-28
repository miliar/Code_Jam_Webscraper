#include <cstdio>
#include <string>
#include <iostream>
#include <map>
using namespace std;
#define MAX 1001

int v[MAX];
int main()
{
	int N,S,Q;
	string s;
	int index;
	map<string,int> M;
	scanf("%d ",&N);
	for(int X=1;X<=N;X++)
	{
		scanf("%d ",&S);
		M.clear();
		for(int i=0;i<S;i++)
		{
			v[i]=0;
			getline(cin,s);
			M[s] = i;
		}
		scanf("%d ",&Q);
		int currInd = 0;
		int count = 0;
		for(int i=0;i<Q;i++)
		{
			getline(cin,s);
			map<string,int>::iterator iter = M.find(s);
			if( iter != M.end() ) {

				index = M[s];
				if(v[index] == currInd)
				{
					v[index]++;
					count++;
				}
				if(count == S)
				{
					currInd++;
					v[index]++;
					count = 1;
				}
			}
		}
		printf("Case #%d: %d\n",X,currInd);
	}
	return 0;
}
