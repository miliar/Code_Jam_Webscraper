#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
	string line;
	getline(cin, line);
	int N;
	istringstream(line)>>N;
	vector<string> matrix(N);
	vector<int> last1(N);
	for(int i=0; i<N; i++)
		getline(cin, matrix[i]);
	for(int i=0; i<N; i++)
		for(int j=0; j<N; j++)
			if(matrix[i][j]=='1')
				last1[i]=j;
	int res=0;
	for(int i=0; i<N; i++){
		if(last1[i]>i){
			int j;
			for(j=i+1; ; j++){
				if(last1[j]<=i){
					break;
				}
			}
			while(j>i){
				swap(last1[j], last1[j-1]);
				res++;
				j--;
			}
		}
	}
	cout<<res<<endl;
}

int main(){
	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
