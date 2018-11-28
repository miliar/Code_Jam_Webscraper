#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

struct ITEM
{
	int n;
	int check;
};

int nMaxCount;

void Process(std::vector<ITEM> vGoogler, int N, int S, int Start)
{
	if( N == 0)
	{
		int sum = 0, t;
		int value;
		for( int i=0; i < vGoogler.size(); i++)
		{
			value = vGoogler[i].n;
			
			switch( vGoogler[i].n % 3)
			{
			case 0:
				if( vGoogler[i].check == 0)
					t = vGoogler[i].n/3;
				else
					t = vGoogler[i].n/3 + 1;
				break;
			case 1:
				t = vGoogler[i].n/3 + 1;
				break;
			case 2:
				if( vGoogler[i].check == 0)
					t = vGoogler[i].n/3 + 1;
				else
					t = vGoogler[i].n/3 + 2;
				break;
			}
			if( value == 0)
				t = 0;
			if( t >= S )
				sum++;
		}
		if( sum > nMaxCount )
			nMaxCount = sum;
		return;
	}

	for( int i=Start; i < vGoogler.size(); i++)
	{
		if( vGoogler[i].check == 0 )
		{
			vGoogler[i].check = 1;
			Process(vGoogler, N-1, S, i+1);
			vGoogler[i].check = 0;
		}
	}
}

void main()
{
	int T;

	cin >> T;
	
	for(int i=1; i <= T ; i++)
	{
		int N, S, p;
		std::vector<ITEM> vGoogler;	
		cin >> N >> S >> p;
		for( int j=0; j < N; j++)
		{
			ITEM item;
			cin >> item.n;
			item.check = 0;

			vGoogler.push_back(item);
		}
		nMaxCount = 0;
		Process(vGoogler, S, p, 0 );
		cout << "Case #"<< i << ": " << nMaxCount << endl;
	}
}