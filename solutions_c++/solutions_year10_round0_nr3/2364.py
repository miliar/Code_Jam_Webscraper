#include <iostream>
#include <queue>
#include <list>
using namespace std;


int main()
{
	int num_test;
	
	cin>>num_test;

	for(int i=0; i!=num_test; i++)
	{
		long int R;
		cin>>R;
		
		long int k;
		cin>>k;

		int N;
		cin>>N;

		//cerr<<R<<" "<<k<<" "<<N<<endl;

		queue< long int, list<long int> > q;
			

		long int t;
		for(long int j=0; j!=N ;j++)
		{	cin>>t;
			q.push(t);
		}

		//cerr<<"que"<<q.size()<<" "<<q.front()<<" "<<q.back()<<endl;
		long int amt=0;
		
		for(long int l=0; l!=R; l++)
		{
			long int sum=0;
			long int f;
			//cerr<<l<<"th time"<<endl;
			for(int m=0; m!=N ; m++)
			{
				f=q.front();
				sum+=f;
				if(sum>k)
				break;

				q.pop();
				q.push(f);

				//cerr<<f;
				
			}
			if(sum>k)
			sum -=f;

			amt+=sum;
			//cerr<<endl<<endl;
		}
				

			


		cout<<"Case #"<<i+1<<": "<<amt<<endl;
	
				
	}

		return 0;
}
