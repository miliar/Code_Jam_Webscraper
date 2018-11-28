#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
ifstream input;
ofstream output;
input.open("d:/input.in");
output.open("d:/output.in");
int N,T;
vector<int> B,O,S;
input>>N;
for(int i=1;i<=N;i++){
	int ans=0;
	O.clear();
	B.clear();
	int Os=1,Bs=1;
	output<<"Case #"<<i<<": ";
	cout<<"Case #"<<i<<": ";
	input>>T;
	char tmp;
	int tmp2;
	for(int j=0;j<T;j++){
		input>>tmp;
		input>>tmp2;
		if(tmp=='O') {O.push_back(tmp2); S.push_back(1);} else{B.push_back(tmp2); S.push_back(0);}
	}
	while(S.size()>0){
		bool chk=false,chk2=false;
		if(O.size()>0)if(Os!=O.at(0)){if(Os<O.at(0))Os++; else Os--; chk=true;}
		if(B.size()>0)if(Bs!=B.at(0)){if(Bs<B.at(0))Bs++; else Bs--; chk2=true;}
		ans++;
		if (S.at(0)==1){
		if (chk==false){
			O.erase(O.begin());
			S.erase(S.begin());
		}
		}else{
		if (chk2==false){
			B.erase(B.begin());
			S.erase(S.begin());
		}
		}

	}		output<<ans<<endl;cout<<ans<<endl;
}
system("pause");
return 0;
}