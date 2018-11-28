#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;

bool f[111][111];
int T, TT;

int r;
int a1, a2, b1, b2;
int ans;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	cin>>T;
	for(int TT=1; TT<=T; ++TT){
		cin>>r;
		memset(f, false, sizeof(f));
		for(int k=0; k<r; ++k){
			cin>>a1>>b1>>a2>>b2;
			for(int i=a1; i<=a2;++i){
				for(int j=b1; j<=b2; ++j)
					f[i][j]=true;	
			}
		}
		ans=0;
		while (r){
			r=0;++ans;
			for(int i=100; i>=1; --i){
				for(int j=100; j>=1; --j){
					if (f[i][j]){
						if (!f[i-1][j]&&!f[i][j-1]) f[i][j]=false;	else ++r;
					} else {
						if (f[i-1][j]&&f[i][j-1]) {
								f[i][j]=true; ++r;
						}
					}
				}	
			}	
		//	cout<<ans<<"!!!!!"<<endl;
	//		for(int i=1; i<7; ++i)
	//	{		for(int j=1; j<7; ++j)
	//				cout<<f[i][j]<<" ";
//			cout<<endl;
//		}
		}

		cout<<"Case #"<<TT<<": "<<ans<<endl;	
	}
//	cin>>T;
}
