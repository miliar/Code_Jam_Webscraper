#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;
#define MODV 10007
int a[102][102];
bool ok[102][102];
int main(){
	int t;
	int h,w,r,rw,cl;
	cin>>t;
	//scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		memset(a,0,sizeof(a));
		memset(ok,1,sizeof(ok));
		a[1][1]=1;
		cin>>h>>w>>r;
		for(int i=0;i<r;i++)
		{
			cin>>rw>>cl;
			ok[rw][cl]=false;
		}
		for(int i=1;i<=h;i++) 
		for(int j=1;j<=w;j++)
		if(ok[i][j]){
			if(i-2>=1 && j-1>=1)
				a[i][j]+=a[i-2][j-1];
			if(i-1>=1 && j-2>=1)
				a[i][j]+=a[i-1][j-2];
			a[i][j]%=MODV;
		}
		//printf("Case #%d: %d\n",tc,res);
		cout<<"Case #"<<tc<<": "<<a[h][w]<<endl;
	}
	return 0;
}
