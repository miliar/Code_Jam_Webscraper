/*
*  Javier Segovia
*  0.016
*/
#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair

int A[1000005];
int main(){
	cout.setf(ios::fixed);
	cout.precision(10);
	int T; cin>>T;
	int X,S,R,t,N,B,E,w,dist;
	double act;
	for (int kas=1; kas<=T; kas++) {
		cin>>X>>S>>R>>t>>N;
		for (int i=0; i<=X ; i++) {
			A[i] = 0;
		}
		double res=0.0;
		for (int i=0; i<N ; i++) {
			cin>>B>>E>>w;
			for (int j=B ; j<E ; j++) {
				A[j]+=w;
			}
		}
		sort(A,A+X); //for(int i=0;i<=X;i++) cout<<"I: "<<i<<" A: "<<A[i]<<endl;
		double diff;
		int p=0;
		act=0.0;
		while (res<t && p<X) {
			act = 1.0/double(A[p]+R);
			if(res+act>t){
				diff = 1.0 - (t-res)*double(A[p]+R);
				//res-= diff/double(A[p]+R);
				res = t;
				res+= diff/double(A[p]+S);
			}
			else res+=act;
			p++; 
			//cout<<"P: "<<p<<" R: "<<res<<" "<<limt<<endl;
		}//cout<<"OUT"<<endl;
		for (int i=p; i<X ; i++) {
			res+= 1.0/double(A[i]+S);
			//cout<<"P: "<<i<<" R: "<<res<<endl;

		}
		cout<<"Case #"<<kas<<": "<<res<<endl;
	}
}