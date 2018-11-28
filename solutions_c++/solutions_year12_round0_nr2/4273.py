#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const long long MNAX=100000;


int main(){
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	long long n,i,j;
	int test;
	cin>>test;
	getchar();
	
	for (int t=1;t<=test;++t){
		cout<<"Case #"<<t<<": ";
		
		int n,s,p;
		cin>>n>>s>>p;
		int ans = 0;
		for (int i=0;i<n;++i){
			int tp;
			cin>>tp;
			int a1=tp/3,a2=tp/3,a3=tp/3;

			int maxSurp = a3;
			int maxNotSurp = a3;

			if (tp%3 == 0){
				if (tp!=0) ++maxSurp;
			}
			else if (tp%3 == 1){
				++maxNotSurp;
				maxSurp = -1;
			}
			else if (tp%3 == 2){
				++maxNotSurp;
				maxSurp += 2;
			}

			if (maxNotSurp>=p){
				++ans;
			}
			else{
				if (maxSurp>=p && s>0){
					++ans;
					--s;
				}
			}


		}

		cout<<ans<<'\n';
	}

	return 0;
}