
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
using namespace std;
int main(){
	int t,c;
	cin>>t;
	for(c=1;c<=t;c++){
		int a,b,i,n,m,f=0,ten=1,temp,cnt=0;
		cin>>a>>b;
		temp=a;
		while(temp){
			ten*=10;
			temp/=10;
		}
		ten/=10;
		for(i=a;i<=b;i++){
			n=i;
			m=n;
			f=1;
			int fl=0;
			while(1){
				m=m/10+(m%10)*ten;
				fl=1;
				if(m==n && fl==1)
					break;
				if(m<=b && m>n)
					cnt++;
			}
		}
		printf("Case #%d: %d\n",c,cnt);
	}
	return 0;
}
