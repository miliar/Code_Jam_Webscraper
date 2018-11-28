#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 110;

char robot[MaxN];
int button[MaxN];

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	
	int T;	cin >> T;
	
	for(int cas=1; cas<=T; cas++)
	{
		int N;	scanf("%d", &N);
		for(int i=0; i<N; i++)
		{
			scanf("%s %d", robot + i, button + i);	
		}	
		
		char ch1 = 'O', ch2 = 'B';
		int pos1 = 1, pos2 = 1;
		int ans = 0;
		
		for(int i=0; i<N; i++)
		{
			if(robot[i] != ch1)
			{
				swap(ch1, ch2);
				swap(pos1, pos2);	
			}	
			
			int d = abs(button[i] - pos1) + 1;
			ans += d;
			pos1 = button[i];
			
			int pos = pos2;
			for(int j=i; j<N; j++)
			{
				if(robot[j] == ch2)
				{
					pos = button[j];
					break;	
				}	
			}
			
			if(d >= abs(pos - pos2))
			{
				pos2 = pos;	
			}
			else
			{
				if(pos > pos2)	pos2 += d;
				else	pos2 -= d;	
			}
		}
		
		printf("Case #%d: %d\n", cas, ans);
	}
	
	
	return 0;	
}
