#include<iostream>
#include<string>
#include<fstream>
#include<map>
#include<set>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<queue>

using namespace std;

int ret(int x,int y,int turn){
	if(y==0)return turn;
	if(x<y)swap(x,y);
	if(x/y!=1)return turn;
	return ret(y,x%y,turn+1);
}

int main(){
	int tn=0;cin>>tn;
	for(int ttn =1;ttn<=tn;ttn++){
		int a1,a2,b1,b2;cin>>a1>>a2>>b1>>b2;
		long long cnt=0;
		for(int i=a1;i<=a2;i++){
			for(int j=b1;j<=b2;j++){
				if(ret(i,j,0)%2==0)cnt++;
			}
		}
		cout<<"Case #"<<ttn<<": "<<cnt<<endl;
	}
}
