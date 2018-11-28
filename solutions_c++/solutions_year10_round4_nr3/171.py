#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
int ma[2][120][120];
int main()
{
	int i,j,k,l,r,t,x1,x2,y1,y2;vector <int> out;
	cin>>t;
	for(i=0;i<t;i++){
		memset(ma,0,sizeof(ma));
		cin>>r;
		for(j=0;j<r;j++){
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			for(k=x1;k<=x2;k++) for(l=y1;l<=y2;l++) ma[0][k][l]=1;
		}
		for(j=1;j<=250;j++){
			int f=0;
			for(k=1;k<110;k++) for(l=1;l<110;l++){
				if(ma[(j-1)%2][k][l]==0){
					if(ma[(j-1)%2][k-1][l]==1 && ma[(j-1)%2][k][l-1]==1) ma[j%2][k][l]=1;
					else ma[j%2][k][l]=0;
				}
				else{
					if(ma[(j-1)%2][k-1][l]==1 || ma[(j-1)%2][k][l-1]==1) ma[j%2][k][l]=1;
					else ma[j%2][k][l]=0;
				}
				if(ma[j%2][k][l]==1) f++;
			}
			if(f==0){out.pb(j);break;}
		}
	}
	for(i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
