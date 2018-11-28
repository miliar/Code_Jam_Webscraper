#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>

using namespace std;

bool check[101];
map<string,int> m;
char engine[101][101];
char query[1001][101];

int main(){

	int ans=0;
	int testcase;
	int E , Q;
	int last;

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d",&testcase);

	for(int i=1;i<=testcase;i++){

		scanf("%d\n",&E);
		
		for(int j=0;j<E;j++){
			gets(engine[j]);
			m[(string)engine[j]] = j;
		}

		scanf("%d\n",&Q);

		for(int j=0;j<Q;j++)
			gets(query[j]);

		int k;
		for(k=0;k<E;k++)
			check[k] = false;
		ans=0;

		for(int j=0;j<Q;j++){	//major

			check[m[(string)query[j]]] = true;
			last = m[(string)query[j]];

			for(k=0;k<E;k++)
				if(!check[k])
					break;

			if(k == E){
				for(k=0;k<E;k++)
					check[k] = 0;
				ans++;
				check[last] = true;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}

	return 0;
}


