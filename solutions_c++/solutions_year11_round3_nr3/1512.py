#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>

using namespace std;

int a[100];

bool harmony(int x, int y)
{
  int t;
  if(y>x) {
    t = x;
    x = y;
    y = t;
  }

  if(x%y==0)
    return true;
  else
    return false;
}


int main()
{
	//freopen("test.txt","r",stdin);freopen("test.out","w",stdout);
	freopen("C-small.in","r",stdin);freopen("C-small.out","w",stdout);
	//freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
	int testcase;
	cin >> testcase;
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		int N, L, H;
    cin >> N >> L >> H;

    for(int i=0; i!=N; i++) {
      cin >> a[i];
    }
    
    bool h;
    int x;
    for(x=L; x<=H; x++) {
      h=true;
      for(int i=0; i!=N; i++) {
        h &= harmony(x, a[i]);
        if(!h)
          break;
      }
      if(h) 
        break;
    }
		printf("Case #%d: ",caseId);
    if(h)
		  printf("%d\n",x);
    else
      printf("NO\n");
    
	}

	return 0;
}
