//author:- viper_yash
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <sstream>
#include <ctype.h>
#include <utility>
#include <cstdlib>

using namespace std;

#define ll long long
#define md1 1000000007ll
#define md2 10000007ll
#define linf 998877665544332211ll
#define inf 987654321ll
#define fillchar(a,i) memset(a,i,sizeof(a))
#define rev(s) string(s.rbegin(),s.rend())
#define read(f) freopen(f, "r", stdin)
#define write(f) freopen(f, "w", stdout)
#define unq(v) unique(v.begin(),v.end(),v.end())
#define maxe(v) max_element(v.begin(),v.end())
#define mine(v) min_element(v.begin(),v.end())
#define rep(i,n) for(int i=0;i<n;i++)
#define per(i,n) for(int i=n-1;i>=0;i--)
#define fnd(v,val) find(v.begin(), v.end(),val)
#define cont(v,val) count (v.begin(),v.end(),val)
#define revrse(v) reverse(v.begin(),v.end())
#define replce(v,x,y) replace (v.begin(), v.end(), x, y)
#define remv(v,val) remove(v.begin(), v.end(),val)
#define acc(v) accumulate(v.begin(),v.end(), 0)
int gcd(int a,int b) {return b?gcd(b,a%b):a;}


struct node{
	int x;
	int y;
	double z;
	string ss;

};
typedef struct node yash;

bool my_fun(yash a,yash b){
    if(a.x<b.x)
        return 1;
    else if(a.x==b.x){
        return (a.y<b.y);
    }
    else
        return 0;
}

int Z = 0;

int evaluate(vector< vector<char> > grid,int pos, int qos, char ch) {
	int cnt = 0;
	for(int i = 0; i < 4; i++){
		if(grid[i][qos] == ch || grid[i][qos] == 'T'){
			cnt++;
			if(cnt == 4)
				return cnt;
		}
		else
			break;
	}
	cnt = 0;
	for(int i = 0; i < 4; i++){
		if(grid[pos][i] == ch || grid[pos][i] == 'T'){
			cnt++;
			if(cnt == 4)
				return cnt;
		}
		else
			break;
	}
	cnt = 0;
	if(pos == qos){
		if((grid[0][0] == ch || grid[0][0] == 'T') && (grid[1][1] == ch || grid[1][1] == 'T') && (grid[2][2] == ch || grid[2][2] == 'T') && (grid[3][3] == ch || grid[3][3] == 'T')){
			cnt = 4;
			return cnt;
		}
	}
	if((pos == 1 && qos==2) || (pos==2 && qos==1) || (pos==3 && qos==0) || (pos==0 && qos==3)){
		if((grid[3][0] == ch || grid[3][0] == 'T') && (grid[2][1] == ch || grid[2][1] == 'T') && (grid[1][2] == ch || grid[1][2] == 'T') && (grid[0][3] == ch || grid[0][3] == 'T')){
			cnt = 4;
			return cnt;
		}
	}
	return 0;
}
int main(){
	int t;
	cin>>t;
	for(int f = 1; f <= t; f++){
		int flag=0,flagx=0,flago=0;
		char ch;
		vector<vector<char> >grid(4,vector<char>(4,'c'));
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> ch;
				grid[i][j] = ch;
			}
		}
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(grid[i][j] == '.')
					flag = 1;
				if(grid[i][j] == 'X')
					flagx = evaluate(grid,i,j,grid[i][j]);
				if(grid[i][j] == 'O')
					flago = evaluate(grid,i,j,grid[i][j]);
			}
			if(flagx == 4 || flago == 4)
				break;
		}
        if(flagx == 4)cout<<"Case #"<<f<<": "<< "X won"<<endl;
        if(flago == 4)cout <<"Case #"<<f<<": "<< "O won" << endl;
        if(flagx != 4 && flago != 4) {
			if(flag == 1)cout<<"Case #"<<f<<": "<<"Game has not completed"<<endl;
		}
		if(flagx != 4 && flago != 4){
			if(flag == 0)cout <<"Case #"<<f<<": "<< "Draw" << endl;
		}
	}
	return 0;
}