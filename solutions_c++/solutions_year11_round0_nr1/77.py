#include<stdio.h>
#include<string.h>
int dis[110][110][110];
int que[2000010][3];
int qs,qe;
int in[110][2];
int main(){
    int t,i,cas=1,j;
    scanf("%d",&t);
    while(t--){
	int n;
	scanf("%d",&n);
	for(i=0;i<n;i++){
	    char c[3];
	    int k;
	    scanf("%s%d",c,&k);
	    in[i][1]=k;
	    if(c[0]=='O')in[i][0]=0;
	    else in[i][0]=1;
	}
	memset(dis,-1,sizeof(dis));
	dis[0][1][1]=0;
	qs=qe=0;
	que[0][0]=0;
	que[0][1]=1;
	que[0][2]=1;
	qe++;
	while(qs<qe){
	    int nx=que[qs][0],p1=que[qs][1],p2=que[qs][2];
	    qs++;
	    if(nx==n){
		printf("Case #%d: %d\n",cas++,dis[nx][p1][p2]);
		break;
	    }
	    if(in[nx][0]==0&&p1==in[nx][1]){
		for(i=-1;i<=1;i++){
		    int pp2=p2+i;
		    if(pp2<=0||pp2>100)continue;
		    if(dis[nx+1][p1][pp2]==-1){
			dis[nx+1][p1][pp2]=dis[nx][p1][p2]+1;
			que[qe][0]=nx+1;
			que[qe][1]=p1;
			que[qe][2]=pp2;
			qe++;
		    }
		}
	    }
	    if(in[nx][0]==1&&p2==in[nx][1]){
		for(i=-1;i<=1;i++){
		    int pp1=p1+i;
		    if(pp1<=0||pp1>100)continue;
		    if(dis[nx+1][pp1][p2]==-1){
			dis[nx+1][pp1][p2]=dis[nx][p1][p2]+1;
			que[qe][0]=nx+1;
			que[qe][1]=pp1;
			que[qe][2]=p2;
			qe++;
		    }
		}
	    }
	    for(i=-1;i<=1;i++){
		int pp1=p1+i;
		if(pp1<=0||pp1>100)continue;
		for(j=-1;j<=1;j++){
		    int pp2=p2+j;
		    if(pp2<=0||pp2>100)continue;
		    if(dis[nx][pp1][pp2]==-1){
			dis[nx][pp1][pp2]=dis[nx][p1][p2]+1;
			que[qe][0]=nx;
			que[qe][1]=pp1;
			que[qe][2]=pp2;
			qe++;
		    }
		}
	    }
	}
	//fprintf(stderr,"%d\n",qe);
    }
}
