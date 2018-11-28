#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>

using namespace std;

int main() {
	int t,row,col;
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>row>>col;
		char pic[row][col];
		bool flag = true;
		for(int r=0;r<row;r++){
			for(int c=0;c<col;c++){
				cin>>pic[r][c];
			}
		}
		for(int r=0;r<row-1;r++){
			for(int c=0;c<col-1;c++){
				if(pic[r][c]=='#') {
					if(pic[r+1][c]=='#' && pic[r+1][c+1]=='#' && pic[r][c+1]=='#') {
						pic[r][c]='/';
						pic[r][c+1] = '\\';
						pic[r+1][c] = '\\';
						pic[r+1][c+1] = '/';
					}
					else {
						flag = false;
					}				
				}
			}
		}
		for(int r=0;r<row;r++) {
				for(int c=0;c<col;c++){
					if(pic[r][c]=='#') {
						flag = false;
						break;
					}
				}
		}
		cout<<"Case #"<<i<<":"<<endl;
		if(!flag)
			cout<<"Impossible"<<endl;
		else {
			
			for(int r=0;r<row;r++) {
				for(int c=0;c<col;c++){
					cout<<pic[r][c];
				}
				cout<<endl;
			}
		}
	}
}
