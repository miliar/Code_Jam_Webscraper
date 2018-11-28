#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <set>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef multiset<char>::iterator iter;

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	char n[25];
	n[0] = '0';
	scanf("%s",n+1);
	int l=strlen(n);

	multiset<char> d;
	d.insert(n[l-1]);

	for(int i=l-2;;i--)
	{
	    assert(i>=0);
	    d.insert(n[i]);
	    iter it = d.upper_bound(n[i]); // first element in d that is greater than n[i]
	    if(it != d.end())
	    {
		n[i] = *it;
		d.erase(it);

		iter it2 = d.begin();
		for(int j=i+1;j<l;j++)
		    n[j] = *it2++;

		break;
	    }
	}

	printf("Case #%d: %s\n",test_case,n[0]=='0' ? n+1 : n);
	
    }
    return 0;
}
