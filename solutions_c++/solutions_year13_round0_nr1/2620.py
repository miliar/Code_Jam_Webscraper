#include<stdio.h>
const int n = 4;

int T;
char map[n+10][n+10];

int ans;

void input(){
    int i;
    for(i=0;i<n;i++)
	scanf("%s",map[i]);
}

void work(){
    int i,j,o,x,t;
    ans=0;
    for(i=0;i<n;i++){
	o=x=t=0;
	for(j=0;j<n;j++){
	    if(map[i][j]=='O')    
		o++;
	    else if(map[i][j]=='X')
		x++;
	    else if(map[i][j]=='T')
		t++;
	}
	if(x+t==4){
	    ans=1;
	    return;
	}
	if(o+t==4){
	    ans=2;
	    return;
	}
	o=x=t=0;
	for(j=0;j<n;j++){
	    if(map[j][i]=='O')
		o++;
	    else if(map[j][i]=='X')
		x++;
	    else if(map[j][i]=='T')
		t++;
	}
	if(x+t==4){
	    ans=1;
	    return;
	}
	if(o+t==4){
	    ans=2;
	    return;
	}
    }
    o=x=t=0;
    for(i=0;i<n;i++){
	if(map[i][i]=='X')
	    x++;
	else if(map[i][i]=='O')
	    o++;
	else if(map[i][i]=='T')
	    t++;
    }
    if(x+t==4){
	ans=1;
	return;
    }
    if(o+t==4){
	ans=2;
	return;
    }
    o=x=t=0;
    for(i=0;i<n;i++){
	if(map[i][n-1-i]=='X')
	    x++;
	else if(map[i][n-1-i]=='O')
	    o++;
	else if(map[i][n-1-i]=='T')
	    t++;
    }
    if(x+t==4){
	ans=1;
	return;
    }
    if(o+t==4){
	ans=2;
	return;
    }
    t=0;
    for(i=0;i<n;i++)
	for(j=0;j<n;j++)
	    t+=(map[i][j]=='.');
    if(t>0)
	ans=3;
}

void output(){
    printf("Case #%d: ",T);
    if(ans==0)
	printf("Draw\n");
    if(ans==1)
	printf("X won\n");
    if(ans==2)
	printf("O won\n");
    if(ans==3)
	printf("Game has not completed\n");
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int totT;
    scanf("%d",&totT);
    for(T=1;T<=totT;T++){
	input();
	work();
	output();
    }
    //while(1);
    return 0;
}
