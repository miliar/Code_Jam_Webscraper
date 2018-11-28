#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>

#include "windows.h"
using namespace std; 
char s[1000];
int xyz[26][26];
int mat[26][26];
int main()   
{   
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,c,d,n,i,j;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		memset(xyz,-1,sizeof(xyz));
	    scanf("%d",&c);
		for(i=0;i<c;i++){
		    scanf("%s",s);
			int x=s[0]-'A',y=s[1]-'A',z=s[2]-'A';
			xyz[x][y]=z;xyz[y][x]=z;
		}
		scanf("%d",&d);
		memset(mat,0,sizeof(mat));
		for(i=0;i<d;i++){
		    scanf("%s",s);
			int x=s[0]-'A',y=s[1]-'A';
			mat[x][y]=mat[y][x]=1;
		}
		scanf("%d%s",&n,s);
		string ss="";
		for(i=0;i<n;i++){
			if(ss!=""){
				int x=ss[ss.length()-1]-'A',y=s[i]-'A';
				if(xyz[x][y]!=-1){
				    ss[ss.length()-1]=char(xyz[x][y]+'A');
				}
				else {
					bool find=0;
					for(int k=0;k<ss.length();k++){
						if(mat[ss[k]-'A'][y]){
							find=1;
							break;
						}
					}
					if(find)ss="";
					else ss+=s[i];
				}
			}
			else ss+=s[i];
		}
		printf("Case #%d: [",test);//[E, A]
		for(i=0;i<ss.length();i++){
		    if(i)printf(", ");
			printf("%c",ss[i]);
		}
		puts("]");

	}
	
}   
