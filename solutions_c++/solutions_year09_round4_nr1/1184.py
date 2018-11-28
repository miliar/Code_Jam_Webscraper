#include <vector>
#include <cstdio>
#include <iostream>
#include <map>
#include <algorithm>
#include <queue>
using namespace std;

map<vector<string>,int> mapa;
bool sirve(vector<string>& cad,int & N){
      for(int i=0;i<N;i++)
	for(int j=i+1;j<N;j++) if(cad[i][j]=='1') return false;
    return true;
      
}
int main(){
    int N,T;
    cin>>T;
    for(int t=1;t<=T;t++){
	cin>>N;
	mapa.clear();
	vector<string> ini(N);
	for(int i=0;i<N;i++) cin>>ini[i];
	mapa[ini]=0;
	queue<vector<string> > q;
	q.push(ini);
	int res=-1;
	while(!q.empty()){
	   vector<string> u=q.front();q.pop();
	   
	   if(sirve(u,N)){ res=mapa[u];break;}
	   for(int i=1;i<N;i++){
	     vector<string> v=u;
	     swap(v[i],v[i-1]);
	     if(mapa.find(v)==mapa.end()){
	      mapa[v]=mapa[u]+1;
	      q.push(v);
	     }
	   }
	}
	cout<<"Case #"<<t<<": "<<res<<endl;
    }
}