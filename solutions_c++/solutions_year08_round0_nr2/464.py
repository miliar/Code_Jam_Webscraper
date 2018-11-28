#include "iostream"
#include "sstream"
#include "fstream"
#include "vector"
#include "algorithm"

using namespace std;

ifstream in("B-large.in");
ofstream out("out.txt");

struct A{
	A(int s, int t): Start(s), Time(t) {}
	A(const A& a): Start(a.Start), Time(a.Time) {}
	bool operator>(const A& a){ return Start > a.Start; }
	bool operator<(const A& a){ return Start < a.Start; }
	int Start;
	int Time;
};

int main(){
	int N = 0;
	in >> N;
	for(int i = 0; i < N; i++){
		vector<A> A, B;
		int T = 0;
		in >> T;
		int NA = 0, NB = 0;
		in >> NA >> NB;
		for(int i = 0; i < NA; i++){
			int start = 0, temp = 0, time = 0;
			char c = 0;
			in >> start >> c >> temp;
			start = 60*start + temp;
			in >> time >> c >> temp;
			time = time*60 + temp - start;
			A.push_back(struct A(start, time));
		}
		for(int i = 0; i < NB; i++){
			int start = 0, temp = 0, time = 0;
			char c = 0;
			in >> start >> c >> temp;
			start = 60*start + temp;
			in >> time >> c >> temp;
			time = time*60 + temp - start;
			B.push_back(struct A(start, time));
		}

		//Processing
		if(0 == NA || 0 == NB){
			out << "Case #" << i+1 << ": " << NA << " " << NB << endl;
			continue;
		}
		sort(A.begin(), A.end());
		sort(B.begin(),	B.end());

		int resA = 0, resB = 0;
		while(A.size() != 0 && B.size() != 0){
			bool isA = A.at(0) < B.at(0);
			int curtime = T + (isA ? A.at(0).Start + A.at(0).Time : B.at(0).Start + B.at(0).Time);
			if(isA){
				resA++;
				A.erase(A.begin());
			}else{
				resB++;
				B.erase(B.begin());
			}
			vector<struct A> *temp = isA ? &B : &A;
			while(curtime <= temp->at(temp->size()-1).Start){
				for(size_t i = 0; i < temp->size(); i++){
					if(curtime <= temp->at(i).Start){
						isA = !isA;
						curtime = T + temp->at(i).Start + temp->at(i).Time;
						temp->erase(temp->begin() + i);
						temp = isA ? &B : &A;
						break;
					}
				}
				if(temp->size() == 0){
					break;
				}
			}
		}
		out << "Case #" << i+1 << ": " << resA + A.size() << " " << resB + B.size() << endl;
	}
}