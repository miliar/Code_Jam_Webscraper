#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
using namespace std;

char buf[111];
int main(){
	int T,n,tests=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		vector<int> a;
		for(int i=0;i<n;i++){
			scanf("%s",buf);
			int last=0;
			for(int j=n-1;j>=0;j--)
				if(buf[j]=='1'){
					last=j;
					break;
				}
			a.push_back(last);
		}
		int ret=0;
		for(int j=0;j<n;j++){
			int pos=-1;
			for(int k=0;k<a.size();k++)if(a[k]<=j){
				pos=k;
				break;
			}
			assert(pos!=-1);
			a.erase(a.begin()+pos);
			ret+=pos;
		}
		printf("Case #%d: %d\n",++tests,ret);
	}
}
