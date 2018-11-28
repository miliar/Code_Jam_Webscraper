#include<iostream>
#include<fstream>
#include<string>
#include<stack>
#include<cmath>
#include<queue>

using namespace std;

int main(int argc, char *argv[]){
	if(argc != 2)
		return -1;
	ifstream fin(argv[1]);
	string str;
	
	int T;

	fin>>str;
	T = atoi(str.c_str());
	for(int i = 1; i <= T; i++){
		priority_queue<int> order;
		int N;
		int sum = 0;

		fin>>str;
		N = atoi(str.c_str());
		for(int j = 0; j < N; j++){
			fin>>str;
			int tmp = atoi(str.c_str());
			order.push(tmp);
			sum ^= tmp;
		}
		if(sum){
			cout<<"Case #"<<i<<": NO"<<endl;
			continue;
		}
		sum = 0;
		while(order.size() > 1){
			sum += order.top();
			order.pop();
		}
		order.pop();
		
		cout<<"Case #"<<i<<": "<<sum<<endl;
	}
}