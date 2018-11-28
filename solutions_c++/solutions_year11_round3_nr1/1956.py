/*
LANG: C++
TASK: sqrtiles
*/

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;

int T,R,C;
string grid[52];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=1; i<=T; i++){
	    scanf("%d%d",&R,&C);
	    for(int j=0; j<51; j++){
	        grid[j]="";
	    }
	    char a;
	    for(int j=0; j<R; j++){
	        for(int k=0; k<C; k++){
                cin>>a;
                grid[j]+=a;
	        }
	    }
	    for(int j=1; j<R-1; j++){
	        for(int k=0; k<C-1; k++){
                if(grid[j][k]=='#' && grid[j][k+1]=='#' && grid[j-1][k]=='#' && grid[j-1][k+1]=='#'){
                    grid[j][k]='\\';
                    grid[j][k+1]='/';
                    grid[j-1][k]='/';
                    grid[j-1][k+1]='\\';
                }
                if(grid[j][k]=='#' && grid[j][k+1]=='#' && grid[j+1][k]=='#' && grid[j+1][k+1]=='#'){
                    grid[j][k]='/';
                    grid[j][k+1]='\\';
                    grid[j+1][k]='\\';
                    grid[j+1][k+1]='/';
                }
	        }
	    }
	    int flag=0;
	    for(int j=0; j<R; j++){
	        for(int k=0; k<C; k++){
	            if(grid[j][k]=='#') flag=1;
	        }
	    }
	    if(flag) cout<<"Case #"<<i<<": "<<endl<<"Impossible"<<endl;
	    else{
	        cout<<"Case #"<<i<<": "<<endl;
            for(int j=0; j<R; j++){
                for(int k=0; k<C; k++){
                    cout<<grid[j][k];
                }
                cout<<endl;
            }
	    }
	}
	return 0;
}
