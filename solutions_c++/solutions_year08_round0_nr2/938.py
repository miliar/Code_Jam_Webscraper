#include <iostream>
#include <algorithm>
using namespace std;
struct Train{
int start;
int end;
int visit;
Train(){
visit=0;}
};
bool com1(const Train& t1, const Train& t2){
return t1.start<t2.start;
}
bool com2(const Train& t1, const Train& t2){
return t1.end<t2.end;
}

int main() {
    freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out.txt","w",stdout);
	int cases;
	int ca;
	
	cin>>cases;
	for (ca=1; ca<=cases; ++ca) {
		int T;
		int NA, NB;
		int h, m;
		char tmp;
		Train A[101];
		Train B[101];
		
		cin>>T;
		cin>>NA>>NB;
		int i, j;
		for (i=0; i<NA; ++i) {
			cin>>h>>tmp>>m;
		//	cout<<h<<tmp<<m<<endl;
			A[i].start=h*60+m;
			cin>>h>>tmp>>m;
			A[i].end=h*60+m+T;
		}
		for (i=0; i<NB; ++i) {
			cin>>h>>tmp>>m;
			B[i].start=h*60+m;
			cin>>h>>tmp>>m;
			B[i].end=h*60+m+T;
		}
		int ansA=0, ansB=0;
	sort(A,A+NA,com1);
	sort(B,B+NB,com2);
		for (i=0; i<NA; ++i) {
			for (j=0; j<NB; ++j) {
				if (A[i].start>=B[j].end&&B[j].visit==0)
				{
					B[j].visit=1;
					break;
				}
			}
			if (j==NB)
				++ansA;
		}
sort(A,A+NA,com2);
	sort(B,B+NB,com1);
		for (i=0; i<NB; ++i) {
			for (j=0; j<NA; ++j) {
				if (B[i].start>=A[j].end&&A[j].visit==0){
					A[j].visit=1;
					break;
				}
			}
			if (j==NA)
				++ansB;
		}
		cout<<"Case #"<<ca<<": "<<ansA<<" "<<ansB<<endl;


	}
	return 0;
}