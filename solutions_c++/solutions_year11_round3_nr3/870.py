#include<iostream>
#include<vector>

using namespace std;
long long NWD(long long a,long long b)
{
	long long c;
	while(b!=0)
	{
		c=a%b;
		a=b;
		b=c;
	}
	return a;
}
long long NWW(long long a, long long b)
{
	return a*b/NWD(a,b);
}
int main2()
{	long long N,L,H;
	cin >> N >> L >>H;
	long long f;
	vector<long long> freq (N);
	for(int i=0;i<N;i++)
	{
		cin >> freq[i];
	}
	for(int freqz=L;freqz<=H;freqz++)
	{
		bool poss=true;
		for(int i=0;i<N;i++)
		{
			if(freq[i]%freqz != 0&& freqz%freq[i] !=0)
			{
				poss=false;
				break;
			}
		}
		if(poss)
		{
			cout << freqz << endl;
			return 1;
		}
	}
	cout << "NO"<<endl;;
}
int main()
{
	ios::sync_with_stdio(0);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		cout << "Case #" << t << ": ";
		main2();
	}
}

