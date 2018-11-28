#include <iostream>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>

using namespace std;
#define MAXA 100000000
//vector <int> a,b;
int a[10],b[10],asize,bsize;
int main(){
	int t,n,tmp,res;
	int bga,bgb,ena,enb;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		asize=0;
		bsize=0;
		res=MAXA;
		scanf("%d",&n);
		//cout<<n<<endl;
		for(int i=0;i<n;i++){
			scanf("%d",&a[i]);
		}
		for(int i=0;i<n;i++){
			scanf("%d",&b[i]);
		}
		sort(a,a+n);
		sort(b,b+n);
		do{
			tmp=0;
			for(int i=0;i<n;i++){
				tmp+=(a[i]*b[i]);
			}
			if(tmp<res)res=tmp;
		}while(next_permutation(a,a+n));
		printf("Case #%d: %d\n",tc,res);
		//cout<<"Case #"<<tc<<": "<<res<<endl;
	}
	return 0;
}