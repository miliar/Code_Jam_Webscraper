#include<iostream.h>
#include<fstream.h>
#include<stdlib.h>
#include<iomanip.h>
#include<string.h>
#include<math.h>


//文件与输出
//ifstream fin("A-small-attempt1.in",ios::in);ofstream fout("A-small-practice.out",ios::out);
ifstream fin("A-large.in",ios::in);ofstream fout("A-large-practice.out",ios::out);

#define cin fin
#define cout fout


int state(int N,int K){
	int yushu;
	for(int i=0;i<N;i++){
		yushu=K%2;
		if(yushu==0)return 0;
		K=K/2;
	}
	return 1;
}

void f(int time){
	int N,K;
	cin>>N>>K;

	int s=state(N,K);
	cout<<"Case #"<<time<<": ";
	if(s==1)cout<<"ON"<<endl;
	else cout<<"OFF"<<endl;
}

void main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++)f(i+1);
}