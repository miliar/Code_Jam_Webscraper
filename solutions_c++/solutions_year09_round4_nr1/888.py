#include <iostream>
#include <fstream>
#include <queue>
#include <utility>

using namespace std;

int main() {
	ofstream fout ("google2a.out");
	ifstream fin ("google2a.in");
	int numCases;
	fin>>numCases;
	for(int caseNum=0; caseNum<numCases; caseNum++){
		int length;
		fin>>length;
		fin.get();
		priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > que;
		priority_queue<int, vector<int>, greater<int> > que2;
		for(int i=0; i<length; i++){
			int last=0;
			for(int j=0; j<length; j++){
				if(fin.get()=='1')
					last=j;
			}
			fin.get();
			que.push(pair<int, int>(last, i));
		}
		int want[40], index[40];
		for(int n=0; n<length; n++){
			while(!que.empty() && que.top().first<=n){
				que2.push(que.top().second);
				que.pop();
			}
			want[que2.top()]=n;
			index[n]=que2.top();
			que2.pop();
		}
		int swaps=0;
		for(int n=length-1; n>=0; n--){
			while(index[n]!=n){
				swaps++;
				int pos=index[n];
				//cout<<pos<<pos+1<<endl;
				int c=want[pos+1];
				want[pos+1]=want[pos];
				want[pos]=c;
				index[n]++;
				index[want[pos]]--;
			}
		}
		fout<<"Case #"<<caseNum+1<<": "<<swaps<<endl;
	}
	return 0;
}
