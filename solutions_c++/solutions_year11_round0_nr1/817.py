#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
using namespace std;

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		int N; cin>>N;
		
		vector<char> colors(N);
		vector<int> numbers(N);
		for(int n=0;n<N;n++)
			cin>>colors[n]>>numbers[n];
		
		int total=0;
		int posO=1,waitO=0;
		int posB=1,waitB=0;
		for(int i=0;i<N;i++)
		{
			int time;
			switch(colors[i])
			{
			case 'O':
				time=abs(numbers[i]-posO);
				fprintf(stderr,"O: %d -> %d [%d] (%d,%d)\n",posO,numbers[i],time,waitO,waitB);
				time-=waitO;
				time=max(time,0);
				waitO=0;
				waitB+=time;
				posO=numbers[i];
				
				time++;
				waitB++;
				break;
			case 'B':
				time=abs(numbers[i]-posB);
				fprintf(stderr,"B: %d -> %d [%d] (%d,%d)\n",posB,numbers[i],time,waitO,waitB);
				time-=waitB;
				time=max(time,0);
				waitB=0;
				waitO+=time;
				posB=numbers[i];
				
				time++;
				waitO++;
				break;
			}
			total+=time;
		}
		
		int ans=total;
		printf("Case #%d: %d\n",ds,ans);
	}
	return 0;
}
