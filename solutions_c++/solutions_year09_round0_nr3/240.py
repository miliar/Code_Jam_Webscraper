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

const int maxlen=505;
const char* t = "welcome to code jam";

inline int res(int x)
{
    return x%10000;
}

int main(int argc,char* argv[])
{
    int tlen = strlen(t);

    int num_test_cases;
    scanf("%d ",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
	char s[maxlen];
	int slen;
	for(int i=0;;i++)
	{
	    assert(i<maxlen);
	    s[i]=getchar();
	    if(s[i]=='\n')
	    {
		slen=i;
		break;
	    }
	}

	int m[tlen+5];
	memset(m,0,sizeof(m));
	for(int i=0;i<slen;i++)
	{
	    for(int j=tlen-1;j>0;j--)
		if(s[i]==t[j])
		    m[j]=res(m[j]+m[j-1]);
	    if(s[i]==t[0])
		//m[0]=(m[0]<10000 ? m[0]+1 : 0);
		m[0]=res(m[0]+1);
	}
	printf("Case #%d: %04d\n",test_case,m[tlen-1]);
	
    }
    return 0;
}
