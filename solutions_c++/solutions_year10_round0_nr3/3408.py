#include<iostream>
#include<vector>

using namespace std;

main()
{
	long long int T,R,k,N,l;


	cin >> T;
	
	for(l=0;l<T;l++)
	{

		cin >> R >> k >> N;
		vector<long long int> G(N,0),profit(N,0),next(N,0);

		for(int i=0;i<N;i++)cin >> G[i];
		
		long long int count=0,index=0,gain=0,current=0,i;
		for(i=0;i<N;i++)
		{
			count=G[i];
			index=(i+1)%N;

			while(1)
			{
				if((count + G[index] <=k) && (index!=i)) count+=G[index];
				else break;
				index=(index+1)%N;
			}
			next[i]=index;
			profit[i]=count;
		}

		for(i=0;i<R;i++)
		{
			gain+=profit[current];
			current=next[current];

		}
		cout<<"Case #"<<l+1<<": "<<gain<<'\n';
	}
}
		
			

		
	
		
