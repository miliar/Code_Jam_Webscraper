#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int C,I;
	cin >> C;
	for(I=1;I<=C;I++)
	{
		int N,K,B,T,i,j,cnt=0;
		vector <int> c;
		
		cin >> N >> K >> B >> T;
		
		for(i=0;i<N;i++)
		{
			cin >> j;
			c.push_back(j);
		}
		for(i=0;i<N;i++)
		{
			cin >> j;
			c[i] += j*T;
			if(c[i]>=B) cnt++;
		}
		
		if(cnt>=K)
		{
			int r=0;
			int curpos = N-1;
			i = N-1;
			while(K)
			{
				if(c[i]>=B)
				{
					r += curpos - i;
					curpos--;
					K--;
				}
				i--;			
			}			
			cout << "Case #" << I << ": " << r << endl;			
		}
		else
			cout << "Case #" << I << ": " << "IMPOSSIBLE" << endl;	
		
	}
}
