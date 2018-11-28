#include<iostream>
#include<fstream>
#include<string>
#include <stdlib.h> 
 using namespace std;

int main(){
ifstream in("x.in");
ofstream out("y.out");
if(in.is_open())
while(!in.eof()){
int n;
in>>n;
for(int i=0;i<n;i++){
int N,PD,PG;
in>>N;
in>>PD;//cout<<PD<<endl;
in>>PG;
bool b=false;if(PG==0&&PD==0)b=true;
for(int j=1;j<=N;j++){
	if(b)break;
float wd=j*((float)PD/100);//cout<<j<<"   "<<wd<<endl;
if(wd-(int)wd==0){//cout<<j<<"   "<<wd<<endl;
	for(int k=0;k<100;k++){//if(b)break;
	float G=k*100/(float)PG;
	if(G-(int)G==0&&G!=0){//cout<<k<<"   "<<G<<endl;
	if(PG==100&&PD<100)break;
	if(k*100/G==PG&&wd*100/j==PD)
	b=true;
	}// if g
	}// for k
}// if wd


}//for j

if(b)out<<"Case #"<<(i+1)<<": "<<"Possible"<<endl;else {out<<"Case #"<<(i+1)<<": "<<"Broken"<<endl;}
}//end for i 



}// end while 

return 0;
}//end main



/*
int* A=new int[arraynum];// must delete
delete [] A;

getline(in,s);
int a=atoi(s.c_str());
getline(in,s);
int c=atoi(s.c_str());



*/