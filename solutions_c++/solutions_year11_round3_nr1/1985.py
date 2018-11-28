#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
#include <cstring>
using namespace std;

char pic[6][6];
int r,c;

bool blue_red()
{
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(pic[i][j]=='#' && i+1<r && j+1<c){
				pic[i][j]='/';
				pic[i][j+1]='\\';
				pic[i+1][j]='\\';
				pic[i+1][j+1]='/';
			}
			else if(pic[i][j]=='#' && (i+1>=r || j+1>=c  ||	pic[i][j+1]=='.'	|| pic[i+1][j]=='.' || pic[i+1][j+1]=='.' ))return false;
		}
	}
	return true;
}

int main()
{
	freopen("small.in","r",stdin);
	freopen("small.out","w",stdout);
	//freopen("large.in","r",stdin);
	//freopen("large.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>r>>c;
		string s;
		getline(cin,s);
		for(int j=0;j<r;j++){
			getline(cin,s);
			for(int k=0;k<c;k++)
			{
				pic[j][k]=s[k];
			}
		}
		if(blue_red()){
			cout<<"Case #"<<i<<":\n";
			for(int j=0;j<r;j++){
				for(int k=0;k<c;k++){
					cout<<pic[j][k];
				}
				cout<<endl;
			}
		}
		else cout<<"Case #"<<i<<":\nImpossible\n";
	}


	return 0;
}
