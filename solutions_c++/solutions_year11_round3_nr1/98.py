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
#include <string>

using namespace std;



void doit(){
	int n,m;
	int ni, nj;
	bool pos=true;
	char c='\\';
	string s[55];
	cin>>n>>m;
	//cout<<c<<endl;
	for(int i=0;i<n;i++)
		cin>>s[i];
	for(int i=0;i<n;i++)
	for(int j=0;j<m;j++)
	if(s[i][j]=='#'){
		ni=i+1;nj=j+1;
		if(ni<n && nj<m){
			if(s[i+1][j]!='#' || s[i+1][j+1]!='#' || s[i][j+1]!='#')
				pos=false;
			else{
				s[i][j]=s[i+1][j+1]='/';
				s[i+1][j]=s[i][j+1]=c;
			}
		}
		else
			pos=false;
	}
	if(!pos){
		cout<<endl<<"Impossible"<<endl;
	}
	else{
		for(int i=0;i<n;i++)
			cout<<endl<<s[i];
		cout<<endl;
	}
	return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<":";
        doit();
    }
    return 0;
}

