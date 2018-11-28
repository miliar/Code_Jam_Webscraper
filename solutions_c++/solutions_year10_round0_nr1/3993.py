#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int t=0;
	scanf("%d",&t);
	int w=0;
	while(t--){
	//	int w=0;
		w++;
		int n=0;
		long int k=0;
		scanf("%d",&n);
		scanf("%d",&k);
		int AA[30];
		for(int i=0; i<30; i++)   AA[i]=0;
		for(int i=0; i<n; i++){
			int x=1;
			for(int j=0; j<i+1; j++)  x*=2;
			if(k%x>= x/2) AA[i]=1;
		}
		int flag=1;
		for(int i=0; i<n; i++){
			if(AA[i]==0) flag=0;
		}
		if(flag){
			printf("Case #%d: ON\n",w);
		}else{
			printf("Case #%d: OFF\n",w);
		}
	}

	return 0;
}

