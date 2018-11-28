#include <iostream>
#include <fstream>
using namespace std;

bool has_atleast(int triplet,int p, int &S){
	//cout<<"\nnum: "<<triplet<<" p: "<<p<<" s: "<<S<<"\n";
	int pre=0,rem=0;
	if(triplet>2){
		if(triplet%3==0)
			pre=triplet/3-1;
		else
			pre=triplet/3;
	}
	rem=triplet-(pre*3);
	//cout<<"div: "<<pre<<" remain: "<<rem<<endl<<endl;
	if(rem==0)
		if(pre>=p) 
			return true; 
		else 
			return false;
	if(rem==1)
		if((pre+1)>=p) 
			return true; 
		else 
			return false;
	if(rem==2 || rem==3)
		if((pre+1)>=p) 
			return true; 
		else 
			if((pre+2)>=p && S>0){
				S--;
				return true; 
			}else 
				return false;
}

int main(){
	ifstream input;
	ofstream output;
	input.open("d:/input.in");
	output.open("d:/output.in");
	int T;
	input>>T;
	for(int i=1;i<=T;i++){
		output<<"Case #"<<i<<": ";
		cout<<"Case #"<<i<<": ";
		int N,S,P;
		input>>N>>S>>P;
		int Res=0;
		for(int j=0;j<N;j++){
			int tmp;
			input>>tmp;
			int tmp2=has_atleast(tmp,P,S);
			//cout<<tmp2<<endl;
			Res+=tmp2;
		}
		cout<<"="<<Res<<endl;
		output<<Res<<endl;
	}
	system("pause");
	return 0;
}