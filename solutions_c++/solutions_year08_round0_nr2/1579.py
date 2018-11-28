#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

ifstream ifs("in.txt");
ofstream ofs("out.txt");
string tmp;


int minutes(string str)
{
	return ( (str[0]-'0')*10 + (str[1]-'0') )*60 + (str[3]-'0')*10 + (str[4]-'0');
};

void rec(vector<pair<int,int> >& A , vector<pair<int,int> >& B, int time , int T)
{
	
	for(size_t i = 0 ; i < A.size() ; i++){
		if (A[i].first>=time){

			time = A[i].second + T;
			A.erase(A.begin() + i);
			rec(B,A,time,T);

			break;
		}
	}

};

int main()
{
	int N; ifs>>N;
	
	for(int n = 0 ; n < N ; n++){
		int T , NA, NB;
		ifs>>T>>NA>>NB;

		vector< pair<int,int> > A(NA),B(NB);

		for(int i = 0 ; i < NA ; i++){
			ifs>>tmp; A[i].first = minutes(tmp);
			ifs>>tmp; A[i].second = minutes(tmp);
		}
		for(int i = 0 ; i < NB ; i++){
			ifs>>tmp; B[i].first = minutes(tmp);
			ifs>>tmp; B[i].second = minutes(tmp);
		}

		sort( A.begin() , A.end() );
		sort( B.begin() , B.end() );

		int needA = 0 , needB = 0;;

		while(A.size() > 0 && B.size() > 0){
			if ( A[0].first < B[0].first ){
				needA++;
				rec(A,B,A[0].first , T);
			}
			else{
				rec(B,A,B[0].first , T);
				needB++;

			}

		}
		needA+=A.size();
		needB+=B.size();
		ofs<<"Case #"<<n+1<<": "<<needA<<" "<<needB<<endl;





	}


	return 0;
};
