#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;
string s[11];
int a[11][1050];
int maxh,maxw;
int main(){
	int t,cnt;
	int n,m; //mrows ncolums
	cin>>t;
	//scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		cin>>m>>n;
		memset(a,0,sizeof(a));
		for(int i=0;i<m;i++)
			cin>>s[i];
		maxh=(1<<m);maxw=(1<<n);
		for(int j=0;j<maxh;j++){
			cnt=0;
			for(int i=0;i<m;i++)
			if(s[i][0]=='.' && (1<<i)&j)cnt++;
			a[0][j]=cnt;
			//cout<<cnt<<endl;
		}
		//cout<<"here"<<endl;
		for(int i=1;i<n;i++){
			for(int j=0;j<maxh;j++){ //combination of curr col
				//cout<<" "<<j<<endl;
				for(int k=0;k<maxh;k++){ //combination of prev col
					//cout<<"  "<<k<<endl;
					cnt=0;
					for(int ii=0;ii<m;ii++)
					if(s[ii][i]=='.'&& (1<<ii)&j){
						if( (ii-1>=0 && (k&(1<<(ii-1)))) || ( ii+1<m && (k&(1<<(ii+1)))) || (k&(1<<ii))){
							//dummy;
						}
						else{
							cnt++;
						}
					}
					a[i][j]=max(a[i][j],cnt+a[i-1][k]);
				}
			}
		}
		cnt=0;
		for(int i=0;i<n;i++)
		for(int j=0;j<maxh;j++)
			cnt=max(cnt,a[i][j]);
		//printf("Case #%d: %d\n",tc,res);
		cout<<"Case #"<<tc<<": "<<cnt<<endl;
	}
	return 0;
}
