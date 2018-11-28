#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<vector>
using namespace std;
#define f(i,n) for(int i=0;i<n;i++)
#define vi vector<int>
#define vii vector< vi >
int x1=0;
int min(int x,int y){
	if(x<y)
		return x;
	else
		return y;
}

int cal(int i,int j,vii &v ,vii &u){

	if(u[i][j]!=-1)
		return u[i][j];
	else{
		int x=min(v[i][j+1],v[i+1][j]);
		int y=min(x,v[i][j-1]);
		int z=min(y,v[i-1][j]);
		//	cout<<i<<"  "<<j<<endl;
		if(v[i-1][j]==z && v[i-1][j]<v[i][j])
			u[i][j]=cal(i-1,j,v,u);
		else if(y==v[i][j-1] && v[i][j-1]<v[i][j])
			u[i][j]=cal(i,j-1,v,u);
		else if(z==v[i][j+1] && v[i][j+1]<v[i][j])
			u[i][j]=cal(i,j+1,v,u);
		else if(v[i+1][j]<v[i][j])
			u[i][j]=cal(i+1,j,v,u);
		else{
			u[i][j]=x1;
			x1++;
		//	cout<<i<<"  "<<j<<endl;
		//	cout<<"hjdd";
		}
		return u[i][j];
	}
}





int main(){
	ifstream fin;
	ofstream fout;
	int a=1;
	fin.open("input.txt");
	fout.open("output.txt");
	int t,h,w;
	fin>>t;
	while(t--){
		fout<<"Case #"<<a<<":"<<endl;
		a++;
		fin>>h>>w;
		vector<vector<int> >v(h+2,vector<int>(w+2,1000000));
		vii u(h+2,vi(w+2,-1));
		x1=0;
		for(int  i=1;i<=h;i++)
			for(int j=1;j<=w;j++)
			fin>>v[i][j];
		//cout<<v.size()<<" "<<v[0].size()<<endl;
		
		for(int  i=1;i<=h;i++){
			for(int j=1;j<=w;j++)
			fout<<(char)('a'+cal(i,j,v,u))<<" ";
			fout<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}



		
