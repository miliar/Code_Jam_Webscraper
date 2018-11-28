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



int main(){
	int casos,i,c,N;
	
	cin>>casos;
	for (c=0;c<casos;c++){
		cout<<"Case #"<<(c+1)<<": ";
		
		cin>>N;
		vector<int> x(N),y(N),r(N);
		for (i=0;i<N;i++){
			cin>>x[i]>>y[i]>>r[i];
		}
		double rta;
		if (N==1){
			rta=r[0];
		}else if (N==2){
			rta=max(r[0],r[1]);
		}else{
			rta=1e50;
			int i1,i2;
			for (i=0;i<3;i++){
				for (i1=0;i1<3;i1++) if (i1!=i) break;
				for (i2=i1+1;i2<3;i2++) if (i2!=i) break;
				
				double d=(r[i1]+r[i2]+pow((x[i1]-x[i2])*(x[i1]-x[i2])+(y[i1]-y[i2])*(y[i1]-y[i2]),0.5))/2.0;
				rta=min(rta,max(d,(double)r[i]));
			}
		}
		printf("%.9f\n",rta);
	}
	
	return 0;
}
