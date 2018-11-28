#include <stdio.h>
#include <iostream>
using namespace std;
int main(){
	FILE *file;
	int Num;
	file=fopen("A-large.in","r");
	
	if(file==NULL){
		cout<<"read file error!"<<endl;
		exit(0);
	}
	char ch=0;
	string input_line="";

	while(true){
		ch=fgetc(file);
		if(ch=='\n'){
			break;		
		}else{
			input_line+=ch;		
		}	
	}	
	Num=atoi(input_line.c_str());

	for(int i=0;i<Num;i++){
		
		int N;
		long long K;
		ch=0;
		input_line="";
		while(true){
			ch=fgetc(file);
			if(ch==' '){
				break;		
			}else{
				input_line+=ch;		
			}			
		}
		
		N=atoi(input_line.c_str());
		
		ch = 0;
		input_line = "";
		int count=0;
		long long temp=0;
		
		while(true){
			count++;
			
			ch = fgetc(file);
			if(ch == '\n'){
				break;
			}
			
			input_line += ch;
			if(count==9){
				temp=atol(input_line.c_str());
				input_line="";
				count=0;
			}			
		}
		
		while(count>0)
		{
			temp=temp*10;
			count--;
		}
		
		K = temp+atoi(input_line.c_str());
		int val=1;
		while(N>0){
			val=2*val;
			N--;		
		}
		
		int rest=K%(val);
		//cout<<K<<" "<<N<<" "<<rest<<endl;
		if(rest==(val-1))
			cout<<"Case #"<<i+1<<":"<<" ON"<<endl;
		else
			cout<<"Case #"<<i+1<<":"<<" OFF"<<endl;

	}
	



	return 0;
}
