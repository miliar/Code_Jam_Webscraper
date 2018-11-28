#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
void main(){
	int T,A,B;
	float p[100000];
	ofstream cout("test.txt");
	cin >> T;
	for(int i = 0; i < T; i++){
		float Pt = 1.0;
		float expect = 0.0;
		cin >> A >> B;
		for(int j = 0; j < A; j++){
			cin >> p[j];Pt*=p[j];
		}
		expect = float(2*B-A+2)-float(B+1)*Pt;	
		if(B+2<expect)expect = B+2;
		float t_exp = 0.0;
		int n = A%2?(A+1)/2-1:A/2;
		for(int j = 1; j <= n; j++){
			float Ps = 1.0;
			for(int k = 0; k < A-j;k++)Ps*=p[k];
			t_exp = (float)(2*j+B-A+1)*Ps+(float)(2*j+2*B-A+2)*(1-Ps);
			if(t_exp < expect)expect = t_exp;
		}
		cout << "Case #"<<i+1<<": ";
		cout << setiosflags(ios::fixed)<<setprecision(6)<<expect<<endl;
	}
	system("pause");
}