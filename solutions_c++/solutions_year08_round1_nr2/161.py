#include <iostream>
#include <vector>

using namespace std;

#define LL long long
#define pb push_back


int main()
{
	int T;
	scanf("%d",&T);
	int c=0;
	while(T--)
	{
		int N,M;
		scanf("%d",&N);
		scanf("%d",&M);
		vector< vector<int> > cust(M);
		vector< vector<int> > malt(M);
		for(int i=0;i<M;i++)
		{
			int T;
			cin >> T;
			vector<int> mm(T);
			vector<int> cc(T);
			for(int j=0;j<T;j++)
			{
				cin >> cc[j]; 
				cc[j]--;
				cin >> mm[j];
			}
			
			cust[i] = cc;
			malt[i] = mm;

		}
		int type[N];
		bool done[N];
		
		for(int i=0;i<N;i++)
			done[i] = false;

		cout<<"Case #"<<++c<<":";
		while(1)
		{

		int index = -1;
		for(int i=0;i<cust.size();i++)
		{
			if( cust[i].size() == 1)
				index = i;
		}

		if(index == -1)
			goto last;

		done[cust[index][0]] = 1;
		type[cust[index][0]] = malt[index][0];

		vector<int> rem;

		for(int i=0;i<cust.size();i++)
		{
			for(int j=0;j<cust[i].size();j++)
				if(cust[i][j]==cust[index][0])
					if(malt[i][j]==malt[index][0])
						rem.pb(i);
					else
					{
						cust[i].erase(cust[i].begin()+j,cust[i].begin()+j+1);
						malt[i].erase(malt[i].begin()+j,malt[i].begin()+j+1);
					}
		}
		sort(rem.begin(),rem.end());
		reverse(rem.begin(),rem.end());
		for(int i=0;i<rem.size();i++)
		{
			cust.erase( cust.begin()+rem[i], cust.begin() + rem[i] + 1);
			malt.erase( malt.begin()+rem[i], malt.begin() + rem[i] + 1);
		}

		for(int i=0;i<cust.size();i++)
			if(cust[i].size()==0)
				goto impossible;

		}
		
			
impossible:
			cout<<" IMPOSSIBLE\n";
			goto end;
last:
			for(int i=0;i<N;i++)
				if(done[i])
					cout<<" "<<type[i];
				else
					cout<<" 0";
			cout<<"\n";
end:;
		}
	return 0;
}
