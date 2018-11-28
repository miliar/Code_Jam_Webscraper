#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>

using namespace std;
bool bac[105][105], newbac[105][105];
void doit(){
	int r, xa, ya, xb, yb, res=0;
	bool bact=true;
	cin>>r;
	memset(bac,0,sizeof(bac));
	for(int i=0;i<r;i++){
		cin>>xa>>ya>>xb>>yb;
		for(int x=xa;x<=xb;x++)
		for(int y=ya;y<=yb;y++)
			bac[x][y]=true; 
	}
	while(bact){
		bact=false;
		res++;
		memset(newbac,0,sizeof(newbac));
		for(int x=101;x>0;x--)
		for(int y=101;y>0;y--){
			if(bac[x][y] && (bac[x-1][y] || bac[x][y-1])){
				newbac[x][y]=true;
				bact=true;
			}
			if(bac[x-1][y] && bac[x][y-1]){
				newbac[x][y]=true;
			}
		}
		memcpy(bac,newbac,sizeof(newbac));
	}
	cout<<res<<endl;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}

