/*
 * C.cpp
 *
 *  Created on: May 22, 2011
 *      Author: yassery
 */


#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

int a[1000];


int main(){
#ifndef ONLINE_JUDGE
	freopen("test.in","rt",stdin);
	freopen("test.txt","wt",stdout);
#endif

	int TC;
	cin >> TC;
	int N , L,H;
	for (int tt = 0; tt < TC; tt++) {

		printf("Case #%d: ",tt+1);
		cin>>N>>L>>H;
		for(int i=0;i<N;i++)
			cin>>a[i];

		for(int i=L;i<=H;i++){
			for(int j=0;j<N;j++){
				if(a[j]%i != 0 && i%a[j]!=0)
					goto WRONG;
			}
			printf("%d\n",i);
			goto NEXT;

			WRONG:;
		}

		printf("NO\n");
		NEXT:;
	}

	return 0;
}
