//PATRICK NAKAGAWA
//patricknakagawa@gmail.com



#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int time_to_int(string s){
	return ((int)s[0]-48)*600+((int)s[1]-48)*60+((int)s[3]-48)*10+((int)s[4]-48);
}

class trip{
	public:
	int depart;
	int arrive;
	bool needstrain;
	bool providestrain;
	trip();
	trip(string d, string a){
		depart=time_to_int(d);
		arrive=time_to_int(a);
		needstrain=true;
		providestrain=false;
	}
	trip(int d, int a){
		depart=d;
		arrive=a;
		needstrain=true;
		providestrain=false;
	}
};

//selection sort
void sort_by_arrivals(vector<trip> &x){
	//latest first
	if(x.empty()||x.size()==1){return;}
	int temp;
	int k;
	for (int top=0; top<=x.size()-2; top++) {
		int maxLoc = top;
		for (k=top+1; k<=x.size()-1; k++) {
			if (x[k].arrive > x[maxLoc].arrive) {
				maxLoc = k;
			}
		}
		//trip temp(x[top].depart,x[top].arrive);
		trip temp = x[top];
		x[top] = x[maxLoc];
		x[maxLoc] = temp;
	}
}

void sort_by_departures(vector<trip> &x){
	//latest first
	if(x.empty()||x.size()==1){return;}
	int temp;
	int k;
	for (int top=0; top<=x.size()-1; top++) {
		int maxLoc = top;
		for (k=top+1; k<=x.size()-1; k++) {
			if (x[k].depart > x[maxLoc].depart) {
				maxLoc = k;
			}
		}
		trip temp = x[top];
		x[top] = x[maxLoc];
		x[maxLoc] = temp;
	}
}		




int main (int argc, char * const argv[]) {

	ifstream in("in.txt");
	ofstream out("out.txt");

	int N,T,NA,NB;
	string s1,s2;
	vector<trip> A,B;
	in>>N;
	for(int i=0;i<N;i++){

		
		in>>T>>NA>>NB;
		for(int j=0;j<NA;j++){
			in>>s1>>s2;
			A.push_back(trip(s1,s2));
		}
		for(int j=0;j<NB;j++){
			in>>s1>>s2;
			B.push_back(trip(s1,s2));
		}

		//find trains arriving from B at A to depart back to B
		sort_by_departures(A);
		sort_by_arrivals(B);
		for(int j=0;j<A.size();j++){
			for(int k=0;k<B.size();k++){
				if(B[k].arrive+T<=A[j].depart && !B[k].providestrain && A[j].needstrain){
					B[k].providestrain=true;
					A[j].needstrain=false;
					
				}
			}
		}

		//find trains arriving from A at B to depart back to A
		sort_by_departures(B);
		sort_by_arrivals(A);
		for(int j=0;j<B.size();j++){
			for(int k=0;k<A.size();k++){
				if(A[k].arrive+T<=B[j].depart && !A[k].providestrain && B[j].needstrain){
					A[k].providestrain=true;
					B[j].needstrain=false;
					
				}
			}
		}
			
		//count trains needed
		int Atrainsneeded=0;
		int Btrainsneeded=0;
		for(int j=0;j<A.size();j++){
			if(A[j].needstrain){
				Atrainsneeded++;
			}
		}

		for(int j=0;j<B.size();j++){
			if(B[j].needstrain){
				Btrainsneeded++;
			}
		}
		
		out<<"Case #"<<i+1<<": "<<Atrainsneeded<<" "<<Btrainsneeded<<endl;

		A.clear();
		B.clear();
	}

			
			
    return 0;
}


////////test code

//cout<<"B to A "<<B[k].depart<<" "<<B[k].arrive<<" -------> A to B"<<A[j].depart<<" "<<A[j].arrive<<endl;

///////////////////

		//cout<<"-------results--------"<<endl;
		//cout<<"----------A-----------"<<endl;
		//cout<<"depart arrive   needs  provides"<<endl;
		//for(int j=0;j<A.size();j++){
		//	cout<<A[j].depart<<"   "<<A[j].arrive<<"   ";
		//	if(A[j].needstrain){cout<<"TRUE";}else{cout<<"FALSE";}
		//  cout<<"    ";
		//	if(A[j].providestrain){cout<<"TRUE";}else{cout<<"FALSE";}
		//	cout<<endl;
		//}
		//cout<<"----------B-----------"<<endl;
		//for(int j=0;j<B.size();j++){
		//	cout<<B[j].depart<<"   "<<B[j].arrive<<"   ";
		//	if(B[j].needstrain){cout<<"TRUE";}else{cout<<"FALSE";}
		//  cout<<"    ";
		//	if(B[j].providestrain){cout<<"TRUE";}else{cout<<"FALSE";}
		//	cout<<endl;
		//}