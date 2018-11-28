#include<iostream>
using namespace std;
int main() {
	int T;
	int N, S, p, points, output;
	cin>>T;
	for(int i=0;i<T;i++) {
		cin>>N>>S>>p;
		output=0;
		for(int j=0;j<N;j++) {
			cin>>points;
			switch(points%3) {
			case 0:	if(points/3>=p)
					output++;
				else if(points/3>=p-1&&S>0&&points/3>0) {
					output++;
					S--;
				}break;
			case 1:if(points/3>=p-1)
					output++;
				break;
			case 2:if(points/3>=p-1)
					output++;
				else if(points/3>=p-2&&S>0) {
					output++;
					S--;
				}break;
			};
		}
		cout<<"Case #"<<i+1<<": "<<output<<"\n";
	}
	return 0;
}		
