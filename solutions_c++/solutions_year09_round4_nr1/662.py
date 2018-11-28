#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

const int nmax=45;
int cm[nmax];				// cm[r] is the maximum column with a 1 in row r

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	int n;
	scanf("%d ",&n);
	for(int r=0;r<n;r++)
	{
	    cm[r]=-1;
	    for(int c=0;c<n;c++)
	    {
		char ch;
		scanf("%c ",&ch);
		if(ch=='1')
		    cm[r]=c;
	    }
	    //printf("%d\n",cm[r]);
	}

	int swaps=0;
	for(int r=0;r<n;r++)
	    if(cm[r]>r)
	    {
		int rn=-1;
		for(int k=r+1;k<n;k++)
		    if(cm[k]<=r)
		    {
			rn=k;
			break;
		    }
		assert(rn!=-1);
		
		for(int k=rn;k>r;k--)
		    swap(cm[k],cm[k-1]);
		swaps+=rn-r;
	    }
		
	printf("Case #%d: %d\n",test_case,swaps);
    }
    return 0;
}
