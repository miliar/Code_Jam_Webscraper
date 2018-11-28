#include <iostream>
using namespace std;
int main() {
	int T=0, cases=0, N=0, S=0, p=0, result=0;
	int score;
	int i, j;
	cin>>T;
	for (cases=1; cases<=T; cases++) {
		cin>>N>>S>>p;
		result=0;
		for (i=0; i<N; i++) {
			cin>>score;
			if (score==0 && p>0)
				continue;
			if (score==1 && p>1)
				continue;
			if ((score+2)/3>=p)
				result++;
			else
				if (S>0 && (score+4)/3>=p) {
					S--;
					result++;
				}
		}
		cout<<"Case #"<<cases<<": "<<result<<endl;
	}
	return 0;
}
