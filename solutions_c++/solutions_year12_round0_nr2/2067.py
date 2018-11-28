#include <iostream>

using namespace std;

int main()
{
//	freopen("d:/!google/b1.in", "rt", stdin);
	int T, N, S, p, t;

	cin>>T;

	for(int tt=0; tt<T; ++tt)
	{
		cin>>N>>S>>p;

		if(p==0)
		{
			for(int i=0; i<N; ++i)cin>>t;
			cout<<"Case #"<<(tt+1)<<": "<<N<<endl;
			continue;
		}

		int cnt = 0;

		for(int i=0; i<N; ++i)
		{
			cin>>t;

			if(t==0)continue;

			if(t%3==0)
			{
				if(t/3>=p)++cnt;
				else if( (S>0) && (t/3+1 >=p) )
				{
					--S; ++cnt;
				}
			}
			else if(t%3==1)
			{
				if(t/3+1 >= p)++cnt;
			}
			else if(t%3==2)
			{
				if(t/3+1 >=p)++cnt;
				else if( (S>0) && (t/3+2 >= p) )
				{
					--S; ++cnt;
				}
			}
		}

		cout<<"Case #"<<(tt+1)<<": "<<cnt<<endl;
	}


	return 0;
}