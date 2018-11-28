#include"stdlib.h"
#include"stdio.h"
#include <string>
#include<cmath>
#include<iostream>
#include<fstream>
using namespace std;

int T,N;
int Q[102][2]={0};


int Walk(int s_O,int s_B,int level){
	int other_dst;
	int step_A,step_B;
	if(level==N)return 0;
	if(Q[level][1]==0){
		for(other_dst=level+1;other_dst<N&&Q[other_dst][1]==0;other_dst++);
		if(other_dst<N){
			step_A=abs(Q[level][0]-s_O)+1;
			step_B=abs(Q[other_dst][0]-s_B);
			if(step_B<=step_A)
				return Walk(Q[level][0],Q[other_dst][0],level+1)+step_A;
			else{
				if(Q[other_dst][0]>s_B)
					return Walk(Q[level][0],s_B+step_A,level+1)+step_A;
				else{
					return Walk(Q[level][0],s_B-step_A,level+1)+step_A;
				}
			}
		}
		else{
			step_A=abs(Q[level][0]-s_O)+1;
			return Walk(Q[level][0],1,level+1)+step_A;
		}
	}
	else{
		for(other_dst=level+1;other_dst<N&&Q[other_dst][1]==1;other_dst++);
		if(other_dst<N){
			step_A=abs(Q[level][0]-s_B)+1;
			step_B=abs(Q[other_dst][0]-s_O);
			if(step_B<=step_A)
				return Walk(Q[other_dst][0],Q[level][0],level+1)+step_A;
			else{
				if(Q[other_dst][0]>s_O)
					return Walk(s_O+step_A,Q[level][0],level+1)+step_A;
				else{
					return Walk(s_O-step_A,Q[level][0],level+1)+step_A;
				}
			}
		}
		else{
			step_A=abs(Q[level][0]-s_B)+1;
			return Walk(1,Q[level][0],level+1)+step_A;
		}


	}

}

int main()
{
ifstream in;
ofstream out;
//in.open("A-small-attempt0.in");
in.open("A-large.in");
out.open("OUTPUT.txt");
	in>>T;
	char c;
	int k;
	for(int i=1;i<=T;i++){
		in>>N;
		for(int j=0;j<N;j++){
			in>>c>>k;
			Q[j][0]=k;
			if(c=='O')Q[j][1]=0;
			else Q[j][1]=1;
		}
		out<<"Case #"<<i<<": "<<Walk(1,1,0)<<endl;
	}






in.close();
out.clear();
out.close();
return 0;
}