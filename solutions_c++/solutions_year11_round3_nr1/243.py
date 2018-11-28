#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
 
#define rei(i,a,b) for(int i=a;i<b;i++)
#define red(i,a,b) for(int i=a;i>=b;i--)
#define ree(i,a,b) for(int i=a;i<=b;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define pb(a,x) a.push_back(x)
#define all(a) a.begin(),a.end()
#define srt(a) sort(all(a))
#define rev(a) reverse(all(a))
 
int main(){
	int test;
	scanf("%d",&test);
	ree(t,1,test){
		printf("Case #%d:\n",t);
		int r,c;
		scanf("%d%d",&r,&c);
		vector<string> mat(r,"");
		rei(i,0,r) cin>>mat[i];
		rei(i,0,r){
			rei(j,0,c){
				if(mat[i][j]=='#' ){
					if(j+1<c){
						if(mat[i][j+1]=='#'){
							if(i+1<r){
								if(mat[i+1][j]=='#' && mat[i+1][j+1]=='#'){
									mat[i][j]='/',mat[i][j+1]='\\',mat[i+1][j]='\\',mat[i+1][j+1]='/';
								}
							}
						}
					}
				}
			}
		}
		bool p=true;
		rei(i,0,r) rei(j,0,c) if(mat[i][j]=='#') p=false;
		if(!p){
			printf("Impossible\n");
			continue;
		} 
		rei(i,0,r) cout<<mat[i]<<endl;
	}
	return 0;
}
