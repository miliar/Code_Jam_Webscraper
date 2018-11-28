#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
	int test; scanf("%d",&test);
	for(int tc = 1 ; tc <= test; tc++){
		int n,s,p; scanf("%d %d %d",&n,&s,&p);
		int arr[n];
		for(int i=0; i<n; i++) scanf("%d",&arr[i]);
		sort(arr,arr+n);
		int i = n-1;
		int res = 0;
		while(i >= 0){
			if(((int)ceil(arr[i]/3.0)) >= p){
				res++;
			} else if(((int)ceil(arr[i]/3.0)) == p - 1 && arr[i]%3 != 1 && s>0 && arr[i] != 0){
				res++;
				s--;
			} else if(((int)ceil(arr[i]/3.0)) <= p - 1){
				break;
			}
			i--;
		}
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}