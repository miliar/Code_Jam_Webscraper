#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>

using namespace std;
#define EP 100000000
double rpow(double x,int n){
	if(n==1) return x;
	else{
		double t;
		t=rpow(x,n/2);
		t*=t;
		if(t>(EP*1.0)){
			int ii=(int)t;
			t=t-((ii/EP)*EP*1.0);				
		}
		if(n%2==1){
			t*=x;
			if(t>(EP*1.0)){
				int ii=(int)t;
				t=t-((ii/EP)*EP*1.0);				
			}
		}
		return t;
	}
}
int table[32]={ 0,0,
				27,143,// 2,3
				751,935,
				607,903,
				991,335,
				47,943,
				471,55,
				447,463,
				991,95,
				607,263,
				151,855,
527,743,
351,135,
407,903,
791,135,
647,0
};
int main()
{	

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt1.out","w",stdout);

	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		int n;
		scanf("%d",&n);
		//double base=sqrt(5)+3;
		//double re=rpow(base,n);
		//int res=(int)floor(re);
		printf("%03d\n",table[n]);
	}
	return 0;
}