#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream infile;
	ofstream outfile;
	char inname[50];
	cout<<"input input filename: ";
	cin>>inname;
	infile.open(inname);
	outfile.open("p2Ans.txt");
	int T;
	infile>>T;
	int I=1;
	string line;
	getline(infile,line);
	while(I<=T){
		int ans=0;
		int N,S,P;
		infile>>N;
		infile>>S;
		infile>>P;
		for (int i=0;i<N;++i){
			int total;
			infile>>total;
			int rm=total%3;
			switch(rm){
			  case 0:{
				if((total/3) >= P) ++ans;
				  else if((total/3 +1)>=P&& (total/3 -1)>=0 && S>0) {
					++ans;
					--S;
				}
				break;
			  }
			  case 1:{
				if((total/3 +1)>=P) ++ans;
				break;
			  }
			  case 2:{
				if((total/3 +1)>=P) ++ans;
				  else if((total/3 +2)>=P && S>0) {
					++ans;
					--S;
				}
				break;
			  }
			}	
			
		}
		//output	
		outfile<<"Case #"<<I<<": "<<ans<<"\n";
		++I;
	}
return 0;
}
