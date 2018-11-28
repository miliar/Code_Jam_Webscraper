									/*	In the name of God	*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <sstream>
#include <bitset>
#include <map>
#include <set>
#include <queue>
#include <stack>

#define rep(i,n) for((i)=0;(i)<(n);(i)++)
typedef long long ll;

using namespace std;

int a[10001];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);	
	int ti,tc,i,j,k,s,p,n,r;
	cin>>tc;
	rep(ti,tc){
		cin>>n>>s>>p;
		r=0;
		rep(i,n){
			cin>>k;
			if (k/(double)3+.9>=p)
				r++;
			else if (s>0 && k>0){
				if (k%3==2 && k/3+2>=p){
					r++;s--;
				}
				if (k%3==0 && k/3+1>=p){
					r++;s--;
				}
			}
		}
		printf("Case #%d: %d\n",ti+1,r);
	}
	
	return 0;
}