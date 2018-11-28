#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <vector>
#include <stdlib.h>
#include <stdbool.h>
using namespace std;

/*m is a matrix of char where lines are possibles chars for that position*/
char m[5001][5001];
/*v is a vector where a store how many possibles chars for that postiion*/	 
int v[5001];

int main(){
	 int L,D,N,i,j,k,p,X,pos;
	 int Case=1;
	 vector<string> words;
	 string s,pattern;

	 bool equal;
	 scanf("%d %d %d",&L,&D,&N);
	 /*Ready the dictionary*/
	 for(i=0;i<D;i++){
		 cin>>s;
		 words.push_back(s);
	 }
	 /*Read the pattern*/
	 for(p=0;p<N;p++){
		 cin>>pattern;
		 memset(v,0,sizeof(v));
		 
		 pos=0;
		 /*parse to fill the matrix m*/
		 for(i=0;i<pattern.size();i++){
			 if(pattern[i]=='('){
				 i++;
				 /*Then I have multiple choices*/
				 while(pattern[i]!=')'){
					 m[pos][v[pos]++]=pattern[i];
					 i++;
				 }
			 }else{
				 m[pos][v[pos]++]=pattern[i];
			 }
			 pos++;
		 }
		 
		 X=0;
		 for(i=0;i<D;i++){
			for(j=0;j<L;j++){
				/* OR */
				equal=false;
				for(k=0;k<v[j];k++){
					if(words[i][j]==m[j][k]){
						equal=true;
						break;
					}
				}
				if(!equal) break;
			}
			if(j==L && equal) X++; 
		 }
		 
		printf("Case #%d: %d\n",Case++,X); 
	 }
	 return 0;
}
