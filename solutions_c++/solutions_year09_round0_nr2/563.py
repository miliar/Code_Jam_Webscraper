#include<cstdio>
#include<queue>
#include<list>
int dh[4]={-1,0,0,1};
int dw[4]={0,-1,1,0};
const int inf=2000000000;
using namespace std;
struct v{
     v(int alt=0): alt(alt), vis(false), sns(0), sink(NULL), c(0) {};
     int alt;
     bool vis;
     list<v*> sns;
     v* sink;
     char c;
};

v map[100][100];
int solve(int no) {
     printf("Case #%d:\n",no+1);
     int h,w;
     scanf("%d%d",&h,&w);
     int a;
     for (int i=0; i<h; i++) {
	  for (int j=0; j<w; j++) {
	       scanf("%d",&a);
	       map[i][j]=v(a);
	  }
     }
     int best,bk;
     for (int i=0; i<h; i++) {
	  for (int j=0; j<w; j++) {
	       bk=-1;
	       best=map[i][j].alt;
	       for (int k=0; k<4; k++) {
		    if (i+dh[k]>=0 && i+dh[k]<h && j+dw[k]>=0 && j+dw[k]<w) {
		//	 printf("%d %d (%d)-> %d %d (%d); %d \n",i,j,map[i][j].alt,i+dh[k],j+dw[k],map[i+dh[k]][j+dw[k]].alt,best);
			 if (map[i+dh[k]][j+dw[k]].alt<best) {
			      bk=k;
			      best=map[i+dh[k]][j+dw[k]].alt;
			 }
		    }
	       }
	       if (bk==-1) {
		//    printf("%d %d sink\n",i,j);
		    map[i][j].sink=&map[i][j];
		    continue;
	       }
	       map[i+dh[bk]][j+dw[bk]].sns.push_back(&map[i][j]);
	       
	  }
     }
     queue<v*> Q;
     for (int i=0; i<h; i++) {
	  for (int j=0; j<w; j++) {
	       if (map[i][j].sink!=&map[i][j]) continue;
	       Q.push(&map[i][j]);
	       map[i][j].vis=true;
	       while(!Q.empty()) {
		    v* cur=Q.front();
		    Q.pop();
		    for (list<v*>::iterator it=cur->sns.begin(); it!=cur->sns.end();it++) {
			 if ((*it)->vis) continue;
			 (*it)->vis=true;
			 Q.push(*it);
			 (*it)->sink=&map[i][j];
		    }
	       }
	  }
     }
     char cur='a';
     for (int i=0; i<h; i++) {
	  for (int j=0; j<w; j++) {
	       if (map[i][j].sink->c==0) {
		    map[i][j].sink->c=cur;
		    cur++;
	       }
	       printf("%c ",map[i][j].sink->c);
	  }
	  printf("\n");
     }
     return 0;
}

int main() {
     int t;
     scanf("%d",&t);
     for (int i=0; i<t; i++) solve(i);
     return 0;
  
}