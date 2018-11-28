#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <string.h>
#include <algorithm>

using namespace std;

char read[1000];


int main()
{
	vector< pair<int,int> > O;
	vector< pair<int,int> > B;
	
	stack< pair<int,int> > stackO;
	stack< pair<int,int> > stackB;
	
	
	int q = 1;
	int z;
	scanf("%d",&z);
	while(q<=z)
	{
		int n;
		int l = 0;
		int k = 0;
		scanf("%s",read);
		n = atoi(read);
		int r = 2;
		int i = 0;
		while(i<n)
		{
			scanf("%s",read);
			if (read[0]=='O') 
			{
				scanf("%s",read);
				O.push_back(pair<int,int>(i,atoi(read)));
			}
			else 
			{
				scanf("%s",read);
				B.push_back(pair<int,int>(i,atoi(read)));
			}
			r +=3;
			i++;
		}
		l = O.size();
		k = B.size();
		
		sort(O.begin(),O.end());
		sort(B.begin(),B.end());
		
		
		
		int t = 0;
		int pozO = 1;
		int pozB = 1;
		
		for (int i =l-1;i>=0;i--)
		{
			stackO.push(O[i]);
		}
		
		
		for (int i =k-1;i>=0;i--)
		{ 
			stackB.push(B[i]);
		}
		
		while(!stackO.empty() && !stackB.empty())
		{
			if (stackO.top().first<stackB.top().first)
			{
				while(stackO.top().second != pozO)
				{
					if (stackO.top().second < pozO) pozO--;
					else if (stackO.top().second > pozO) pozO++;
					
					if (stackB.top().second < pozB) pozB--;
					else if (stackB.top().second > pozB) pozB++;
					t++;
				}
				t++; 
				if (stackB.top().second < pozB) pozB--;
				else if (stackB.top().second > pozB) pozB++;
				stackO.pop();
			}
			else
			{
				while(stackB.top().second != pozB)
				{
					if (stackO.top().second < pozO) pozO--;
					else if (stackO.top().second > pozO) pozO++;
					
					if (stackB.top().second < pozB) pozB--;
					else if (stackB.top().second > pozB) pozB++;
					t++;
				}
				stackB.pop();
				if (stackO.top().second < pozO) pozO--;
				else if (stackO.top().second > pozO) pozO++;
				
				t++; 
			}
			
		}
		
		while(!stackB.empty())
		{
			while(stackB.top().second != pozB)
			{
				if (stackB.top().second < pozB) pozB--;
				else if (stackB.top().second > pozB) pozB++;
				t++;
			} 
			t++;
			stackB.pop();
		}
		
		while(!stackO.empty())
		{
			while(stackO.top().second != pozO)
			{
				if (stackO.top().second < pozO) pozO--;
				else if (stackO.top().second > pozO) pozO++;
				t++;
			} 
			t++;
			stackO.pop();
		}
		
		O.clear();
		B.clear();
		
		printf("Case #%d: %d\n",q,t);
		q++;
	}
	return 0;
}
