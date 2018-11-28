//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------

#define INF  (1<<30)
#define EPS  1e-10
#define pb   push_back
#define sz   size()
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLEAR(A,N)  (memset(A,0,(N)*sizeof(A[0])))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))

template<class Type>
Type Maximum(Type a,Type b){
	return (a>b)?a:b;
}
template<class Type>
Type Maximum(Type a,Type b,Type c){
	Type t=(a>b)?a:b;
	return (c>t)?c:t;
}
template<class Type>
Type Minimum(Type a,Type b){
	return (a<b)?a:b;
}
template<class Type>
Type Minimum(Type a,Type b,Type c){
	Type t=(a<b)?a:b;
	return (c<t)?c:t;
}
//--------------------------------------------------------
int ar[105][105],fil[105][105],H,W,color;
void reset(){
	
	int i,j;
	CLR(fil);
	for(i=0;i<=H;i++)
		ar[i][0]=INF;

	for(i=0;i<=H;i++)
		ar[i][W+1]=INF;

	for(i=0;i<=W;i++)
		ar[0][i]=INF;

	
	for(i=0;i<=W;i++)
		ar[H+1][i]=INF;

}
int findMin(int i,int j){

	int m=INF;
	m=Minimum(ar[i][j-1],m);
	m=Minimum(ar[i][j+1],m);
	m=Minimum(ar[i-1][j],m);
	m=Minimum(ar[i+1][j],m);
	return m;
}
int floodfil(int i,int j){

	if(fil[i][j]) 
		return fil[i][j];
	int cl,m=findMin(i,j);

	if(m>=ar[i][j]) return fil[i][j]=color;

	if(ar[i-1][j]==m)
		cl=floodfil(i-1,j);
	else if(ar[i][j-1]==m)
		cl=floodfil(i,j-1);
	else if(ar[i][j+1]==m)
		cl=floodfil(i,j+1);
	else cl=floodfil(i+1,j);
	
	return fil[i][j]=cl;
}
void process(){

	int cl,i,j;
	color=1;
	for(i=1;i<=H;i++)
		for(j=1;j<=W;j++)
		{
			cl=floodfil(i,j);
			color=Maximum(color,cl+1);
		}
	
		for(i=1;i<=H;i++){
			for(j=1;j<=W;j++){
				if(j>1)
					printf(" ");
				printf("%c",'a'-1+fil[i][j]);
			}
			printf("\n");
		}
}
int main()
{
	//freopen("contest/B/B-large.in","rt",stdin);
	//freopen("contest/B/out.txt","w",stdout);	
	
	
	int i,t,j,cas=1;
		cin>>t;
		while(t--){
		
			cin>>H>>W;
			reset();
			for(i=1;i<=H;i++)
				for(j=1;j<=W;j++)
					cin>>ar[i][j];
			printf("Case #%d:\n",cas++);
			process();

		}		
	return 0;
}
