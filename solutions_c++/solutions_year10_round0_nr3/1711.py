#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
long long visited[1200];
int main()
{
	long long N,R,k,test;
	cin>>test;
	for(long long i1=1;i1<=test;++i1)
	{
		memset(visited,0,sizeof(visited));
		cin>>R>>k>>N;
		vector<long long> A(2*N);
		for(long long i=0;i<N;++i)   cin>>A[i];
		for(long long i=N;i<2*N;++i)  A[i]=A[i-N];
		for(long long i=1;i<2*N;++i)  A[i]+=A[i-1];
		vector<long long> next(N),money(N);
		long long previous=0,current=0;
		long long Money=0;
		while(R)
		{
			if(visited[current])
				break;
			vector< long long >::iterator upper;
			long long factor=(current==0)?0:A[current-1];
			upper=upper_bound( A.begin()+current, A.begin()+current+N, k+factor);
			long long pos=upper-A.begin()-1;
			next[current]=(pos+1)%N;
			money[current]=A[pos]-factor;
		//	cout<<current<<" "<<pos<<" "<<next[current]<<" "<<money[current]<<"\n";
			visited[current]=1;
			current=next[current];
			--R;
			Money+=A[pos]-factor;
		}
	//	cout<<"repeated\n";
		long long repeated=current,pos=0,cycleM=0;
		//cout<<repeated<<" "<<Money<<" "<<R<<"\n";
		long long save[1200];
		memset(save,0,sizeof(save));
		while(R)
		{
			pos++;
			R--;
			Money+=money[current];
			cycleM+=money[current];
			current=next[current];
			save[pos]=cycleM;
			if(current==repeated)
			{
				break;
			}
		}
		cout<<"Case #"<<i1<<": ";
		if(!R)
		{
			cout<<Money<<"\n";
			continue;
		}
		//cout<<"hhh\n"<<R<<" "<<Money<<" "<<pos<<" "<<cycleM<<"\n";
		long long times=R/pos;
		Money+=times*cycleM;
		R%=pos;
		//cout<<R<<" "<<Money<<"yy\n";
		Money+=save[R];
		cout<<Money<<"\n";
	}
}