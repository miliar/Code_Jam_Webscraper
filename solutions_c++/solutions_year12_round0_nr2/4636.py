#include <iostream>
#include <vector>
using namespace std;

int main(){
    int T,N,S,p;
    cin >> T;
    for(int i=0;i<T;++i){
		cin >> N >> S >> p;
		int count=0;
		vector <int> vysledky(N);
		for(int j=0;j<N;++j){
			cin >> vysledky[j];
		}
		for(int j=0;j<N;++j){
			int t=vysledky[j]/3;
			//cout << t << endl;
			if(vysledky[j]%3==0){
				if(t>=p){
					++count;
				}
				else if(S>0&&t+1>=p&&t!=0){
					++count;
					--S;
				}
					
			}
			else if(vysledky[j]%3==1){
				if(t+1>=p)
					++count;
			}
			else if(vysledky[j]%3==2){
				if(t+1>=p){
					++count;
				}
				else if(S>0&&t+2>=p){
					++count;
					--S;
				}
			}
				
		}
		cout << "Case #" << i+1 << ": " << count << endl;
    }
	return 0;
}


