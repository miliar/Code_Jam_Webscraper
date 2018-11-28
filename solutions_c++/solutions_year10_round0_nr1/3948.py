#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <deque>
#include <queue>
#include <bitset>
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
#include <cstring>
#include <ctime>

using namespace std;

int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);

	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	//freopen("input","r",stdin);
	//freopen("output","w",stdout);
	
	int numcases;
	long n,k;
	scanf("%d",&numcases);
	for (int cid = 1; cid <= numcases; cid++) {
		printf("Case #%d: ",cid);
		scanf("%li%li",&n,&k);
	 	if(k < n) printf("OFF\n");
		else {
			if(k==(pow(2,n)-1)) printf("ON\n");
			else if(k%(long(pow(2,n)))==(long(pow(2,n))-1)) printf("ON\n");
			else printf("OFF\n");
		}
	}
	return 0;
}
