#include <cstdio>
#include <cmath>
#include <iostream>

using namespace std;

int m[200][200];
char sol[200][200];
char c;

char llena(int j,int k){
	int pos=0;
	int val =m[j][k];
	//printf("%d %d ",j,k);
	if(m[j-1][k]!=-1 && m[j-1][k]<val ){
		val=min(val,m[j-1][k]);
		pos=1;
	}
	if(m[j][k-1]!=-1 && m[j][k-1]<val){
		val=min(val,m[j][k-1]);
		pos=2;
	}
	if(m[j][k+1]!=-1 && m[j][k+1]<val){
		val=min(val,m[j][k+1]);
		pos=3;
	}
	if(m[j+1][k]!=-1 && m[j+1][k]<val){
		val=min(val,m[j+1][k]);
		pos=4;
	}
	//printf("%d\n",pos);
	if(pos==0){
		//puts("acaso entra??");
		sol[j][k]=c;
		c++;
		return sol[j][k];
	}
	int j1=j,k1=k;
	switch(pos){
		case 1:
			j1--;
		break;
		case 2:
			k1--;
		break;
		case 3:
			k1++;
		break;
		case 4:
			j1++;
		break;
	}
	if(sol[j1][k1]!=0) {
		sol[j][k]=sol[j1][k1];
		return (sol[j][k]);
	}else
		sol[j][k]=llena(j1,k1);
	return sol[j][k];
}

int main(){
	int n,x,y;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d%d",&x,&y);
		memset(m,-1,sizeof(m));
		memset(sol,0,sizeof(sol));
		for(int j=1;j<=x;j++)
			for(int k=1;k<=y;k++)
				scanf("%d",&m[j][k]);
		c='a';
		int pos=0,val;
		for(int j=1;j<=x;j++)
			for(int k=1;k<=y;k++){
				pos = 0;
				if(sol[j][k]!=0) continue;
				val =m[j][k];
				if(m[j-1][k]!=-1 && m[j-1][k]<val){
					val=min(val,m[j-1][k]);
					pos=1;
				}
				if(m[j][k-1]!=-1 && m[j][k-1]<val){
					val=min(val,m[j][k-1]);
					pos=2;
				}
				if(m[j][k+1]!=-1 && m[j][k+1]<val){
					val=min(val,m[j][k+1]);
					pos=3;
				}
				if(m[j+1][k]!=-1 && m[j+1][k]<val){
					val=min(val,m[j+1][k]);
					pos=4;
				}
				//printf("aa %d %d %d\n",j,k,pos);
				if(pos==0){
					//puts("entra??");
					sol[j][k]=c;
					c++;
					continue;
				}
				int j1=j,k1=k;
				switch(pos){
					case 1:
						j1--;
					break;
					case 2:
						k1--;
					break;
					case 3:
						k1++;
					break;
					case 4:
						j1++;
					break;
				}
				if(sol[j1][k1]!=0) sol[j][k]=sol[j1][k1];
				else{
					sol[j][k]=llena(j1,k1);
				}
			}
			printf("Case #%d:\n",i);
			for(int j=1;j<=x;j++)
			for(int k=1;k<=y;k++)
				printf("%c%c",sol[j][k],(k<=(y-1))?' ':'\n');
	}
	return 0;
}

