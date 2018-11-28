#include<iostream>
using namespace std;
int check(int mem[],int n,int j){
	for(int i=0;i<n;++i){
		if(mem[i]==0&&i!=j)
			return 0;
	}
	return 1;
}
int find(string f,string engine[],int n){
	//cout<<"comparing "<<f<<" with ";
	for(int i=0;i<n;++i){
		//cout<<"\""<<engine[i]<<"\" ";
		if(engine[i]==f)
			return i;
	}
	return -1;
}
int main(){
	int h;
	cin>>h;
	for(int i=0;i<h;++i){
		//cout<<h<<endl;
		int n,m;
		cin>>n;
		string engine[n+1];
		getline(cin,engine[0]);
		for(int j=0;j<n;++j){
			getline(cin,engine[j]);
			//cout<<engine[j]<<endl;
		}
		cin>>m;
		//cout<<m<<endl;
		string query[m+1];
		getline(cin,query[0]);
		for(int j=0;j<m;++j){
			getline(cin,query[j]);
		}
		//cout<<"hi";
		int mem[n],j=0,ret=0;
		memset(mem,0,sizeof(mem));
		while(j<m){
			int temp=find(query[j],engine,n);
			//cout<<temp<<" "<<query[j]<<endl;
			if(temp>=0){
				//cout<<"asdas";
				if(check(mem,n,temp)){
					++ret;
					memset(mem,0,sizeof(mem));
					mem[temp]=1;
				}
				else{
					mem[temp]=1;
				}
			}
			//cout<<"asdas";
			++j;
		}
		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
}
