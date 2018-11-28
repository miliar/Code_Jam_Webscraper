#include<iostream>
#include<vector>
using namespace std;


int main()
{
	//freopen("C-small-attempt1.IN","r",stdin);
	//freopen("C-small-attempt1.OUT","w",stdout);


	long int T,kase,earn,R,K,N,i,j,mem,tot;
	vector<long int>x;

	cin>>T;

	for(kase=1;kase<=T;kase++)
	{
		cin>>R>>K>>N;
		
		x.clear();
		
		for(i=0;i<N;i++)
		{
			cin>>mem;
			x.push_back(mem);
		}
		
		earn=0;

		for(i=1;i<=R;i++)
		{
			tot=0;

			for(j=0;j<x.size();j++)
			{
				if (tot+x.front()<=K)
				{
					tot+=x.front();
					earn+=x.front();

					long int temp=x.front();

					x.erase(x.begin(),x.begin()+1);

					x.push_back(temp);
				}
				else break;
			}

			/*
			for(j=0;j<x.size();j++)
				cout<<x[j]<<" ";
			
			cout<<"\n";
			*/
		}

		cout << "Case #" << kase << ": " << earn << "\n";
	}

	return 0;
}