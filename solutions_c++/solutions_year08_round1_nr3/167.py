#include<stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
using namespace std;

int ret[]={1,5,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,
95,607,263,151,855,527,743,351,135,407,903,791,135,647,343};//using windows calc

int main(){
	int T,tt;
	scanf("%d",&T);
	for(tt=1;tt<=T;tt++){
		int n;
		scanf("%d",&n);
		//cout<<sizeof(long double)<<endl;
		printf("Case #%d: %.3d\n",tt,ret[n]);
	}
}
