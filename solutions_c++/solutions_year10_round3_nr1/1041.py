#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <set>
#include <bitset>

#define FOR(A,B,C) for(int A=B;A<C;A++)
#define EFOR(A,B,C) for(int A=B;A<=C;A++)
#define RFOR(A,B,C) for(int A=B;A>=C;A--)
#define PB(A,B) A.push_back(B);
#define SORT(A) sort( A.begin(),A.end() )
#define ALL(A) A.begin(),A.end()
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define VB vector<bool>
#define SZ(A) int(A.size())
#define LL long long

using namespace std;

int main()
{
	freopen("A-large.txt","r",stdin);
	freopen("A-large Output.txt","w",stdout);

	int T;
	scanf("%d",&T);
	EFOR(cases,1,T){
		int N;
		cin>>N;
		VI left(N),right(N);
		FOR(inp,0,N)
			cin>>left[inp]>>right[inp];

		int cnt=0;
		FOR(i,0,N){
			FOR(j,i+1,N){
				if(left[i]<left[j] && right[i]>right[j])
					++cnt;
				if(left[i]>left[j] && right[i]<right[j])
					++cnt;
			}
		}

		printf("Case #%d: ",cases);
		cout<<cnt<<"\n";
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
