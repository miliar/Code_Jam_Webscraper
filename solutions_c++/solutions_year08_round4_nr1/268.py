#include <iostream>
#include <vector>

using namespace std;
#define pb push_back
#define LL long long

int P[10001];
bool C[10001];
bool type[10001];
int T;

#define INF 1000000

int rec(int ind)
{
	if(ind>=T)
		return type[ind] ? 0 : INF;
	if( P[ind]!=-1)
		return P[ind];
	
	if( type[ind])
		P[ind] = rec(ind*2+2)+rec(ind*2+1);
	else 
		P[ind] = min ( rec(ind*2+2), rec(ind*2+1));
	if(C[ind])
		P[ind] = min( P[ind], 1 + min ( rec(ind*2+2), rec(ind*2+1)));
	return P[ind];
	
			
}


int main()
{
	int TT;
	scanf("%d",&TT);
	int c=0;
	while(TT--)
	{
		for(int i=0;i<10001;i++) P[i] = -1;
		int M,V;
		scanf("%d %d", &M, &V);
		T = (M-1)/2;
		for(int i=0;i<T;i++)
			scanf("%d %d", &type[i], &C[i]);
		for(int i=T;i<M;i++)
			scanf("%d", &type[i]);
		if(!V)
			for(int i=0;i<M;i++)
			{
				type[i] = !type[i];
			}
		int ret = rec(0);
		if( ret >= INF)
		cout<<"Case #"<<++c<<": IMPOSSIBLE\n";
		else
		cout<<"Case #"<<++c<<": "<<ret<<"\n";
	}
	return 0;
}
