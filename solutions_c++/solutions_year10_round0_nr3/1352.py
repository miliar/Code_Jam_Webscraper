#include <iostream>

using namespace std;

long long data[1000];
long long r, K, n;

pair <long long, long long> doRotate(int s);

int main(void)
{
	int t;
	cin>>t;
	for(int caseN=1;caseN<=t;caseN++)
	{
		cin>>r>>K>>n;
		for(int i=0;i<n;i++) cin>>data[i];

		long long earned[1000], round[1000];
		memset(round, -1, sizeof(round));

		int last=0;
		long long curMoney=0;
		long long mGap, rGap;
		int cnt;

		bool isEnd=false;

		for(int i=0;;i++)
		{
			if(i==r)
			{
				isEnd=true;
				break;
			}

			int next=last;
			if(round[next]!=-1)
			{
				mGap=curMoney-earned[next];
				rGap=i-round[next];
				cnt=i;
				break;
			}

			earned[next]=curMoney;
			round[next]=i;
			pair <long long, long long> res=doRotate(next);

			curMoney+=res.second;
			last=res.first;
		}

		cout<<"Case #"<<caseN<<": ";
		if(!isEnd)
		{
			r-=cnt;
			curMoney+=(r/rGap)*mGap;
			int lim=r%rGap;
			for(int i=0;i<lim;i++) 
			{
				int next=last;
				pair <long long, long long> res=doRotate(next);
				curMoney+=res.second;
				last=res.first;
			}
		}

		cout<<curMoney<<endl;
	}

	return 0;
}

pair <long long, long long> doRotate(int s)
{
	int cnt=0;
	long long cnt2=0;
	for(int i=0;i<n;i++)
	{
		int next=(s+i)%n;
		if(cnt2+data[next]>K) break;

		cnt++;
		cnt2+=data[next];
	}

	return make_pair((s+cnt)%n, cnt2);
}
