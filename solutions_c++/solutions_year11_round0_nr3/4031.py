#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<algorithm>
#include<memory.h>
#include<iomanip>
#include<cmath>
#include<fstream>
#include<map>
#include<ctime>
#include<queue>
using namespace std;

int main()
{
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("out1.txt","w",stdout);
	int t,n,p[1005],i,j;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>n;
		for(i=0;i<n;i++){
			cin>>p[i];
		}
		int ans=0;
		for(i=1;i<(1<<n)-1;i++){
			int a=0,b=0,sa=0,sb=0;
			for(j=0;j<n;j++){
				if((i>>j) & 1){
					a=a^p[j];
					sa+=p[j];
				}else{
					b=b^p[j];
					sb+=p[j];
				}
			}
			if(a==b && sa>ans){
				ans=sa;
			}
		}
		if(ans!=0)
			cout<<"Case #"<<k<<": "<<ans<<endl;
		else
			cout<<"Case #"<<k<<": NO"<<endl;
	}
	return 0;
}