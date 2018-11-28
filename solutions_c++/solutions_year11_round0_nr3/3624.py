#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
	freopen("//Users//KwonHC//Xcode//Qualification Round 2011 C. Candy Splitting//C-large.in", "rt", stdin);
	freopen("//Users//KwonHC//Xcode//Qualification Round 2011 C. Candy Splitting//C Candy Splitting large.out", "wt", stdout);
	int T, N;
	int Sean[20];
	long long table[1000];
	long long sum;
	long long minCandy;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		memset(Sean, 0 , sizeof Sean);
		minCandy=1000001;
		sum=0;
		cin >> N;
		for(int i=0; i<N; i++)
		{
			cin >> table[i];
			sum+=table[i];
			minCandy=min(minCandy, table[i]);
		}
	
		for(int i=0; i<N; i++)
		{
			int binaryCnt=524288;
			for(int j=0; j<20; j++)
			{
				if(table[i]==0)
					break;
				else if(table[i]>=binaryCnt)
				{
					table[i]-=binaryCnt;
					if(Sean[j]==0) Sean[j]=1;
					else if(Sean[j]==1) Sean[j]=0;
				}
				binaryCnt/=2;
			}
		}
		bool flag=true;
		for(int i=0; i<20; i++)
		{
			if(Sean[i]!=0)
			{
				flag=false;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if(flag)
			cout << sum-minCandy << endl;
		else 
			cout << "NO" << endl;
		
	}
	return 0;
}