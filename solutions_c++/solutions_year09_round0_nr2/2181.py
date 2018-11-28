#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<iostream>
int map[100][100],h,w;
int x[4]={-1,0,0,1};
int y[4]={0,-1,1,0};
char color[100][100];
int q[10050][2],p,co,t;
void flood(int a,int b){
	bool flag=true;
	int s[4],i,xt,yt,mem,cot;
	for(i=0;i<4;i++)
		s[i]=11000;
	p=1;
	q[p][0]=a;
	q[p][1]=b;
	while(flag){
		flag=false;
		for(i=0;i<=3;i++){
			xt=q[p][0]+x[i];
			yt=q[p][1]+y[i];
			if(xt>=0&&yt>=0&&xt<h&&yt<w)
				s[i]=map[xt][yt];
		}
		mem=0;
		for(i=1;i<=3;i++)
			if(s[i]<s[mem])
				mem=i;
		if(map[q[p][0]][q[p][1]]>s[mem]){
			p++;
			flag=true;
			q[p][0]=q[p-1][0]+x[mem];
			q[p][1]=q[p-1][1]+y[mem];
		}
	}
	if(color[q[p][0]][q[p][1]]==0)
		color[q[p][0]][q[p][1]]=++co;
	cot=color[q[p][0]][q[p][1]];
	for(i=1;i<=p-1;i++)
		color[q[i][0]][q[i][1]]=cot;
}

int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&t);
	int i,j,k;
	for(i=1;i<=t;i++){
		co=0;
		memset(color,0,sizeof(color));
		scanf("%d%d",&h,&w);
		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
				scanf("%d",&map[j][k]);
		for(j=0;j<h;j++)
			for(k=0;k<w;k++)
				if(color[j][k]==0)
					flood(j,k);
		printf("Case #%d: \n",i);
		for(j=0;j<h;j++){
			for(k=0;k<w;k++)
				printf("%c ",color[j][k]+'a'-1);
		    printf("\n");
	    }
	}
    return 0;
}