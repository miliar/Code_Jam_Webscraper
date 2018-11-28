#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
	int n;
	scanf(" %d ",&n);
	for(int qq=0;qq<n;++qq)
	{
		int turn,a,b;
		scanf(" %d ",&turn);
		scanf(" %d %d ",&a,&b);

		vector<pair<pair<int,int>,int> > A,B;
		for(int i=0;i<a;++i)
		{
			char buf[256];
			gets(buf);
			int t1=((buf[0]-'0')*10+(buf[1]-'0'))*60 + (buf[3]-'0')*10+(buf[4]-'0');
			int t2=((buf[6+0]-'0')*10+(buf[6+1]-'0'))*60 + (buf[6+3]-'0')*10+(buf[6+4]-'0');

			A.push_back(make_pair(make_pair(t1,t2),0));
		}

		for(int i=0;i<b;++i)
		{
			char buf[256];
			gets(buf);
			int t1=((buf[0]-'0')*10+(buf[1]-'0'))*60 + (buf[3]-'0')*10+(buf[4]-'0');
			int t2=((buf[6+0]-'0')*10+(buf[6+1]-'0'))*60 + (buf[6+3]-'0')*10+(buf[6+4]-'0');

			A.push_back(make_pair(make_pair(t1,t2),1));
		}

		sort(A.begin(),A.end());


		int na=0,nb=0;
		int retA=0,retB=0;
		for(int t=0;t<24*60;++t)
		{
			for(int i=0;i<A.size();++i)
			{
				if (A[i].first.second+turn==t)
				{
					if (A[i].second==0) nb++;
					if (A[i].second==1) na++;
				}
				if (A[i].first.first==t)
				{
					if (A[i].second==0) na--;
					if (A[i].second==1) nb--;

					if (na<0) {na=0;++retA;}
					if (nb<0) {nb=0;++retB;}
				}
			} // trips
		} // t

		cout << "Case #" << qq+1 << ": " << retA << " " << retB << endl;

	}

	return 0;
}
