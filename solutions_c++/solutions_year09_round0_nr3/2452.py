#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

int main(){

	
	vector<int> Ppoint;
	vector<int> Gpoint;
	

	string wstr("welcome to code jam");
	int N;
	string tstr;

	ifstream in("C-small-attempt0.in");	
	ofstream out("C-output.out");	

	in>>N;
	
	getline(in, tstr);

	for(int i=0; i<N; i++){
			   
		getline(in, tstr);

		for(int j=0; j<tstr.length()+1; j++){
			Ppoint.push_back(1);
			Gpoint.push_back(0);
		}

		for(int k=0; k<wstr.length(); k++){
		  for(int l=0; l<tstr.length(); l++){
			  if(wstr.at(k)==tstr.at(l)){
				Gpoint[l+1]=Ppoint[l]+Gpoint[l];
			  }
			  else{
			    Gpoint[l+1]=Gpoint[l];
			  }
		  }

		  for(int m=0; m<tstr.length()+1; m++){
			Ppoint[m]=Gpoint[m];
			Gpoint[m]=0;
		  }

		}
			
		int num=i;
		num++;
		out<<"Case #"<<num<<": "<<setw(4)<<setfill('0')<<Ppoint[tstr.length()]<<endl;
		
		Ppoint.clear();
		Gpoint.clear();
	}

	

	return 0;
}