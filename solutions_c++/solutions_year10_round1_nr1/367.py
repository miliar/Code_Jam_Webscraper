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

char s[60][60];
int n, k, T, TT;
char a[60][60];
int f[60][60][4];
string ans;
int x, y;
map<char, bool> mp;

int main(){
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	cin>>T;
	for(int TT=1; TT<=T; ++TT){
		cin>>n>>k;
		mp['R']=mp['B']=false;
		memset(f, 0, sizeof(f));
		for(int i=0; i<60; ++i){
			for(int j=0; j<60; ++j)
				a[i][j]='\0';	
		}
		gets(s[0]);
		for(int i=0; i<n; ++i){
			gets(s[i]);	//cout<<s[i]<<endl;
		}
		for(int i=n-1; i>=0; --i){
			y=n-1-i; x=n-1;
			for(int j=n-1; j>=0; --j){
				if (s[i][j]!='.'){
					a[x][y]=s[i][j]; //cout<<x<<" "<<y<<" "<<a[x][y]<<endl;
					f[x][y][1]=f[x][y][2]=f[x][y][3]=f[x][y][0]=1;
					if (y!=0&&x<n-1){
						if (a[x+1][y-1]==a[x][y]) f[x][y][1]=f[x+1][y-1][1]+1;
					}
					if (y!=0){
						if (a[x][y-1]==a[x][y]) f[x][y][0]=f[x][y-1][0]+1;
					}
					if (y!=0&&x!=0){
						if (a[x-1][y-1]==a[x][y]) f[x][y][2]=f[x-1][y-1][2]+1;
					}
					if (x<n-1){
						if (a[x+1][y]==a[x][y]) f[x][y][3]=f[x+1][y][3]+1;	
					}
					for(int l=0; l<4; ++l)
						if (f[x][y][l]>=k) 
							mp[a[x][y]]=true;
					--x;
				}
			}	
		}
		//for(int i=0; i<n;++i)			printf("THI%s\n",a[i]);
		
		if (mp['R'])
			if (mp['B']) ans="Both"; else ans="Red";
		else if (mp['B']) ans="Blue"; else ans="Neither";		
		cout<<"Case #"<<TT<<": "<<ans<<endl;	
	}
	//cin>>T;
}
