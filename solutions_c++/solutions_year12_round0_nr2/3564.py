#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<fstream>

using namespace std;




int main(){

	ifstream in;
	ofstream out;
	in.open("B-large.txt");
	out.open("B-large_out.txt");

	int T;
	in>>T;
	for(int i=1;i<=T;++i){
		int N,S,p;
		in>>N>>S>>p;
		int arr[150];
		for(int j=0;j<N;++j){
			in>>arr[j];
		}
		int res=0;
		for(int j=0;j<N;++j){
			int score=arr[j]/3;
			int mod=arr[j]%3;

			if(arr[j]>28){
				res++;
				continue;
			}
			if(arr[j]==0 ){
				if(score>=p){
					res++;
				}
				continue;
			}
			if(arr[j]==1){
				if(score+1>=p){
					res++;
				}
				continue;
			}
			if(mod==0){
				if(score>=p){
					res++;
					continue;
				}
				if(S>0 && score+1>=p){
					S--;
					res++;
					continue;
				}
			}
			else if(mod==1){
				if(score+1>=p){
					res++;
					continue;
				}
			}
			else if(mod==2){
				if(score+1>=p){
					res++;
					continue;
				}
				if(S>0 && score+2>=p){
					S--;
					res++;
					continue;
				}
			}
		}
		out<<"Case #"<<i<<": "<<res<<endl;
	}
	in.close();
	out.close();
	return 0;
}