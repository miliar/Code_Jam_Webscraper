#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

#define INF 100000

int N;

int main(){
	int casos,i,j,c;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<(c+1)<<": ";
		cin>>N;
		
		vector<int> abajo(N,0);
		string tmp;
		for (i=0;i<N;i++){
			cin>>tmp;
			
			for (j=0;j<N;j++) if (tmp[j]=='1') abajo[i]=j;
			//cout<<i<<" "<<abajo[i]<<endl;
		}
		int rta=INF;
		vector<int> p(N);
		vector<int> queda(N);
		for (i=0;i<N;i++) p[i]=i;
		do{
			for (i=0;i<N;i++) queda[i]=abajo[p[i]];
			for (i=0;i<N;i++) if(queda[i]>i) break;
			if (i==N){
				int tot=0;
				int a,b;
				for (a=0;a<N;a++) for (b=a+1;b<N;b++) if (p[a]>p[b]) tot++;
				rta=min(rta,tot);
			}
		}while (next_permutation(all(p)));
		
		cout<<rta<<endl;
	}
	
	return 0;
}
