#include<iostream>
#include<cstring>
#include<queue>
#include<map>
//#define DEBUG
using namespace std;
struct train{
	int dep, arr;
	bool operator < (const struct train & b) const {
		return (this->dep < b.dep || (this->dep == b.dep && this->arr < b.arr) ) ? true : false;
	}
	bool operator <= (const struct train & b) const {
		return (this->dep < b.dep || (this->dep == b.dep && this->arr <= b.arr) ) ? true : false;
	}
};
struct trainBigCmp{
	bool operator()(const struct train &a, const struct train &b){
		return !(a < b) ;
	}
};
priority_queue<train, vector<train>, trainBigCmp> schA, schB;

void schedule(int test){
	int fromA = 0, fromB = 0, tmp;
	priority_queue<int, vector<int>, greater<int> > sbA, sbB; //standby time
	while(!schA.empty() || !schB.empty()){
		train nextA = schA.top();
		train nextB = schB.top();

		if( !schA.empty() && (schB.empty() || nextA <= nextB ) ){
			sbB.push( nextA.arr );
			if( !sbA.empty() && sbA.top() <= nextA.dep )
				sbA.pop();
			else
				fromA++;
#ifdef DEBUG
			cout << "train A(" << nextA.dep << "::" << nextA.arr << ")\t#" << sbB.size() << " stanby B at :" << nextA.arr << "(standbyA #" << sbA.size() << " fromA:" << fromA << ")" << endl;
#endif
			schA.pop();
		}else if( !schB.empty() && (schA.empty() || nextB < nextA ) ){
			sbA.push( nextB.arr );
			if( !sbB.empty() && sbB.top() <= nextB.dep )
				sbB.pop();
			else
				fromB++;
#ifdef DEBUG
			cout << "train B(" << nextB.dep << "::" << nextB.arr << ")\t#" << sbA.size() << " standby A at :" << nextB.arr << "(standbyB #" << sbB.size() << " fromB:" << fromB << ")" << endl;
#endif
			schB.pop();
		}
	}
	cout << "Case #" << test << ": " << fromA << " " << fromB << endl;
}

int main(){
	int N, NA, NB, T, t1[2], t2[2];
	char dep[100], arr[100];
	train tn;
	cin >> N;
	for(int i = 0 ; i < N ; i++){
		cin >> T >> NA >> NB;
		for(int j = 0 ; j < NA ; j++){
			cin >> dep >> arr;
			sscanf(dep, "%d:%d", &(t1[0]), &(t1[1]));
			sscanf(arr, "%d:%d", &(t2[0]), &(t2[1]));
			tn.dep = t1[0]*60 + t1[1];
			tn.arr = t2[0]*60 + t2[1] + T;
			schA.push( tn );
		}
		for(int j = 0 ; j < NB ; j++){
			cin >> dep >> arr;
			sscanf(dep, "%d:%d", &(t1[0]), &(t1[1]));
			sscanf(arr, "%d:%d", &(t2[0]), &(t2[1]));
			tn.dep = t1[0]*60 + t1[1];
			tn.arr = t2[0]*60 + t2[1] + T;
			schB.push( tn );
		}
		schedule(i+1);
	}
}

