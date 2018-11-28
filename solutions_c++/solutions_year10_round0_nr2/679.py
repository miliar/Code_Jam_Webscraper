#include<iostream>
#include<vector>
using namespace std;
int main(){
	vector<long long unsigned> t(1000);
	long long unsigned ans,gcd,in,gcdx;
	int c,n;
	cin>>c;
	for(int x=1;x<=c;x++){
		t.resize(0);
		cin>>n;
		for(int y=1;y<=n;y++){
			cin>>in;
			t.push_back(in);
		}
		sort(t.begin(),t.end());
		for(int y=1;y<=n;y++){
			//cout<<t[y-1]<<endl;
		}
		gcd=t[n-1]-t[0];
		for(int y=0;y<n;y++){
			for(int z=y+1;z<n;z++){
				if(t[y]!=t[z]){
					gcdx=t[z]-t[y];
					while((gcd%=gcdx)&&(gcdx%=gcd)){}
					gcd+=gcdx;
				}
			}
		}
		//cout<<gcd<<endl;
		if(t[0]%gcd==0)
			printf("Case #%d: 0\n",x);
		else{
			ans=(1+(t[0]/gcd))*gcd-t[0];
			printf("Case #%d: %llu\n",x,ans);
		}
	}

}
