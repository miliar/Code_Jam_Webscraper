#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
	int N ; 
	scanf("%d",&N) ; 

	for(int i = 1 ; i <= N ; i++)
	{
		int r,k,n ; 
		scanf("%d %d %d",&r,&k,&n) ; 

		long long sum = 0 ; 
		vector<bool> check(n,false) ; 
		vector<int> next(n,-1) ; 
		vector<long long> partSum(n) ; 
		vector<int> g(n) ; 

		for(int j = 0 ; j < n ; j++)
		{
			scanf("%d", &g[j]) ;
			sum+= g[j] ; 
		}		

		long long ret = 0  ; 
		if(sum <= (long long)k)
		{
			ret = sum*r ; 			
		}
		else
		{
			sum = 0 ; 
			int cnt = 0 ; 
			int index = 0 ; 
			while(check[index]==false && cnt<r)
			{
				int old_index = index ; 
				check[index] = true ; 

				long long localSum =  0 ; 
				
				while(1)
				{
					if(localSum+g[index] > k) break ; 
					
					localSum += g[index++] ;
					if(index == n) index = 0 ; 
				}
				partSum[old_index] = localSum ;
				sum += localSum ; 
				next[old_index] = index;
				cnt++ ; 
			}	
			
			if(cnt != r)
			{
				int cycleCnt = 0 ; 
				int cycleIndex = index ; 
				long long cycleSum = 0 ; 
				while(1)
				{
					cycleSum += partSum[index] ; 
					index = next[index] ; 
					cycleCnt++ ; 
					if(cycleIndex == index) break; 
				}

				r -= cnt - cycleCnt ; 
				sum = sum - cycleSum; 

				sum += (long long) (r/cycleCnt) * cycleSum ; 

				int restCnt = r%cycleCnt ; 
				for(int j = 0 ; j < restCnt ; j++)
				{
					sum += partSum[index] ; 
					index = next[index] ; 
				}
			}
			ret = sum ; 
		}
		cout<<"Case #"<<i<<": "<<ret<<endl;
	}
	return 0 ; 
}