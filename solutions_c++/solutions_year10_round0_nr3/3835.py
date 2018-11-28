#include <cstdlib>
#include <cstring>
#include <memory>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
//#include <algo.h>
using namespace std;
//#define PRINT(format,args...) printf(format,args);
typedef unsigned long long int  ULLInt;
ULLInt  playAndQueue(deque<ULLInt>& groups,ULLInt& pos,ULLInt K);
static unsigned long long int pos = 0;
int main(int argc,char* argv[])
{
	
	typedef vector<ULLInt>::iterator LLD_ITER;
	string fname = "C-small-attempt6";
	

  freopen((fname+".in").c_str(), "r", stdin);
	freopen((fname+".out").c_str(), "w", stdout);
	unsigned int T,currentCase = 1;
	ULLInt K,R; //K ,the hold capacity of the roller coaster
	unsigned int N ; // N groups
	ULLInt gi;
    deque<ULLInt> groups;
    
		scanf("%u",&T);
		while(T--)
		{
				scanf("%lld %lld %u",&R,&K,&N);
				for(int i = 0; i < N;i++)
				{
					scanf("%lld ",&gi);
					groups.push_back(gi);
					
				}
				ULLInt earn = 0;
				for(int round = 0; round < R;round++)
				{
				//ULLInt limit = 0;
				
				deque<ULLInt>::iterator iter = groups.begin();
			
					earn +=playAndQueue(groups,pos,K);
				}
				printf("Case #%d: %lld\n", currentCase++,earn);
				earn = 0;
				groups.clear();
				pos = 0;
					
		}
        fclose(stdin);
        fclose(stdout);
	 return 0;
}

ULLInt  playAndQueue(deque<ULLInt>& groups,ULLInt& pos,ULLInt K)
{
		ULLInt limit = 0;
		bool isAll = true;
		deque<ULLInt>::size_type size = groups.size();
		for(int index=0; index < size;index++)
		{
			if(limit + groups[pos] > K)
				{
				//pos = index;
				isAll = false;
				break;
				}
			else 
                if(limit + groups[pos] == K )
                {
                    isAll= false;
                    limit += groups[pos];
                    pos = (pos+1)%size;
                    break;
                }
                else
                {
					limit += groups[pos];
					pos++;
					pos = pos%size;
				}
		}
		if(isAll == true)
			pos = 0;
		return limit;
}
