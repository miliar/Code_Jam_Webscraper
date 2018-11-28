#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
typedef long long ll;
using namespace std;
double T,d;
vector< double > x , xd;
int N;

inline bool check(){


   
xd[0]=x[0]-d;
   for(int i=1;i<N;i++){
     //always try to move everyone leftward by d 
     //if not possible only then move rightward
     if((x[i]-d)-(xd[i-1]+T)>(1e-7))
           xd[i]=x[i]-d;
     else{
        xd[i]=xd[i-1]+T;
        if(xd[i]-x[i]>(1e-7))
            if((xd[i]-x[i])-d>(1e-7))return false;
     }
   }
   return true;
}

int main(){
    int k;scanf("%d",&k);
	int cs = 1;
    while(k--){
	cout<<"Case #"<<cs<<": ";
	cs++;
	x.clear();xd.clear();
        scanf("%d%lf",&N,&T);
        for(int i=0;i<N;i++){
        	int tmp , n;
		cin >> tmp >> n; 
	  	for( int k = 0; k<n;k++) x.push_back((double)(tmp));
	}
	N = x.size();xd = vector<double>(N);
        double dmin=0.0,dmax=N*T;
        //select a d using binary search
        //check if its possible to place for this d or not
        while(dmax-dmin>(1e-7)){
            d=(dmin+dmax)/2;
            if(check())
                 {dmax=d;}
            else {dmin=d;}
        }
       cout<<dmin<<endl;
    }
    return 0;
}

