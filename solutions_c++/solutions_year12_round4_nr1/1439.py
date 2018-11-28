#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;
int dist[10001];
int length[10001];
int D;
int N;
bool swing(int position,int vine_id){
	int reach=min(dist[vine_id]-position,length[vine_id])+dist[vine_id];
	if(reach>=D){
		return true;	
	}
	if(vine_id==N-1){// the last vine and can not reach the target!
		return false;
	}
	if(reach<dist[vine_id+1]){// can not reach the next target
		return false;
	}
	int i;
	for(i=vine_id+1;i<N;i++){
		if(reach>=dist[i]){
			if(swing(dist[vine_id],i)){
				return true;
			}
		}
	}
	return false;
}
/*
bool swing(){
	int position=0;
	if(dist[0]>length[0]){
		return false;
	}
	int vine=0;
	int new_vine;
	int reach=dist[0]*2;
	cout<<"vine:"<<vine<<endl;
	if(reach>=D){
		return true;
	}
	while(true){
		int i;
		int optimal;
		for(i=vine;i<N;i++){
			if(reach>=dist[i]){
				optimal=i;
			}
		}
		if(i==N){
			if(reach>=D){
				return true;
			}
		}
		new_vine=optimal;
		cout<<"new vine:"<<new_vine<<endl;
		if(new_vine==vine){
			return false;
		}
		reach=min(dist[new_vine]-dist[vine],length[new_vine])+dist[new_vine];
		vine=new_vine;
		cout<<"reach:"<<reach<<endl;
	}
}*/
int main(){
	ifstream fin;
	fin.open("E:\\codejam\\input.txt");
	ofstream fout;
	fout.open("E:\\codejam\\output.txt");
	int T;
	fin>>T;
	for(int t=1;t<=T;t++)
	{
		fin>>N;
		for(int i=0;i<N;i++){
			fin>>dist[i];
			fin>>length[i];
		}
		fin>>D;
		bool reach=swing(0,0);
		if(reach==true){
			cout<<"Case #"<<t<<": "<<"YES"<<endl;
			fout<<"Case #"<<t<<": "<<"YES"<<endl;
		}
		else{
			cout<<"Case #"<<t<<": "<<"NO"<<endl;
			fout<<"Case #"<<t<<": "<<"NO"<<endl;
		}
	}
	fout.close();
	return 0;
}