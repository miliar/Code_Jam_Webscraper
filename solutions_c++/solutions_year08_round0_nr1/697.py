#include <iostream>
#include <vector>

using namespace std;
int N,S,Q;
vector<int> queries;
int P[1001];
int QQ[101][1001];

int rec(int ind)
{
	if(ind == Q)
		 return 0;
	if(P[ind]!=-1) return P[ind];
	P[ind]=999999;
	for(int i=0;i<S;i++)
		if(queries[ind]!=i)
		{
			P[ind] = min ( P[ind] , 1 + rec(QQ[i][ind]));
		}
	return P[ind];
}

void pre()
{
	for(int j=0;j<S;j++)
	for(int i=0;i<Q;i++)
	{
		int ind;
		for(ind = i+1;ind<Q && queries[ind]!=j;ind++);
		QQ[j][i]=ind;
	}
}

int main()
{
	scanf("%d",&N);
	int cnt=0;
	while( N-- )
	{
		cnt++;
		for(int i=0;i<1001;i++)
			P[i] = -1;
		::queries.clear();
		scanf("%d\n",&S);
		vector<string> names;
		for(int i=0;i<S;i++)
		{
				char arr[200];
				cin.getline(arr,200);
				names.push_back(arr);			
		}	
		scanf("%d\n",&Q);
		for(int i=0;i<Q;i++)
		{
			char arr[200];
			cin.getline(arr,200);
			int index = -1;
			for(int j=0;j<S;j++)
			if( names[j]==(string)arr)
				index = j;
			queries.push_back(index);	
		}	
		//solve
		pre();
		printf("Case #%d: %d\n", cnt, max ( 0, rec(0) - 1) );


	}
	return 0;
}
