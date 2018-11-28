#include <iostream>
#include <string.h>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int r,t,k,n,m[1000],in;
int tr[1000];//transformed
int ind[1000],used[1000];
int euros,moves;


int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    cin>>t;
    for(int i=0; i<t; i++){
        cin>>r>>k>>n;
        for(int j=0; j<n; j++){
            cin>>m[j];
        }
        int curr=0;//current
        euros=0;
        moves=0;
        for(int j=0; j<n;){
            curr=0;
            for(int l=0; l<n; l++){
                used[l]=0;
            }
            while(curr+m[j]<=k && j<n && !used[j]){
                curr+=m[j];
                used[j]=1;
                j++;
                j%=n;
            }
            //cout<<curr<<endl;
            euros+=curr;
            moves++;
            if(moves==r){
                cout<<"Case #"<<i+1<<": "<< euros<<endl;
                break;
            }
        }
    }
	return 0;
}
