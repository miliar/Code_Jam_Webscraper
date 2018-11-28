#include<iostream>
#include<stdio.h>


using namespace std;

void main(){
	freopen("input.txt","rb",stdin);
	freopen ("out.txt","w",stdout);

	int T;
	cin>>T;
	int u=T;
	while(u--){
		int n,p;
		char r;

		cin>>n;

		int button[1001];
		char color[1001];
		for(int i=0;i<1001;i++){button[i]=-1;color[i]=0;}
		for(int i=0;i<n;i++){
			cin>>color[i]>>button[i];
		}
		
#define INF -10000
		int time=0;

		for(;time<100000;time++){
			int j;
			char tb=0,to=0;
			for(j=0;j<n;j++)
				if(button[j]!=INF)break;

			if(j==n)break;

			if(button[j]==0){
				button[j]=INF;color[j]=='B'?tb=1:to=1;
			}

			int bm=-1,om=-1;
			int i;
			for(i=j;i<n;i++)
				if(color[i]=='B')
					if(button[i]==0)tb=1;
					else{
						if(button[i]<0)bm=1;
						break;
					}

			for(i=j;i<n;i++)
				if(color[i]=='O')
					if(button[i]==0)to=1;
					else{
						if(button[i]<0)om=1;
						break;
					}

			


			if(!(tb==1 && to==1))
				for(int i=j;i<n;i++)
					if((tb==0 && color[i]=='B'))button[i]+=bm;
					else if((to==0 && color[i]=='O'))button[i]+=om;
		}

		printf("Case #%d: %d\n",T-u,time-1);
	}
}