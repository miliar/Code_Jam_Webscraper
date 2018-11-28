#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

unsigned candy[1000];
unsigned maxval;

void subset(int n,int s)
{
	unsigned realval=0;
	unsigned falseval1=0;
	unsigned falseval2=0;
	for(int i=0;i<n;i++){
		if(s&(1<<i)){
			realval+=candy[i];
			falseval1^=candy[i];
		}else falseval2^=candy[i];
		
	}
	if(realval>maxval&&
		falseval1==falseval2&&
		falseval1!=0)
		maxval=realval;
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);

	int n;
	cin>>n;

	for(int i=0;i<n;i++){
		int num;
		cin>>num;

		for(int j=0;j<num;j++){
			cin>>candy[j];
		}

		maxval=0;
		for(int j=0;j<(1<<num);j++){
			subset(num,j);
		}

		cout<<"Case #"<<i+1<<": ";
		if(maxval>0)cout<<maxval<<endl;
		else cout<<"NO"<<endl;
	}

	return 0;
}