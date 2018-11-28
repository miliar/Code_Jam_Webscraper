#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <list>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main()
{
	//freopen("test.txt","r",stdin);freopen("test.out","w",stdout);
	//freopen("C-small.in","r",stdin);freopen("C-small.out","w",stdout);
	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
    int N;
    cin >> N;
    long long sum=0;
    long long min=10*10*10*10*10*10+1;
    long long C=0;
    long long xsum=0;
    for(int i=0; i<N; i++) {
      cin >> C;
      sum += C;
      xsum ^= C;
      if(C < min) {
        min = C;
      }
    }
		printf("Case #%d: ",caseId);
    if (xsum == 0) {
      printf("%lld", sum-min);
    }
    else
		  printf("NO");
		printf("\n");
	}

	return 0;
}
