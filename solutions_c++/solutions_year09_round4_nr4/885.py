#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<ctime>
#include<algorithm>
#include <map>

using namespace std;
#define SZ(v) ((int)v.size())
#define FOR(i,b,e) for(int i = b;i < e; ++i)
#define REP(i,v) FOR(i,0,SZ(v))
typedef vector<int> VI; 
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<char> VC;

const double pi=acos(-1.0);
const double eps=1e-11;
#define zero(x) memset(&x, 0, sizeof x);



int main(){
	freopen("E:\\D-small-attempt0.in","r",stdin);
	freopen("E:\\out.txt","w",stdout);
	

	int T;
	cin>>T;

	FOR(k,0,T){
		int N;
		cin>>N;
		double res;
		int X[10],Y[10],R[10];
		
		for(int i=0;i<N;++i){
			cin>>X[i]>>Y[i]>>R[i];
		}
		if (N==1){
			res=R[0];
		}
		if (N==2){
			res=R[0];
			if (res<R[1]) res=R[1];
		
		}
		if (N==3){
			res=10000;
			double temp;
			for(int i=0;i<N;++i){
				temp=R[i];
				double temp2;
				int s1=-1,s2=-1;
				for(int j=0;j<N;++j){
					if (j!=i){
						if (s1==-1) s1=j; else s2=j;
					}
				}
				temp2=R[s1]+R[s2]+sqrt(double((X[s1]-X[s2])*(X[s1]-X[s2])+(Y[s1]-Y[s2])*(Y[s1]-Y[s2])));
				temp2=temp2/2;
				if (temp<temp2) temp=temp2;
				if (res>temp) res=temp;
			}
			
		
		}


		cout<<"Case #"<<k+1<<": ";
		printf("%.7lf",res);
		cout<<endl;
	}
	return 0;

}