#include <iostream>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int N,T;
	cin >> T;
	for(int i=0;i<T;i++)
	{
		cin >> N;
		char color;
		int OP=1,BP=1;
		int step=0;
		int OB[200]={0};
		bool who[200]={0};
		for(int j=0;j<N;j++)
		{
			cin >> color;
			if(color == 'O')
			{
				cin >> OB[j];
				who[j] = 0;
			}
			else
			{
				cin >> OB[j];
				who[j] = 1;
			}
		}
		int k = 0;
		while(k<N)
		{
			step++;
			int p = k;
			if(who[k] == 0)
			{
				while(who[p] != 1 && p<=N) p++;
				if(OB[p] < BP && p<=N) BP--;
				else if(OB[p] > BP && p<=N) BP++;
				if(OP < OB[k]) OP++;
				else if(OP > OB[k]) OP--;
				else k++;
			}
			else
			{
				while(who[p] != 0 && p<=N) p++;
				if(OB[p] < OP && p<=N) OP--;
				else if(OB[p] > OP && p<=N) OP++;
				if(BP < OB[k]) BP++;
				else if(BP > OB[k]) BP--;
				else k++;
			}
		}
		cout << "Case #" << i+1 << ": " << step << endl;
	}	
	return 0;
}
