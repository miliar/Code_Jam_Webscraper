#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

typedef pair<int,int> wire;

bool intersect(int A1, int B1, int A2, int B2){
	int num = (B2+A2)-(B1+A1);
	int den = (B1-A1)-(B2-A2);
	if (den==0)	return false;
	int x = num/den;
	if (x>=-1 && x<=1)	return true;
	return false;
}

int main(){
	int T;
	cin >> T;
	for (int c=0; c<T; c++){
		long N;
		cin >> N;
		long count=0;
		
		wire *input = new wire [N];
		
		for (int n=0; n<N; n++){
			int A,B;
			cin >>A >> B;
			input[n] = wire(A,B);
		}
				
		for (int n=0; n<N; n++)
			for (int m=n+1; m<N; m++){
				//if (intersect(input[n].first,input[n].second,input[m].first,input[m].second))	count++;
				if (input[n].first<input[m].first && input[n].second>input[m].second)	count++;
				else if (input[n].first>input[m].first && input[n].second<input[m].second) count++;
			}
		cout<<"Case #"<<c+1<<": "<<count<<endl;
	}
	return 0;
}
