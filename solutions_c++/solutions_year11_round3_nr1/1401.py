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

	int test,i,j,r,c,k;
	char str[100][100];
	freopen("E:\\codejam\\A-large.in","r",stdin);
	freopen("E:\\codejam\\A-large.txt","w",stdout);
	
	scanf("%d",&test);
	int count=0;
	for(i=0;i<test;i++){
		memset(str,'0',sizeof(str));	
		scanf("%d %d\n",&r,&c);
		
		for(j=1;j<=r;j++){
			for(k=1;k<=c;k++)
				scanf("%c",&str[j][k]);
			getchar();
		}
		int flag=0;
		for(j=1;j<=r;j++){
			for(k=1;k<=c;k++){
				if((str[j][k]=='#')){
					if((str[j][k+1]=='#')&&(str[j+1][k]=='#')&&(str[j+1][k+1]=='#')){
						str[j][k]='/';
						str[j][k+1]='\\';
						str[j+1][k]='\\';
						str[j+1][k+1]='/';
					}
					else{
						flag=1;
						break;
					}
				}
			}
			if(flag==1)break;
		}
		if(flag==1){
			cout<<"Case #"<<i+1<<":"<<endl;
			cout<<"Impossible"<<endl;
		}
		else{
			cout<<"Case #"<<i+1<<":"<<endl;
			for(j=1;j<=r;j++){
				for(k=1;k<=c;k++)
					printf("%c",str[j][k]);
				cout<<endl;
			}
		}
	}
	return 0;
}