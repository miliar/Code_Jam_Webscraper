#include<iostream>
#include<fstream>
#include<string>
#include <stdlib.h> 
 using namespace std;
 
 class Or{
	private:
int bosition;
 public:
void inti(){bosition=1;}
void moveforward(){bosition+=1;}
void movebackward(){bosition-=1;}
int getbosition(){return bosition;}
bool Push(){return true;}
 };
 class Bl{
	private:
 int bosition;
 public:
void inti(){bosition=1;}
void moveforward(){bosition+=1;}
void movebackward(){bosition-=1;}
int getbosition(){return bosition;}
bool Push(){return true;}
 };


int main()
{
ifstream in("x.in");
ofstream out("y.out");
Or or;
Bl bl;
while(!in.eof()){
int n;
in>>n;
for(int i=0;i<n;i++){//loop testcases>>>>>>>>>>>>>>>>>>>>>>
int time=0;
int arraynum;
or.inti();bl.inti();
in>>arraynum;
//cout<<arraynum<<endl;
int* A=new int[arraynum];
char* C=new char[arraynum];
for(int j=0;j<arraynum;j++){
in>>C[j];//cout<<C[j];
in>>A[j];//cout<<A[j];
}//endfor
//cout<<endl;
for(j=0;j<arraynum;j++){
	if(C[j]=='O'){//ooooooooooooooooooooooooooooooooooooooooooooooo
	int goal=A[j];bool click=false;
//	cout<<goal<<endl;
while(click==false){	
	if(goal>or.getbosition()){or.moveforward();
	time++;
		// for B not to wait
	if(arraynum-1>j){
		for(int k=j+1;k<=arraynum-1;k++){	bool u=false;
		if(C[k]=='B'){
		if(A[k]>bl.getbosition())bl.moveforward();
		if(A[k]<bl.getbosition())bl.movebackward();
			u=true;
		}//if c
		if(u)break;
		}// for k
	}//if ar
	}//if goal
	else if(goal<or.getbosition()){
	or.movebackward();
	time++;
	// for B not to wait
	if(arraynum-1>j){
		//if(C[j+1]=='B'){
		//if(A[j+1]>bl.getbosition())bl.moveforward();
		//if(A[j+1]<bl.getbosition())bl.movebackward();
		//}//if c
		for(int k=j+1;k<=arraynum-1;k++){	bool u=false;
		if(C[k]=='B'){
		if(A[k]>bl.getbosition())bl.moveforward();
		if(A[k]<bl.getbosition())bl.movebackward();
			u=true;
		}//if c
		if(u)break;
		}// for k
	}//if ar
	}//else if <
	else if(goal==or.getbosition()){
	click=or.Push();
	time++;
	// for B not to wait
	if(arraynum-1>j){
	//	if(C[j+1]=='B'){
		//if(A[j+1]>bl.getbosition())bl.moveforward();
	//	if(A[j+1]<bl.getbosition())bl.movebackward();
	//	}//if c
for(int k=j+1;k<=arraynum-1;k++){	bool u=false;
		if(C[k]=='B'){
		if(A[k]>bl.getbosition())bl.moveforward();
		if(A[k]<bl.getbosition())bl.movebackward();
			u=true;
		}//if c
		if(u)break;
		}// for k

	}//if ar

	}// else if goal
}//while 
	}//end if cj o
	else if(C[j]=='B'){
	int goal=A[j];bool click=false;
while(click==false){
	if(goal>bl.getbosition()){bl.moveforward();
	time++;
		// for B not to wait
	if(arraynum-1>j){
	//	if(C[j+1]=='O'){
	//	if(A[j+1]>or.getbosition())or.moveforward();
	//	if(A[j+1]<or.getbosition())or.movebackward();
	//	}//if c
for(int k=j+1;k<=arraynum-1;k++){	bool u=false;
		if(C[k]=='O'){
		if(A[k]>or.getbosition())or.moveforward();
		if(A[k]<or.getbosition())or.movebackward();
			u=true;
		}//if c
		if(u)break;
		}// for k

	}//if ar
	}//if goal
	else if(goal<bl.getbosition()){
	bl.movebackward();
	time++;
	// for B not to wait
	if(arraynum-1>j){
		//if(C[j+1]=='O'){
	//	if(A[j+1]>or.getbosition())or.moveforward();
	//	if(A[j+1]<or.getbosition())or.movebackward();
	//	}//if c
for(int k=j+1;k<=arraynum-1;k++){	bool u=false;
		if(C[k]=='O'){
		if(A[k]>or.getbosition())or.moveforward();
		if(A[k]<or.getbosition())or.movebackward();
			u=true;
		}//if c
		if(u)break;
		}// for k

	}//if ar
	}//else if <
		else if(goal==bl.getbosition()){
	click=bl.Push();
	time++;
	// for B not to wait
	if(arraynum-1>j){
	//	if(C[j+1]=='O'){
	//	if(A[j+1]>or.getbosition())or.moveforward();
	//	if(A[j+1]<or.getbosition())or.movebackward();
	//	}//if c
		for(int k=j+1;k<=arraynum-1;k++){	bool u=false;
		if(C[k]=='O'){
		if(A[k]>or.getbosition())or.moveforward();
		if(A[k]<or.getbosition())or.movebackward();
			u=true;
		}//if c
		if(u)break;
		}// for k
	}//if ar

	}// else if goal


}//end while goal
	
	}//end if cj b

}//for j loop array
out<<"Case #"<<(i+1)<<": "<<time<<endl;

}//end for i;
in.close();
out.close();
}// end while
	


	return 0;

}



/*	ofstream out("y.out");
	ifstream in("x.in");
	while(!in.eof()){
/*	getline(in,s);
	out<<s<<endl;
int a=atoi(s.c_str());or*
		int a;
		in>>a;// cases num
for(int i=0;i<a;i++){
//getline(in,s);int b=atoi(s.c_str()); or
	int b; in>>b;//credit
 int x;in>>x;// items num
 int* A=new int[x];
for(int j=0;j<x;j++){
in>>A[j];
}//end for
for(j=0;j<x;j++){
	for(int k=j+1;k<x;k++){
		if(A[j]+A[k]==b){
		out<<"Case #"<<(i+1)<<":"<<" "<<(j+1)<<" "<<(k+1)<<endl;
		}// if end 
	}//k end
}// end j
int c=atoi(s.c_str());
delete [] A;
} //forend 
	}
	in.close();
out.close();
*/
