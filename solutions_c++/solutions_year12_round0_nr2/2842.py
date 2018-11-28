#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int i = 0; i<T; i++){
		int N, S, p;
		cin>>N>>S>>p;
		int y = 0;
		for(int j = 0; j<N; j++){
			int n;
			cin>>n;
			if(n >= p){
				if((n-p)/2 > p || abs(((n-p)/2)-p) < 2){
					y++;
				}
				else if(abs(((n-p)/2)-p)== 2 && S>0){
					y++;
					S--;
				}
			}
		}
		cout<<"Case #"<<(i+1)<<": "<<y<<endl;
	}
}