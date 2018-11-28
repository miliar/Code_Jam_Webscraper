#include<cstdio>
#include<vector>
using namespace std;
#define MAXK 1000001
#define PB push_back
int deck[MAXK];
vector<int> idx;
const bool dbg=0;
void computeCase(int cas)
{
	idx.clear();
	int K;
	int n,a;
	scanf("%d%d",&K,&n);
	for(int i=0;i<K;i++)
		deck[i]=K+2;
	for(int i=0;i<n;i++)
	{
		scanf("%d",&a);
		a--;
		idx.PB(a);
	}
	int id=0;
	deck[0]=1;
	for(int i=2;i<K+1;i++)
	{
		int count=0;
		for(id++;count<i;id++)
		{
			if(id==K)id=0;
			if(deck[id]>i)count++;
		}
		id--;
		deck[id]=i;
	}
	if(dbg){for(int i=0;i<K;i++)printf("%d ",deck[i]);printf("\n");}
	printf("Case #%d: ",cas+1);
	for(int i=0;i<n;i++)
		printf("%d ",deck[idx[i]]);
	printf("\n");
}
int main()
{
	int t;scanf("%d",&t);
	for(int i=0;i<t;i++)
		computeCase(i);
	return 0;
}



