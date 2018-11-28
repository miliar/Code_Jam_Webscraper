#include <stdio.h>
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define SIZE 1000

int T,n;
int arr[SIZE+2][2];


int ccw(int x0,int y0,int x1,int y1,int x2,int y2)
{
	return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);
}

bool intersect(int y0[2],int y1[2]){
	int s1,s2,s3,s4;
	
	s1=ccw(0,y0[0],1,y0[1],0,y1[0]);
	s2=ccw(0,y0[0],1,y0[1],1,y1[1]);
	s3=ccw(0,y1[0],1,y1[1],0,y0[0]);
	s4=ccw(0,y1[0],1,y1[1],1,y0[1]);
	
	if(s1*s2<0 && s3*s4<0) return true;
	return false;
}



void process(){
	int i,j;
	bool flag;
	int ans=0;
	FOR(i,1,n){
		FOR(j,i+1,n){
			flag=	intersect(arr[i],arr[j]);
			if (flag){
				ans++;
			}
		}
	}
	printf("Case #%d: %d\n",T,ans);
}

void input(){
	int i;
	scanf("%d",&n);
	FOR(i,1,n){
		scanf("%d %d",&arr[i][0],&arr[i][1]);
	}
}

int main(){
	int t;
	freopen("A-large.in","r",stdin);
	freopen("output","w",stdout);
	scanf("%d",&t);
	FOR(T,1,t){
		input();
		process();
	}
	return 0;
}
