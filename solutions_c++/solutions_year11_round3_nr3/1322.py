#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;
#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
 
#define pi acos( -1 )
#define eps 1e-9
 
#define max( a, n ) ( ( a ) > ( n ) ? ( a ) : ( n ) )
#define min( a, n ) ( ( a ) < ( n ) ? ( a ) : ( n ) )
#define pb push_back
#define inf 1 <<28

int main(void){
	
	int i,n,l,h,j,a[1000],test,k;
	freopen("E:\\codejam\\C-small-attempt0.in","r",stdin);
	freopen("E:\\codejam\\C-small-attempt0.txt","w",stdout);

	scanf("%d",&test);
	for(i=0;i<test;i++){
		
		scanf("%d %d %d",&n,&l,&h);
		for(j=0;j<n;j++) scanf("%d",&a[j]);
		int flag1=0;
		for(k=l;k<=h;k++){
			
			int flag=0;
				
			for(j=0;j<n;j++){
				if((a[j]%k!=0)&&(k%a[j]!=0)){
					flag=1;
					break;
				}
			}
			if(flag==0){
				cout<<"Case #"<<i+1<<": "<<k<<endl;
				flag1=1;
				break;
			}
		}
		if(flag1==0)
			cout<<"Case #"<<i+1<<": NO"<<endl;
	}
	return 0;
}