#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int tc;
	cin>>tc;
	for(int tt=1;tt<=tc;++tt)
	{
		int N,sur,min_sc;
		cin>>N>>sur>>min_sc;
		vector<int> tot_scores(N);
		for(int i=0;i<N;++i)
			cin>>tot_scores[i];

		if(min_sc == 0)
		{
			cout<<"Case #"<<tt<<": "<<N<<endl;
			continue;
		}
		else if(min_sc == 1)
		{
			int r = 0;
			for(int i=0;i<N;++i)
				if(tot_scores[i]>0)
					++r;
			cout<<"Case #"<<tt<<": "<<r<<endl;
			continue;
		}
		int min_non_sur = min_sc + 2*(min_sc-1);
		int min_sur = 3*(min_sc-1)-1;

		int r=0;
		for(int i=0;i<N;++i)
			if(tot_scores[i]>=min_non_sur)
				++r;
			else if(tot_scores[i]>=min_sur&&sur>0)
			{
				++r;
				--sur;
			}
		cout<<"Case #"<<tt<<": "<<r<<endl;
	}
	return 0;
}
