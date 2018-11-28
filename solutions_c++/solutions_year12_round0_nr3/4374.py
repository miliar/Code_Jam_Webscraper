#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int a,b;
		int ret=0;
		cin>>a>>b;
		for(int j=a;j<b;j++){
			for(int k=j+1;k<=b;k++){
				int c=j,d=k;
				if(c>=100){
					if(d<=999){
						if(c==d/10+(d%10)*100)ret++;
						else if(c==d/100+(d%100)*10)ret++;
					}
				}else if(c>=10){
					if(d<=99){
						if(c==d/10+(d%10)*10)ret++;
					}
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
	return 0;
}
