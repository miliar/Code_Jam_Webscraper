#include <iostream>
#include <vector>
#include <string>
using namespace std;

#define ulli unsigned long long int
#define lli long long int

#define f(i,n) for(ulli i = 0; i < n; i++)


int main(){
	int ntc = 0;
	cin>>ntc;
	
	f(tc,ntc){
		ulli r, k, n;
		cin >>r >>k >>n;
		ulli g[n];
		ulli sum[n];
		f(i,n){
			cin >> g[i];
			if(i)
				sum[i]=sum[i-1]+g[i];
			else
				sum[i]=g[i];
		}
		ulli p = 0;
		ulli amt = 0;
		f(j,r){
			if(g[p]>k) break;
			if(sum[n-1]<=k){
				amt+=sum[n-1];
				continue;
			}
			if(p>0){
				ulli diff = sum[n-1]-sum[p-1];
				if(diff<=k){
					f(i,n){
						if(sum[i] + diff > k){
							p = i;
							amt += diff;
							if(i)
								amt += sum[i-1];
							break;
						}
					}
				} else {
					for(ulli i = p; i < n; i++){
						if(sum[i]-sum[p-1]>k){
							amt = amt+sum[i-1]-sum[p-1];
							p = i;
							break;
						}
					}
				}
			} else{
				f(i,n){
					if(sum[i]>k){
						amt+= sum[i-1];
						p = i;
						break;
					}
				}
			}
		}
		cout << "Case #"<<tc+1<<": "<<amt<<endl;
	}
	return 0;
}
