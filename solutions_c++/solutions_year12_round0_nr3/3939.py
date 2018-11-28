#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int i;
int a, b, num;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin>>test;
	for (i=1;i<=test;i++){
		cout<<"Case #"<<i<<": ";
		cin>>a>>b;
		int n = 0;
		int pow = 1;
		int ans = 0;
		int aa=a;
		while (aa>0) {aa/=10;n++;pow*=10;}
		pow/=10;
		for (num = a;num<=b;num++){
		  set<int> dist;
		  int num1 = num;
		  for (int s=0;s<n-1;s++){
		    num1 = pow * (num1%10) + num1/10;
		    if (num1>num && num1<=b){
		      dist.insert(num1);
		      //cout<<num<<"  "<<num1<<endl;
		    }
		  }
		  ans+=dist.size();
		}
		cout<<ans<<endl;
	}
	return 0;
}
