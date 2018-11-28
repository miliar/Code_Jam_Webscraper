#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
#include <cassert>
#include <complex>
using namespace std;

int main()
{
    freopen("in.in","rt",stdin);
    freopen("out.out","wt",stdout);

	int n;
	cin>>n;
	for (int i=0;i<n;i++) {
		int N,S,p;
		cin>>N>>S>>p;
		int cnt=0;
		for (int j=0;j<N;j++) {
			int points;
			cin>>points;
			if ((points+2)/3>=p)
				cnt++;
			else if (3*p-points<=4&&S>0&&points>=2) {
				S--;
				cnt++;
			}
		}
		printf("Case #%d: %d",i+1,cnt);
		if (i!=n-1) cout<<endl;
	}
    return 0;
} 