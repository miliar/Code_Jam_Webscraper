#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<cmath>
#include<map>
#include<cstdlib>
#include<cstdio>
#include<climits>
#include<algorithm>
#include<cstring>

using namespace std;

#define PB(x) push_back(x)
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define VVI (vector<vector<int> >) 
#define FOR(I,A,B) for(int I=A;I<B;I++)
#define FORA(I,A,B) for(int I=A;I>B;I--)
#define SORT(x) sort(x.begin(),x.end())

int main(){
	VS vs;
	string s, x,y;
	int t,a,b;
	int f;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>a>>b;
		vs.clear();
		for(int i=0;i<a;i++){
			cin>>s;
			vs.PB(s);
		}
		f=1;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				if(vs[i][j]=='#'){
					if(i+1 < a && j+1 < b && vs[i][j]==vs[i][j+1] && vs[i][j]==vs[i+1][j+1] && vs[i][j]==vs[i+1][j] ){
						vs[i][j]='/';
						vs[i][j+1]='\\';
						vs[i+1][j+1]='/';
						vs[i+1][j]='\\';
					}else{
						f=0;
					}
				}
			}
		}
		if(f==0){
			cout<<"Case #"<<k<<":"<<endl<<"Impossible"<<endl;
		}else{
			cout<<"Case #"<<k<<":"<<endl;
			for(int i=0;i<a;i++){
				cout<<vs[i]<<endl;
			}
		}
	}
	return 0;
}
