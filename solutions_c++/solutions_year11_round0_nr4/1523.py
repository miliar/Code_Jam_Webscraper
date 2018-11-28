#include<iostream>
using namespace std;
int main(){
	int i, k, n, CASE, NUM, ANS;
	freopen("D-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin>>CASE;
	for(NUM = 1; NUM <= CASE; NUM++){
		cin>>n;
		ANS = 0;
		for(i = 1; i <= n; i++){
			cin>>k;
			if(i != k)
				ANS++;
		}
		cout<<"Case #"<<NUM<<": "<<ANS<<endl;
	}
}
