#include <cstdio>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const double INF = 99999;

double solve(){
	int a,b;
	double tmp;
	cin >> a >> b;
	vector<double> pn;
	for(int i=0;i<a;i++){
		scanf("%lf",&tmp);
		pn.push_back(tmp);
	}
	vector<double> pb;
	double t;
	for(int i=0;i<=a;i++){
		if(i == a){
			t = pn[0];
			for(int j=1;j<i;j++){
				t *= pn[j];
			}
		}else if (i == 0){
			t = 1 - pn[0];
		}else{
			t = pn[0];
			for(int j=1;j<i;j++){
				t *= pn[j];
			}
			t *= (1 - pn[i]);
		}
		//cout << "pb[" << i << "] = " << t << endl;
		pb.push_back(t);
	}
	//pb[i] = i�Ԗڂ��O���S�Đ������Ai�Ԗڂ��������Ȃ��m��
	double ans = 0;
	double kt,bs,era;
	kt = pb[a] * (b - a + 1) + (1 - pb[a]) * (b - a + 1 + b + 1);
	//cout << "kt = " << pb[a] << " * " << (b - a + 1) << " + " << (1 - pb[a]) << " * " << (b - a + 1 + b + 1) << endl;
	era = 1 + b + 1;
	ans = kt < era ? kt : era;
	//cout << endl << "kt:" << kt << endl << "era:" << era << endl;
	double c,d;
	for(int i=1;i<=a;i++){
		//i:BS��������
		t = 0;
		/*
		for(int j=0;j<=a;j++){
			//pb[j]
			double tt;
			//cout << j  << " >= " << (a - i) << endl;
			if(j >= (a - i)){
				//�ԈႦ��������
				tt = pb[j] * (double)(i + i + (b - a) + 1);
			}else{
				//�����Ȃ�����
				tt = pb[j] * (double)((i + i) + (b - a + 1 + b + 1));
			}
			//cout << "tt(" << i << "," << j << ") = " << tt << endl;
			t += tt;
		}
		*/
		j
		//cout << i << ":" << t << endl;
		if(t < ans){
			ans = t;
		}
	}
	return ans;
}

int casen;

int main(){
	cin >> casen;
	for(int i=1;i<=casen;i++){
		cout << "Case #" << i << ": ";
		printf("%.6f\n",solve());
	}
}