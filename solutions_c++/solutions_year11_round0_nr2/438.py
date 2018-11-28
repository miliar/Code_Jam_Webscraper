#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

int maps[512][512];
int maps2[512][512];
int main(){
    freopen("F://B-large.in","r",stdin);
    freopen("F://B-large.out","w",stdout);
	int t ;
	scanf("%d",&t);
	for(int cases =1 ; cases <= t ;++cases){
		memset(maps,0,sizeof(maps));
		memset(maps2,0,sizeof(maps2));
		int c , d , n ; 
		char a ,b ,x ; 
		scanf("%d",&c);
		for(int i = 0 ; i<c;++i){
			scanf(" %c%c%c",&a,&b,&x);
			maps[a][b] = x ; 
			maps[b][a] = x ;
		}
		scanf("%d",&d);
		for(int i = 0 ; i<d ;++i){
			scanf(" %c%c",&a,&b);
			maps2[a][b] = 1 ; 
			maps2[b][a] = 1 ;
		}
		scanf("%d",&n);
		string tres = "";
		int len = 0; 
		for(int i = 0 ; i<n ;++i){
			scanf(" %c",&a);
			if( len != 0 ){
				if( maps[a][tres[len-1]] > 1 )tres[len-1] = maps[a][tres[len-1]] ;
				else {tres += a ;len++;} 
			}
			else { tres += a ; len++;}
			bool fl = 0 ; 
			for(int j = 0 ; j <len&&fl == 0  ;++j)
				for(int k = j ; k <len&&fl == 0  ;++k)
					if( maps2[tres[j]][tres[k]] == 1 ) 
						fl = 1 ; 
			if( fl == 1 ) len = 0,tres = "" ; 
		}
		string res = "[";
		for(int i = 0 ; i< len - 1; ++i){
			res += tres[i] ;
			res += ", ";
		}
		if( len != 0 ) {
			res += tres[len-1];
			res += "]";
		}
		else res+= "]";
		printf("Case #%d: ",cases);
		cout<<res<<endl;
	}
	return 0 ;
}