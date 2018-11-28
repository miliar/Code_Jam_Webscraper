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
char str[5003][17],text[1000];
int res,len,D;
void reset(){}
void FA(int k,int i,int j,bool inside,bool taken){


	if(j>=len) {res++;return;}
	if(text[i]=='('){
		FA(k,i+1,j,true,false);
		return ;
	}
	else if(text[i]==')'){
		FA(k,i+1,j,false,false);
		return ;
	}
	if(inside){
	
		if(taken)
			FA(k,i+1,j,true,true);
		else if(text[i]==str[k][j])
			FA(k,i+1,j+1,true,true);
		else FA(k,i+1,j,true,false);
	
	}
	else {
	
		if(text[i]==str[k][j])
			FA(k,i+1,j+1,false,true);
	}

}
void process(){

	res=0;
	for(int i=0;i<D;i++)
	{
		len=strlen(str[i]);
		FA(i,0,0,false,false);
	}

}
int main()
{
	//freopen("contest/in.txt","r",stdin);
	freopen("contest/A-large.in","r",stdin);
	freopen("contest/out.txt","w",stdout);	
	
	int i,cas=1,L,N;
	scanf("%d%d%d",&L,&D,&N);

	for(i=0;i<D;i++){	
		scanf("%s",str[i]);	
	}
	
	while(N--){
	
		scanf("%s",text);
		
		process();
		printf("Case #%d: %d\n",cas++,res);
	
	}
	return 0;
}
