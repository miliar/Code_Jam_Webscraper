#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int abs(int a)
{
	return a<0?-a:a;
}


int main()
{
	int T;
	scanf("%d\n",&T);
	
	for(int t=0;t<T;t++)
	{
		pair<int,int> robot[2];
		
		robot[0]=pair<int,int>(1,0);
		robot[1]=pair<int,int>(1,0);
		
		int K;
		scanf("%d",&K);
		
	//	cout<<"K : "<<K<<endl;
		
		for(int k=0;k<K;k++)
		{
			char ch;
			int pos;
			
			scanf(" %c %d",&ch, &pos);
			
			bool num = ch=='B'? 0 : 1;
			
			
			int cost = abs(robot[num].first-pos)+1;
			
			robot[num].first = pos;
			robot[num].second = max(robot[num].second+cost,robot[!num].second+1);
		}
		
		printf("Case #%d: %d\n",t+1,max(robot[0].second,robot[1].second));
	}
}