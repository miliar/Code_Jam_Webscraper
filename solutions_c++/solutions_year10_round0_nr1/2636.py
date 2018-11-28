#include<iostream>
#include<math.h>
#include<fstream>
#include<sstream>
using namespace std;

bool isLightOn(int N,int K){
	int factor=(int)pow(2.0,N);
			if((K+1)%factor==0)
				return true;
			else
				return false;
}
void main(){
	int N,num;	
	int K;
	ifstream in("A-large.in");
	ofstream out("output.txt");
	stringstream ss;
	std::string temp;
	if(in.good()){
		in>>num;
		for(int i=0;i<num&&in.good();i++){			
			in>>N>>K;
			if((N>=1&&N<=30)&&(K>=0&&K<=pow(10.0,8))){				
				if(isLightOn(N,K))
					temp=std::string("ON");	
				else
					temp=std::string("OFF");			
			}
			else{
				temp=std::string("Invalid Input");
			}					
			out<<"Case #"<<i+1<<": "<<temp.c_str()<<"\n";								
		}
	}
	else{
		 out<<"\nCannot open file";
	}

}


/*while(1){
	do{
	cout<<"\nEnter number of Snappers: ";
	cin>>N;
	if(N==-1)
		exit(0);
	}while(N<1&&N>100);
	do{
	cout<<"\nEnter number of finger snaps: ";
	cin>>K;
	}while(K<0&&K>100);*/