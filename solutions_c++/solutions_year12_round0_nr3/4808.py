/*
 * main.cpp
 *
 *  Created on: 2012.04.14.
 *      Author: Peti
 */

#include<iostream>
#include<fstream>
#include<sstream>

using namespace std;

int osszehasonlit(int N, int M){
	int megfelelo=0;
	stringstream ss,sss;
	string n,uj,m;
	int i,j;
	ss<<N;
	ss>>n;
	//cout<<"a "<<n<<"\n";
	sss<<M;
	sss>>m;
	//cout<<"b "<<m<<"\n";
	if(n.length()==m.length()){
		for(i=0;i<int(n.length());i++){
			uj=n;
			for(j=0;j<int(n.length());j++){
				if((j+i)>=n.length()){
					uj[j+i-n.length()]=n[j];
				}else{
					uj[j+i]=n[j];
				}
			}
			//cout<<uj<<"=="<<m<<"? ";
			if(uj==m){
				megfelelo=1;
				//cout<<"igen\n";
			}else{
				//cout<<"nem\n";
			}
		}
	}
	if(megfelelo){
		return 1;
	}else{
		return 0;
	}
}

int main(){
	stringstream ss;
	string s;
	int a,b,n,m,sorok,i;
	ifstream inp("be.txt");
	getline(inp,s);
	ss<<s;
	ss>>sorok;
	int eredmeny[sorok];
	stringstream ss2[sorok];
	/*int x[7];
	int y;*/
	for(i=0;i<sorok;i++){
		getline(inp,s);
		ss2[i]<<s;
		ss2[i]>>a>>b;
		eredmeny[i]=0;
		for(n=a;n<b;n++){
			/*y=a;
			x[0]=y/1000000;
			y-=x[0]*1000000;
			x[1]=y/100000;
			y-=x[1]*100000;
			x[2]=y/10000;
			y-=x[2]*10000;
			x[3]=y/1000;
			y-=x[3]*1000;
			x[4]=y/100;
			y-=x[4]*100;
			x[5]=y/10;
			y-=x[5]*10;
			x[6]=y/1;
			y-=x[6]*1;
			int j;
			int elso;
			for(j=0;j<7;j++){
				if(x[j]==0) elso=j+1;
			}
			int igaz=1;
			for(j=elso;j<6;j++){
				if(x[j]<=x[j+1]){
					igaz=0;
				}
			}
			if(!igaz){*/
				for(m=n+1;m<=b;m++){
					eredmeny[i]+=osszehasonlit(n,m);
				}
			//}
		}
	}
	ofstream op("Output.txt");
	for(i=0;i<sorok;i++){
		cout<<"Case #"<<i+1<<": "<<eredmeny[i]<<"\n";
		op<<"Case #"<<i+1<<": "<<eredmeny[i]<<"\n";
	}
	inp.close();
	op.close();
}


