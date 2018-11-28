#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
using namespace std;

int main(){
	int T;
	string temp;
	cin>>T;

	for(int t=0;t<T;t++){
		int N;
		vector<char> bot;
		vector<int> button;
		cin>>N;
		for(int n=0;n<N;n++){
			char a;
			int b;
			cin>>a>>b;
			bot.push_back(a);
			button.push_back(b);
		}
//		for(int n=0;n<N;n++) cout<<setw(3)<<bot[n];cout<<endl;
//		for(int n=0;n<N;n++) cout<<setw(3)<<button[n];cout<<endl;
		int op=1,bp=1,time=0,step=0,conf,inc,os=-1,bs=-1,dn=0;
		for(int n=0;n<N;n++){
			if(os==-1 && bot[n]=='O') os=n;
			if(bs==-1 && bot[n]=='B') bs=n;
		}

		while(step!=N){
//			cout<<step<<"  ";
//			cout<<"O("<<op<<","<<os<<")"<<" ";
//			cout<<"B("<<bp<<","<<bs<<")"<<endl;
			conf=false;
			inc=false;

			if(os==N)
				dn++;
			else if(bot[step]=='O' && op==button[step] && !conf){	//Push button
				inc=true;
				conf=true;
				for(os=os+1;os<N;os++)
					if(bot[os]=='O')
						break;
			} else if (op<button[os])
				op++;
			else if (op>button[os])
				op--;

			if(bs==N)
				dn++;
			if(bot[step]=='B' && bp==button[step] && !conf){ //Push button
				inc=true;
				conf=true;
				for(bs=bs+1;bs<N;bs++)
					if(bot[bs]=='B')
						break;
			} else if (bp<button[bs])
				bp++;
			else if (bp>button[bs])
				bp--;

			if(inc) step++;
			time++;
		}
		cout<<"Case #"<<(t+1)<<": "<<time<<endl;
	}
}
