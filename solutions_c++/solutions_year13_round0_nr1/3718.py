#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#define rep(i,m) for(int i=0;i<(int)(m);i++)
using namespace std;
int T;int arr[4][4];
bool diag(int n){return ((arr[0][0]==n||arr[0][0]==3)&&(arr[1][1]==n||arr[1][1]==3)&&(arr[2][2]==n||arr[2][2]==3)&&(arr[3][3]==n||arr[3][3]==3)||(arr[0][3]==n||arr[0][3]==3)&&(arr[1][2]==n||arr[1][2]==3)&&(arr[2][1]==n||arr[2][1]==3)&&(arr[3][0]==n||arr[3][0]==3));}
bool row(int m,int n){return (arr[m][0]==n||arr[m][0]==3)&&(arr[m][1]==n||arr[m][1]==3)&&(arr[m][2]==n||arr[m][2]==3)&&(arr[m][3]==n||arr[m][3]==3);}
bool col(int m,int n){return (arr[0][m]==n||arr[0][m]==3)&&(arr[1][m]==n||arr[1][m]==3)&&(arr[2][m]==n||arr[2][m]==3)&&(arr[3][m]==n||arr[3][m]==3);}
int main(){
freopen("A-large.in","rt",stdin);
freopen("A-large.out","wt",stdout);
cin >> T;
char tmp;
rep(tt,T){bool ncmpl=false;
	rep(i,4){
		rep(j,4){
			cin >> tmp;
			switch(tmp){
				case '.':arr[i][j]=0;ncmpl=true;break;
				case 'X':arr[i][j]=1;break;
				case 'O':arr[i][j]=2;break;
				case 'T':arr[i][j]=3;break;
				}
			}
		}
	cout<<"Case #"<<(tt+1)<<": ";
	if(diag(1)||row(0,1)||row(1,1)||row(2,1)||row(3,1)||col(0,1)||col(1,1)||col(2,1)||col(3,1))cout <<"X won\n";
	else if(diag(2)||row(0,2)||row(1,2)||row(2,2)||row(3,2)||col(0,2)||col(1,2)||col(2,2)||col(3,2))cout <<"O won\n";
	else if(ncmpl)cout<<"Game has not completed\n";
	else cout<<"Draw\n";
	}
}
