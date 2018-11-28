#include <iostream>
#include <vector>
#include <list>

using namespace std;

list < int > in, tempStore;
int main(){
	int T;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("Download C-small.out", "w", stdout);
	cin>>T;
	for(int ii = 1; ii <= T; ++ii){
		int R, K, N;
		int i,j,k;
		int temp, poppedVal;
		int result = 0;
		cin>>R>>K>>N;
		in.clear();
		for(i = 0; i< N; ++i){
			cin>>temp;
			in.push_back(temp);
		}
		temp = 0;
		for(i = 0; i< R; ++i){
			temp = 0;
			while(1){
				if(in.size() >=1 ){
					poppedVal = in.front();
					
					if((temp + poppedVal)<= K){
						temp += poppedVal; 
						in.pop_front();
						tempStore.push_back(poppedVal);
					}
					else{
						result += temp;
						while(tempStore.size() > 0){
							poppedVal = tempStore.front();
							in.push_back(poppedVal);
							tempStore.pop_front();
						}
						//cout<<"temp inside :"<<temp<<endl;
						//tempStore.clear();
						//in.clear();
						break;
					}
				}
				else{
						result += temp;
						while(tempStore.size() > 0){
							poppedVal = tempStore.front();
							in.push_back(poppedVal);
							tempStore.pop_front();
						}
						//cout<<"temp outside:"<<temp<<endl;
						//tempStore.clear();
						//in.clear();
						break;
					}
			}
			
		}
		printf("Case #%d: %d\n", ii, result);
		//cout<<" :"<<result<<endl;

	}
}