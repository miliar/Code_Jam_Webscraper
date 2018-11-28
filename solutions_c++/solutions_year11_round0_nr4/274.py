#include <iostream>
#include <algorithm>

using namespace std;

const int MAXN = 1000;

int main(){
    double avg[1+MAXN];
    avg[0] = 0;
    avg[1] = 0; 
    for(int i=2;i<=MAXN;++i){
	avg[i] = 1 + avg[0] + avg[i-1];
	for(int j=2;j<i;++j){
	    avg[i] += ((1+avg[j]) + avg[i-j]);
	}
	avg[i] /= i-1;
    }
    
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp){
	int n;
	cin >> n;
	int a[1+MAXN];
	for(int i=1;i<=n;++i){
	    cin >> a[i];
	}
	
	double resp = 0;
	
	for(int i=1;i<=n;++i){
	    if(a[i] != 0){
		int k = 0;
		int j = i;
		while(a[j] != 0){
		    k++;
		    int nxt = a[j];
		    a[j] = 0;
		    j = nxt;
		}
		resp += (k==1) ? 0 : (1+avg[k]);
	    }
	}
	
	cout << "Case #" << lp << ": " << resp << "\n";
    }
    
    return 0;
}