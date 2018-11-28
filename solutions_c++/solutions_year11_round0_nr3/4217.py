#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;



int main()
{
	cout<<"JMK\n";
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int i,j,r,k,nCandies,line=0,testCase=0;
	unsigned long long patSum =0;
	unsigned long long seanSum =0;
	unsigned long long minElem =0;
	unsigned long long candyValue=0;
    
    scanf("%d",&testCase);
	

	
    for (line=0;line<testCase;line++)
    {
        scanf("%d",&nCandies);		
		patSum =0;
		seanSum =0;
		minElem =1000000+1;

        for (i=0;i<nCandies;i++)
		{
            scanf("%lld",&candyValue);		
			patSum = patSum ^ candyValue;
			if (candyValue < minElem)
			{
				minElem = candyValue;
			}
			seanSum = seanSum + candyValue;
		}
		if (0 != patSum)
		{
			printf("Case #%d: %s\n",line+1,"NO");
		}
		else
		{
			seanSum = seanSum - minElem;
			printf("Case #%d: %lld\n",line+1,seanSum);
		}
        
    }
	
	return 0;
}

