#include<iostream>
#include<vector>
#define INF (1LL<<62)
#define MIN(a,b) ((a)<(b)?(a):(b))

using namespace std;

int P,K,L;
vector <int> freq;
long long mem[1001][1001];
long long get(int begin, int end)
{
	long long pos=(L-1)-(end-begin);
	pos/=K;
	pos++;
	long long min=INF;
	if(begin==end)
		return pos*freq[begin];
	if(mem[begin][end]!=-1)
		return mem[begin][end];
	min=MIN(min,pos*freq[begin]+get(begin+1,end));
	min=MIN(min,pos*freq[end]+get(begin,end-1));
	mem[begin][end]=min;
	return min;
}
	
int main()
{
	int N,count=1;
	cin>>N;
	while(N--)
	{
		cin>>P>>K>>L;
		freq.resize(L);
		int i;
		for(i=0;i<L;i++)
			cin>>freq[i];
		sort(freq.begin(),freq.end());
		memset(mem,0xff,sizeof(mem));
		cout<<"Case #"<<count<<": "<<get(0,L-1)<<endl;
		count++;
	}
	return 0;
}

