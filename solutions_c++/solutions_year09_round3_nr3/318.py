#include<iostream>
#include<vector>
#include<fstream>
#include<functional>
#include<algorithm>

using namespace std;

int main(){
	ifstream ifile("input.txt");
	ofstream ofile("out.txt");

	int n,i=0;
	ifile>>n;
	while(i++<n){
		long p,q;
		ifile>>p>>q;
		vector<long> qList;
		for(long k = 0 ; k < q ;k++){
			long temp;
			ifile>>temp;
			qList.push_back(temp);
		}

		

		
		long min= 999999;
		do{
			long coins = 0;
			vector<int> flag;
			for(int k = 0 ; k < p ;  k++)
				flag.push_back(1);
			
			for(long k = 0 ; k < q ;k++){
				flag[qList[k]-1] = 0;
				for(long j = qList[k] ; j < flag.size() ; j++){
					if(flag[j]==0) break;
					coins += 1;
				} 
				for(long j = qList[k]-2 ; j >= 0; j--){
					if(flag[j] ==0) break;
					coins += 1;
				}
			}
			if(coins < min) min = coins;
		}while( next_permutation( qList.begin() , qList.end()) );

		ofile<<"Case #"<<i<<": "<<min<<"\n";
	}
}