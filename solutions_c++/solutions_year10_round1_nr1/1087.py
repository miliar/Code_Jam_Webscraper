
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
	vector <string> vs,nvs;
	int n,k,mem[51][51][2][4];

void doit(){
	string str;
	int tmprow;
	bool blue=false,red=false;
	vs.clear();nvs.clear();
	memset(mem,0,sizeof(mem));
	cin>>n>>k;
	for(int i=0;i<n;i++){
		cin>>str;
		vs.push_back(str);
		nvs.push_back(str);
	}
	for(int i=0;i<n;i++)
	for(int j=0;j<n;j++){
		nvs[i][j]=vs[n-1-j][i];
	}
	for(int i=n-1;i>=0;i--){
	for(int j=0;j<n;j++){
		if(nvs[i][j]=='.'){
			tmprow=i;
			while(tmprow>=0 && nvs[tmprow][j]=='.')tmprow--;
			if(tmprow>=0){
				nvs[i][j]=nvs[tmprow][j];
				nvs[tmprow][j]='.';
			}
		}
	}
	}
	for(int i=0;i<n;i++)
	for(int j=0;j<n;j++){
		if(nvs[i][j]=='B'){
			if(j-1>=0) mem[i][j][1][0]=mem[i][j-1][1][0]+1; else mem[i][j][1][0]=1; 
			if(i-1>=0)mem[i][j][1][1]=mem[i-1][j][1][1]+1; else mem[i][j][1][1];
			if((i-1>=0) && (j-1>=0))mem[i][j][1][2]=mem[i-1][j-1][1][2]+1; else mem[i][j][1][2]=1; 
			if((i-1>=0) && (j+1<n))mem[i][j][1][3]=mem[i-1][j+1][1][3]+1; else mem[i][j][1][3]=1; 
		}
		if(nvs[i][j]=='R'){
			if(j-1>=0) mem[i][j][0][0]=mem[i][j-1][0][0]+1; else mem[i][j][0][0]=1;
			if(i-1>=0) mem[i][j][0][1]=mem[i-1][j][0][1]+1; else mem[i][j][0][1]=1;
			if((i-1>=0) && (j-1>=0))mem[i][j][0][2]=mem[i-1][j-1][0][2]+1; else mem[i][j][0][2]=1;
			if((i-1>=0) && (j+1<n))mem[i][j][0][3]=mem[i-1][j+1][0][3]+1; else mem[i][j][0][3]=1;
		}
	}
	for(int i=0;i<n;i++)
	for(int j=0;j<n;j++)
	for(int l=0;l<4;l++){
		if(mem[i][j][0][l]>=k)red=true;
		if(mem[i][j][1][l]>=k)blue=true;

	}
	str="";
	if(blue && red)str="Both";
	else if(blue)str="Blue";
	else if(red)str="Red";
	else str="Neither";
	cout<<str<<endl;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}

