#include<iostream>
#include<vector>
using namespace std;

long long computeRevenue(int Rounds, int capacity, vector <int> groups){
	long c;
	long long Revenue = 0;
	vector <int> memo(groups.size(),-1), cachelength(groups.size(),0);
	int front =0, selected, cachefront; 
	for(int i=0;i<Rounds;i++){
		c=0;
		selected = 0;
		cachefront = front;
		if(memo[cachefront] == -1){
			while (c <= capacity && selected < groups.size()){
				if(c + groups[front] <= capacity){
					c += groups[front++];
					if(front == groups.size())
						front = 0;
					selected++;
				}
				else
					break;
			}
			Revenue +=  c;
			memo[cachefront] = c;
			cachelength[cachefront] = selected;
		}
		else{
			Revenue += memo[cachefront];
			front = (front + cachelength[cachefront]) % groups.size();
		}
	}
	return Revenue;
}

int main(){
	int T, R, k, N;
	cin >> T;
	for(int test=0;test<T;test++){
		vector <int> groups;
		int g;
		cin >> R >> k >> N;
		for(int i=0;i<N;i++){
			cin >> g;
			groups.push_back(g);
		}
		cout << "Case #" << test+1 << ": "<< computeRevenue(R,k,groups) << endl;
	}
}
