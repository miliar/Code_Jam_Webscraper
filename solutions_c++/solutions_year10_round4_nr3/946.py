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
#include <stdlib.h>
#include <ctime>
#include <fstream>

using namespace std;

int n,X1,Y1,X2,Y2;
int a[200][200];
int b[200][200];
int ans;
bool notEnd() ;
void flowToB();
void moveToB();
void moveToA();
void clearB();
void pr();
int main() {
	freopen("f:\\c-small.in","r",stdin); freopen("f:\\c-small.out","w",stdout);
	//freopen("f:\\a-large.in","r",stdin); freopen("f:\\a-large.out","w",stdout);
	int t,ans;
	cin>>t;
	for(int j=1;j<=t;j++){
		cout<<"Case #"<<j<<": ";
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		cin>>n;
		for(int i=0;i<n;i++) {
			cin>>Y1>>X1>>Y2>>X2;
			for(int mm=X1;mm<=X2;mm++) {
				for(int nn=Y1;nn<=Y2;nn++) {
					a[mm][nn]=1;
				}
			}
		}
		ans=0;
		
		while(notEnd() ) {
			clearB();
			flowToB();
			pr();
			moveToB();
			pr();
			moveToA();
			pr();
			ans++;
			
//			cout<<ans<<endl;
		}
		cout<<ans<<endl;
	}
}
void pr() {
	return;
	for(int i=0;i<7;i++) {
		for(int j=0;j<7;j++) {
			cout<<b[i][j];
		}
		cout<<endl;
	}
	cout<<"*************"<<endl;
}
void clearB() {
	memset(b,0,sizeof(b));
}
void moveToB() {
	for(int i=0;i<103;i++) {
		int x=i-1;
		if(x<0) continue;
		for(int j=0;j<103;j++) {
			int y=j-1;
			if(y<0) continue;
			if(a[i][j]==0) continue;
			if(a[x][j]==0 && a[i][y]==0) continue;
			b[i][j]=1;
		}
	}
}
void moveToA() {
	memset(a,0,sizeof(a));
	for(int i=0;i<103;i++) {
		for(int j=0;j<103;j++) {
			if(b[i][j]==1) {
				a[i][j]=1;
			}
		}
	}
}
void flowToB() {
	for(int i=0;i<103;i++) {
		int x=i-1;
		if( x<0) continue;
		for(int j=0;j<103;j++) {			
			int y=j-1;
			if(y<0) continue;
			if(a[x][j]==1 && a[i][y]==1) {
				b[i][j]=1;
			}
		}
	}

}
bool notEnd() {
	for(int i=0;i<=102;i++) {
		for(int j=0;j<103;j++) {
			if(a[i][j]==1) return true;
		}
	}
	return false;
}