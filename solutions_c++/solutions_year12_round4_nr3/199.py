#include<fstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;
int main(){
	ifstream in("C.in"); ofstream out("C.out");
	int T;
	in>>T;

	for (int t=0;t<T;t++){
		int N;
		in>>N;
		int next[N-1];
		int num[N];
		int heights[N];
		for (int n=0;n<N-1;n++){
			in>>next[n];
			next[n]--;
		}
		out<<"Case #"<<t+1<<": ";
		bool needbreak = false;
		for (int i=0;i<N-1 && !needbreak;i++){
			for (int j=i+1; (j<next[i]) && (!needbreak); j++){
				if (next[j]>next[i]){
					out<<"Impossible\n";
					cout<<t+1<<": "<<i<<"->"<<next[i]<<", "<<j<<"->"<<next[j]<<"\n";
					needbreak = true;
				}
			}
		}
		if (needbreak) continue;
		num[N-1] = 0;
		heights[N-1] = (N*(N-1))/2 +1;
		for (int i=N-1;i>=0;i--){
			for (int j=0; j<i; j++){
				if (next[j] == i){
					num[j] = num[i]+1;
					heights[j] = heights[i] - (i-j)*num[i]-1;
				}
			}
		}
		for (int i=0;i<N;i++){
			out<<heights[i]<<" ";
		}
		for (int i=0;i<N-1;i++){
			int maxi= i+1;
			for (int j=i+2; j<N;j++){
				if ((heights[j]-heights[i]) * (maxi - i) >(heights[maxi]-heights[i])*(j-i)){
					maxi = j;
				}
			}
			if (maxi!=next[i]) {cout<<t+1<<": "<<i<<", "<<maxi<<" "<<next[i]<<"\n"; break;}
		}
		out<<"\n";
	}
}
