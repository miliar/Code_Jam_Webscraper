/*
LANG: C++
TASK: rope
*/
#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

struct rope{
    int a,b;
};

rope r[1001];
int t,n,cnt;


int main(){
	freopen("A-large.in","r",stdin);
	freopen("rope.out","w",stdout);
	cin>>t;
	for(int i=0; i<t; i++){
	    cin>>n;
	    cnt=0;
	    for(int j=0; j<n; j++){
	        cin>>r[j].a>>r[j].b;
	    }
	    for(int j=0; j<n; j++){
	        for(int k=j+1; k<n; k++){
	            if((r[j].a<r[k].a && r[j].b>r[k].b) || (r[j].a>r[k].a && r[j].b<r[k].b)){
	                cnt++;
	            }
	        }
	    }
	    cout<<"Case #"<<i+1<<": "<<cnt<<endl;
	}
	return 0;
}
