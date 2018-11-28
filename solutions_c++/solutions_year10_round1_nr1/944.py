// 2010A.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <cassert>
#include <cmath>
#include <string>
#include <set>
using namespace std;
char chess[60][60];
char newchess[60][60];

int n,k;
bool find(int x,int y, char c){
	bool res = true;
	if(x==5&&y==2)
		res = true;
	for(int i=0; i<k; i++){
		if(y+i>=n)
			{res = false;break;}
		if(newchess[x][y+i]!=c){
			res = false;
			break;
		}
	}
	if(res==true)
		return true;
	res = true;
	for(int i=0; i<k; i++){
		if(x+i>=n)
			{res = false;break;}
		if(newchess[x+i][y]!=c){
			res = false;
			break;
		}
	}
	if(res==true)
		return true;
	res = true;
	for(int i=0; i<k; i++){
		if(y+i>=n)
			{res = false;break;}
		if(x+i>=n)
			{res = false;break;}
		if(newchess[x+i][y+i]!=c){
			res = false;
			break;
		}
	}
	if(res==true)
		return true;
	res = true;
	for(int i=0; i<k; i++){
		if(y-i<0)
			{res = false;break;}
		if(x+i>=n)
			{res = false;break;}
		if(newchess[x+i][y-i]!=c){
			res = false;
			break;
		}
	}
	if(res==true)
		return true;
	return false;
}
int  solve(){
	memset(newchess,'\0',sizeof(newchess));

     for(int i=0; i<n; i++){
		 int t = n-1;
			for(int j=n-1; j>=0; j--){
				if(t<0) {newchess[i][j]='*'; continue;}
				if(chess[i][t]=='.'){ 
					t--;
					j++;
					continue;
				}
				if(chess[i][t]=='R'||chess[i][t]=='B'){
					newchess[i][j] = chess[i][t];
					t--;
				}
			}
     }
	 //for(int i=0; i<n; i++){
		// for(int j=0; j<n; j++){
		//	printf("%c",newchess[i][j]);
		// }
		// printf("\n");
	 //}
	 int r1 = 0;
	 int r2 = 0;
	 for(int i=0; i<n; i++){
		 for(int j=0; j<n; j++){
			if(find(i,j,'B'))
				r1 = 1;
			if(find(i,j,'R'))
				r2 = 2;
		 }
	 }
	 return r1+r2;
}
int main(int argc, char *argv[])
{
    freopen("A-large2.in","r",stdin);
 //    freopen("B-large-practice (1).in","r",stdin);
    freopen("out.txt","w",stdout);
      
    int T;

    scanf("%d",&T);
    
    int CASE = 1;
    while(T--)
    {


          scanf("%d %d\n",&n,&k);
          memset(chess,'\0',sizeof(chess));
          for(int i=0; i<n; i++){
              for(int j=0; j<n; j++){
                    scanf("%c",&chess[i][j]);  
              }        
              char tmp;
              scanf("%c",&tmp);
          }
          int res = solve();
		  if(res==0)
			  printf("Case #%d: Neither\n",CASE);
		  if(res==1)
			  printf("Case #%d: Blue\n",CASE);
		  if(res==2)
			  printf("Case #%d: Red\n",CASE);
		  if(res==3)
			  printf("Case #%d: Both\n",CASE);
          CASE++;     
    }

    return 0;
}
