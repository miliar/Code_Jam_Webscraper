#include<iostream>
#include<string>
#include<fstream>
using namespace std;
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
*/
int main(){
	
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int te;
	cin>>te;
	
	for(int test=1; test<=te; test++){
		int n,s,p, ans=0;
		cin>>n>>s>>p;
		for(int i=0; i<n; i++){
			int sum;
			cin>>sum;
			if( sum>= p*3-2)
				ans++;
			else if(s && sum >= 3*max(0, p-2) +2){
				ans++;
				s--;
			}
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	return 0;
}
