#include <iostream>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>

using namespace std;

int m[]={1,10,100,1000,10000,100000,1000000,10000000};

int main()
{
	int t,a,b,x;
	string str;
	cin>>x;
	for(int y=1;y<=x;y++){
		cin>>a>>b;
		int ans=0;
		for(int i=a;i<=b;i++){
			ostringstream ost;
			ost<<i;
			int len=ost.str().length();
			int k=i;
			for(int j=1;j<len;j++){
				k=(k%m[len-1])*10+k/m[len-1];
				if(k>i && k<=b){
					ans++;
				}
			}
		}
		cout<<"Case #"<<y<<": "<<ans<<endl;
	}
}