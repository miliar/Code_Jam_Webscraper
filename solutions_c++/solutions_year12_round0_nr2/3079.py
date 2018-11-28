#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

int ROUND(double a){
	return (int)(a+0.5);
}	


int main(){
	int T;
	ifstream ifs; 
	ifs.open("B-large.in");
	ofstream ofs;
	ofs.open("solution.out");;
	int cas = 1;
	ifs>>T;
	while(cas <= T){
		vector<int> myvec;
		int N;
		ifs>>N;
		int surprise;
		ifs>>surprise;
		int bestResult;
		ifs>>bestResult;
		ofs<<"Case #"<<cas++<<": ";
		for(int i=0; i<N; i++){
			int temp;
			ifs>>temp;
			myvec.push_back(temp);
		}
		sort (myvec.begin(), myvec.end());
		int ans=0;
		vector<int>::iterator it;
		for(it= myvec.begin(); it!=myvec.end(); ++it){
			int cmp = ROUND((*it)/3.0);
			if((cmp+1)>bestResult){
				ans++;
				//ofs<<*it<<" ";
			}	
			else if((cmp+1)==bestResult){
				if((*it==0 && bestResult !=0) || (*it==1 && bestResult !=1)){
					;
				}
				else if((cmp*3) < *it ){
					ans++;
					//ofs<<*it<<" ";
				}	
				else if(cmp*3 >= *it && surprise){
					ans++;
					//ofs<<*it<<" ";
					--surprise;
				}
			}
		}
		ofs<<ans<<endl;
	}
	return 0;
}
	
