#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
int main()
{
	int T;
	scanf("%d", &T);
	int cas = 0;
	for(cas = 1; cas <= T; cas++)
	{
			int N;
			scanf("%d", &N);
			char c;
			int bb;
			int total = 0;
			int posO = 1, posB = 1;
			int prevO = 0, prevB = 0;
			int timeO = 0, timeB = 0;
			//cout << N << endl;
			while(N--)
			{
				cin >> c >> bb;
				//cout << c << " " << bb << endl;
				//cout << "hello";
				if(c == 'O')
				{
					int cur = abs(bb - posO) + 1;
					posO = bb;
					if(timeO >= timeB)
					{
						timeO += cur;
					}
					else
					{
						if(cur + timeO <= timeB)
							timeO = timeB + 1;
						else
							timeO += cur;
					}
				}
				else
				{
					int cur = abs(bb - posB) + 1;
					posB = bb;
					//cout << cur << endl;
					if(timeB >= timeO)
					{
						timeB += cur;
					}
					else
					{
						if(cur + timeB <= timeO)
							timeB = timeO + 1;
						else
							timeB += cur;
					}
					//cout << timeO <<  " " << timeB << endl;
				}
				//cout << timeO << " " << timeB << endl;
			}
			printf("Case #%d: %d\n", cas, max(timeO, timeB));
	}
	return 0;
}
