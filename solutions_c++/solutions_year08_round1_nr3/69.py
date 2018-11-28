#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;

int a[30]={
	5,	27,	143,	751,	935,	607,	903,	991,	335,	47,
	943,471,55,		447,	463,	991,	95,		607,	263,	151,
	855,527,743,	351,	135,	407,	903,	791,	135,	647
};

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int Q,Num=0,n;
	cin >> Q;
	while (Q--){
		Num++;
		cin >> n;
		cout << "Case #" << Num << ": ";
		if (n==1) cout << "00";
		else if (n==2||n==10||n==13||n==17) cout << "0";
		cout << a[n-1] << endl;
	}
	return 0;
}