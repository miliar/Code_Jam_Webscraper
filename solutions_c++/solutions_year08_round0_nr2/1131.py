#include <stdio.h>
#include <algorithm>
using namespace std;
int read(){
	char s[100]; scanf("%s",s);
	int hr, mi; 
	sscanf(s,"%d",&hr); sscanf(s+3,"%d",&mi);
	return hr*60+mi;
}


int main(){
	int tt; scanf("%d",&tt);
	for (int ti=1;ti<=tt;ti++){
		int T,na,nb; scanf("%d%d%d",&T,&na,&nb);
		int A1[na+1],A2[na+1], B1[nb+1],B2[nb+1];
		for (int i=0;i<na;i++){
			A1[i] = read();
			A2[i] = read()+T;
		}
		for (int i=0;i<nb;i++){
			B1[i] = read();
			B2[i] = read()+T;
		}
		A1[na]=A2[na]=B1[nb]=B2[nb]=1<<28;

		//for (int i=0;i<na;i++)printf("~~ %d %d\n",A1[i],A2[i]);
		//for (int i=0;i<nb;i++)printf("~~ %d %d\n",B1[i],B2[i]);
			
		sort(A1,A1+na); sort(A2,A2+na);
		sort(B1,B1+nb); sort(B2,B2+nb);
		
		int ans1=0,ans2=0;
		
		for (int i=0,j=0;i<na;i++){
			if (j==nb)ans1++;
			else{
				if (B2[j] <= A1[i])j++;
				else ans1++;
			}
		}

		for (int i=0,j=0;i<nb;i++){
			if (j==na)ans2++;
			else {
				if (A2[j]<=B1[i])j++;
				else ans2++;
			}
		}


		printf("Case #%d: %d %d\n",ti,ans1,ans2);
	}

	return 0;
}
