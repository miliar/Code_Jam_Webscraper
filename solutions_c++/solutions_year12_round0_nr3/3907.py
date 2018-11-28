#include <iostream>

using namespace std;

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int n;
	cin >> n;
	for(int t=0;t<n;t++){
		int res=0;
		int a,b;
		cin >> a >> b;
		int m=1;
		while(m<=b)m*=10;
		for(int k=a;k<=b;k++){
			int x=0;
			int y=k;
			y=(y*10)/m+(y*10)%m;
			while(y!=k){
				if(y>=a && y<=b && y>=k)x++;
				y=(y*10)/m+(y*10)%m;
			}
			res+=x;
		}
		cout << "Case #" << t+1 << ": " << res << "\n";
	}

	return 0;
}