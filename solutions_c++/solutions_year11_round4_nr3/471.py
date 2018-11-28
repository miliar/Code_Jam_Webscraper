#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<string>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<fstream>
#include<sstream>

using namespace std;


int main(){
	int tn;cin>>tn;
	for(int ttn=1;ttn<=tn;ttn++){
		cout<<"Case #"<<ttn<<": ";
		int n;cin>>n;
		int num[1010];memset(num,0,sizeof(num));
		for(int i=2;i<=n;i++){
			int tmp=i;
			for(int j=2;;j++){
				int tt=0;
				while((tmp!=1) && (tmp%j==0)){
					tmp/=j;
					tt++;
				}
				num[j]=max(tt,num[j]);
				if(tmp==1)break;
			}
		}
		int ans=0;
		for(int i=0;i<1010;i++){
			if(num[i]>0)ans+=num[i]-1;
		}
		if(n!=1)ans++;
		cout<<ans<<endl;
	}
	return 0;
}
