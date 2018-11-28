#include <iostream>

using namespace std;
int rotate(int x,int c) {
	int nr,n = 0,num = 0,k,v[100],i = 0;
	    

	    nr = x;
	    
	    k=c;
	    
	    while (nr){
	        v[i] = nr%10;
	        num++;
	        nr/=10;
	        i++;
	    }
	    
	    for (i = k-1;i >= 0;i--){
	            n = n*10+v[i];
	    }
	    for (i = num-1;i >= k;i--) {
	    n = n*10+v[i];
	    }
	    return n;
}
int main() {
 freopen ("A-small.in","r",stdin);
    freopen ("A-small.out","w",stdout);
	int t,a,b;
	int out=0;
	cin >> t;
	int x=1;
	while (x<t+1) {
		cin >> a >> b;
		int a1=a;
		while (a1<b) {
			int a2=rotate(a1,1);
			int f=2;
			while (a2!=a1) {
				if (a2>a1 and a2<=b) {
					out++;
				}
				a2=rotate(a1,f);
				f++;
			}
			a1++;
		}
		cout << "Case #" << x << ": " << out << endl;
		out=0;
		x++;
	}
	
}