
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N,K,B,T;
	int X[55],V[55];
	double t[55];
	int C,Case =1;

	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);


	cin>>C;
	while(C--)
	{
		cin>>N>>K>>B>>T;

     	printf("Case #%d: ",Case++);
		int i;
		for(i=0;i<N;i++)
		{
			int x;
			scanf("%d",&x);
			X[i] = B-x;
		}
		for(i=0;i<N;i++)
		{
			scanf("%d",&V[i]);
		}
		for(i=0;i<N;i++)
		{
			t[i] = X[i]*1.0/V[i];
		}


		int j=N-1;
		while(j>=0)
		{
			if(t[j]<=T)
			{
				K--;
				N--;
				if(K==0)
					break;
			}
			else
				break;
			j--;
		}
		if(K==0)
		{
			cout<<"0"<<endl;
			continue;
		}


		int k = 0;
		int count = 0;
		for(i=N-1;i>=0;i--)
		{
			if(t[i]<=T)
			{
				count += N-1-i-k;
				k++;
				if(k==K)
					break;
			}
		}

	
		if(k<K)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",count);
	}

	return 0;
}





