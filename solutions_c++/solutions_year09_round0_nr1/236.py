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

const int lmax=17,dmax=5005;
char w[dmax][lmax];			// words
bool p[lmax][300];			// p[i][ch] is true if letter i of the pattern can be ch
int l,d;

bool possibleWord(int k)
{
    for(int i=0;i<l;i++)
	if(!p[i][w[k][i]])
	    return false;
    return true;
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d %d %d ",&l,&d,&num_test_cases);
    for(int i=0;i<d;i++)
	scanf("%s ",w[i]);
    
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	memset(p,false,sizeof(p));
	for(int i=0;i<l;i++)
	{
	    char ch = getchar();
	    if(ch == '(')
		while((ch = getchar()) != ')')
		    p[i][ch]=true;
	    else
		p[i][ch]=true;
	    scanf(" ");
	}

	int count=0;
	for(int k=0;k<d;k++)
	    if(possibleWord(k))
		count++;
	printf("Case #%d: %d\n",test_case,count);
    }
    return 0;
}
