#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>
const int MaxN=1000+10;

using namespace std;
int a[MaxN][2],N,T,Ans;
int main(){
	scanf("%d", &T);
	char ch[10];
	for (int t=1;t<=T;t++){
		scanf("%d", &N);
		for (int i=0;i<N;i++){
			int x;
			scanf("%s %d", &ch, &a[i][0]);
			if (ch[0]=='O') a[i][1]=0;else
			a[i][1]=1;
		}
		int now1=1,now2=1,T1=0,T2=0;
		Ans=0;
		for (int i=0;i<N;i++){
			if (a[i][1]==0){
				if (abs(a[i][0]-now1)>Ans-T1) Ans=T1+abs(a[i][0]-now1);
				Ans++;
				T1=Ans;
				now1=a[i][0];
			}else{
				if (abs(a[i][0]-now2)>Ans-T2) Ans=T2+abs(a[i][0]-now2);
				Ans++;
				T2=Ans;
				now2=a[i][0];
			}
//cout << i << " " << T1 << " " << T2 << " " << Ans << endl;
		}
		printf("Case #%d: %d\n", t, Ans);
	}
	return 0;
}
