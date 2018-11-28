#include <iostream>
#include <cstring>
#include <cmath>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <deque>
#include <queue>

#define min(a,b) (((a) < (b)) ? (a) : (b))
#define max(a,b) (((a) > (b)) ? (a) : (b))
using namespace std;
char a[101][101];
int r,c,t,i,j,k,fl;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    cin>>t;
    for(k=0;k<t;++k) {
        cin>>r>>c;
        for(i=0;i<100;++i)
            for(j=0;j<100;++j) a[i][j] = '%';
        for(i=0;i<r;++i)
            for(j=0;j<c;++j)
                cin>>a[i][j];
        cout<<"Case #"<<k+1<<":\n";
        fl=1;
        for(i=0;i<r && fl;++i)
            for(j=0;j<c && fl;++j)
                if (a[i][j]=='#'){
                    if (a[i+1][j]=='#' && a[i][j+1]=='#' && a[i+1][j+1]=='#') {
                        a[i][j]=a[i+1][j+1]='/';
                        a[i][j+1]=a[i+1][j]='\\';
                    }
                    else {cout<<"Impossible\n"; fl=0; break;}
                }
            if (fl){
                for(i=0;i<r;++i){
                    for(j=0;j<c;++j) cout<<a[i][j];
                    cout<<endl;
                }
            }

    }
	return 0;
}
