// watersheds

#include <stdio.h>
#define MAXLEN 110
#define MAXNUM (MAXLEN*MAXLEN)
#define VID(r,c) ((r)*cn+c)

class Node {
  public:
    int id,rank;
    Node *rep;
    void Init(int nid) {
      id=nid;
      rank=0;
      rep=this;
    }
    Node *Rep(void) {
      if(rep!=this) rep=rep->Rep();
      return rep;
    }
};

void Union(Node *v,Node *u) {
  v=v->Rep();
  u=u->Rep();
  if(v!=u) {
    if(v->rank<u->rank) {
      v->rep=u;
    } else {
      u->rep=v;
      if(v->rank==u->rank) v->rank++;
    }
  }
}

const int dir[4][2]={-1,0, 0,-1, 0,1, 1,0};

int rn,cn,num;
int h[MAXLEN][MAXLEN];
char ch,color[MAXNUM];
Node v[MAXNUM];

inline bool Valid(int r,int c)
{
  return (r>=0&&r<rn&&c>=0&&c<cn);
}

void Solve(void)
{
  int i,j,k,ni,nj,mi,mj,mh;
  for(i=0;i<rn;i++)
    for(j=0;j<cn;j++)
      v[VID(i,j)].Init(VID(i,j));
  for(i=0;i<rn;i++) {
    for(j=0;j<cn;j++) {
      mh=h[i][j];
      mi=mj=-1;
      for(k=0;k<4;k++) {
	ni=i+dir[k][0];
	nj=j+dir[k][1];
	if(Valid(ni,nj)&&h[ni][nj]<mh) {
	  mh=h[ni][nj];
	  mi=ni;
	  mj=nj;
	}
      }
      if(mi!=-1) {
	Union(v+VID(i,j),v+VID(mi,mj));
      }
    }
  }
  for(i=0;i<num;i++)
    color[i]=0;
  ch='a';
  for(i=0;i<rn;i++) {
    for(j=0;j<cn;j++) {
      if(!color[v[VID(i,j)].Rep()->id]) color[v[VID(i,j)].Rep()->id]=ch++;
      printf("%c",color[v[VID(i,j)].Rep()->id]);
      if(j<cn-1) printf(" ");
      else printf("\n");
    }
  }
}

int main(void)
{
  int t,casenum;
  int i,j;
  scanf("%d",&t);
  for(casenum=1;casenum<=t;casenum++) {
    scanf("%d %d",&rn,&cn);
    num=rn*cn;
    for(i=0;i<rn;i++)
      for(j=0;j<cn;j++)
	scanf("%d",h[i]+j);
    printf("Case #%d:\n",casenum);
    Solve();
  }
  return 0;
}
