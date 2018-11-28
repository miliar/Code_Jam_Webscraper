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
using namespace std;

char a[52][52];
char ra[52][52];
char b[101][101];
char kb[52];
char kr[52];
int t,n,k;
bool red ;
bool blue ;
string ans;
void rotate();
void down();
void check(char * chr,bool &f);
void makestr();
int main() {
	freopen("f:\\a-small.in","r",stdin); freopen("f:\\a-small.out","w",stdout);
	//freopen("f:\\a-large.in","r",stdin); freopen("f:\\a=large.out","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n>>k;
		red = false;
		blue = false;
		for(int j=0;j<n;j++){
			cin>>a[j];
		}
		rotate();
		makestr();
		check(kr,red);
		check(kb,blue);
		if(red && blue) ans = "Both";
		else if(red) ans = "Red";
		else if(blue) ans = "Blue";
		else ans ="Neither";
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}

}
void rotate() {
	memset(b,0,sizeof(b));
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			b[j][n-i-1]=a[i][j];
		}
	}
	memset(a,0,sizeof(a));
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			a[i][j]=b[i][j];
		}
	}



	for(int i=0;i<n;i++){
		for(int j=n-2;j>=0;j--){
			if(a[j][i]=='.') continue;
			for(int k=j+1;k<n;k++){
				if( a[k][i]=='.'){
					a[k][i]=a[k-1][i];
					a[k-1][i]='.';
				} else break;
			}
		}
	}

}
void check(char * chr,bool &f) {
	for(int i=0;i<n;i++){
		if(strstr(a[i],chr)!=NULL) f=true;
	}
	if(f) return ;
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			b[i][j]=a[j][i];
		}
		b[i][n]='\0';
	}
	for(int i=0;i<n;i++){
		if(strstr(b[i],chr)!=NULL ) f=true;
	}
	if(f) return;
	memset(b,0,sizeof(b));
	int x,y,bx,by;
	for(int i=0;i<n;i++){
		x=i;
		y=0;
		bx=i;
		by=0;
		while(x>=0 && y<n){
			b[bx][by]=a[x][y];
			x-=1;
			y+=1;
			by+=1;
		}
	}
	for(int i=1;i<n;i++){
		x=n-1;
		y=1;
		bx=n+i-1;
		by=0;
		while(x>=0 && y<n){
			b[bx][by]=a[x][y];
			x-=1;
			y+=1;
			by+=1;
		}
	}
	for(int i=0;i<n*2;i++){
		if(strstr(b[i],chr)!=NULL) f=true;
	}
	if(f) return ;

	memset(b,0,sizeof(b));
	for(int i=n-1;i>=0;i--){
		x=i;
		y=0;
		bx=i;
		by=0;
		while(x<n && y<n){
			b[bx][by]=a[x][y];
			x+=1;
			y+=1;
			by+=1;
		}
	}
	for(int i=1;i<n;i++){
		x=0;
		y=i;
		bx=n+i-1;
		by=0;
		while(x>=0 && y<n){
			b[bx][by]=a[x][y];
			x+=1;
			y+=1;
			by+=1;
		}
	}
	for(int i=0;i<n*2;i++){
		if(strstr(b[i],chr)!=NULL) f=true;
	}
	if(f) return ;
}
void makestr() {
	for(int i=0;i<k;i++){
		kb[i]='B';
		kr[i]='R';
	}
	kb[k]='\0';
	kr[k]='\0';
	return;
}