#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>
#include<set>
#define md 100003

using namespace std;
vector<vector<int> > mapp;
int main(){
	int C, R;
	cin>>C;
	for(int i=0; i<C; i++){
		//cin>>wrds[i]; 
		cin>>R;
		vector<int> x1(R),y1(R),x2(R), y2(R);
		mapp.clear(); mapp.resize(200, vector<int>(200, 0));
		for(int j=0; j<R; j++){
			cin>>x1[j]>>y1[j]>>x2[j]>>y2[j];
			for(int k=x1[j];k<=x2[j]; k++ ){
				for(int p = y1[j]; p<=y2[j]; p++){
					mapp[k][p]=1;
				}
			}

		}
		bool notdead=true;
		int res=0;
		while(notdead){
			notdead=false;
			for(int j=100; j>=1; j-- ){
				for(int k=100; k>=1; k--){
					if(mapp[j][k]){
						notdead=true;
						if(!mapp[j-1][k] && !mapp[j][k-1])
							mapp[j][k]=0;
					}                    else{
						if(mapp[j-1][k] && mapp[j][k-1])
							mapp[j][k]=1;
						
						
					}
				}
			}
			if(notdead)res++;
		}
		cout<<"Case #"<<i+1<<": " <<res<<"\n";
	}
	
}
