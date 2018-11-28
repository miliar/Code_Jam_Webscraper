#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;
int T,N,K;
vector <pair<int,int> > equipos; //first -> power   ; second -> status
void load(int n){
	equipos.push_back(make_pair(1,0)); //el primero siempre tiene power
	for (int i=1; i<n; i++)
		equipos.push_back(make_pair(0,0));
}
void debug() {	
	for (int i=0; i<equipos.size(); i++){
		cout << "<"<< equipos[i].first << "," << equipos[i].second<< ">-- " ;
	}
}

void click(){
		if (equipos[0].second==0) 
			equipos[0].second=1;//power es 1 si  o si! 
		else 
			equipos[0].second=0; 
			
		for (int j=1; j<equipos.size(); j++){
			if ( equipos[j].first==1 ) {
				if ( equipos[j].second==0 )
					equipos[j].second=1;
				else 
					equipos[j].second=0;
			}
		}
		
		//	for (int i=0; i<equipos.size(); i++)
	//	cout << equipos[i].first << "," << equipos[i].second << endl;
}
void setPower(){
		for (int j=1; j<equipos.size(); j++){
			if ( equipos[j-1].first==1 && equipos[j-1].second==1 )
				equipos[j].first=1;
			else 
				equipos[j].first=0;
		}
}
string solve(){
	string res = "OFF";
	if ( equipos[equipos.size()-1].first==1 && equipos[equipos.size()-1].second==1 ) 
		res="ON";
	return res;
}
int main (int argc, char** argv) {
	ifstream input(argv[1]);
	input >> T;
	int i=0;
	while (i<T){
		input >> N;
		input >> K;
		load(N);
		//debug();cout <<endl;
		for (int n=0; n<K; n++){
			click();
			setPower();
			//debug();cout <<endl;
		}
		cout << "Case #"<< i+1 << ": " << solve() << endl;
		equipos.clear();
		i++;
	}


	return 0;
}
