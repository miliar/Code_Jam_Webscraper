#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

struct train {
  int st,fin;
};

int ansa,ansb,t,na,nb;
bool ba[110],bb[110];
train a[110],b[110];


bool compare_train(train a,train b) {
  return (a.st<b.st) || ((a.st==b.st) && (a.fin<b.fin));
}

void greedy(int code,int nt) {
  int nowa=1,nowb=1;
  //  printf("greedy %d %d\n",code,nt);
  while (1) {
    if (code==1) {
      while (nowa<=na) {
	if (ba[nowa] && nt+t<=a[nowa].st) {
	  ba[nowa]=false;
	  nt=a[nowa].fin;
	  code=3-code;
	  //	  printf("get %d %d %d\n",code,nowa,nt);
	  break;
	} else 
	  nowa++;
      }
      if (nowa>na) break;
    } else {
      while (nowb<=nb) {
	if (bb[nowb] && nt+t<=b[nowb].st) {
	  bb[nowb]=false;
	  nt=b[nowb].fin;
	  code=3-code;
	  //	  printf("get %d %d %d\n",code,nowb,nt);
	  break;
	} else 
	  nowb++;
      }
      if (nowb>nb) break;
    }
  }
}

int main() {
  int cases,kase=0;
  char ch;
  for (scanf("%d",&cases);cases>0;cases--) {
    int th,tm;
    ansa=0;ansb=0;
    memset(a,0,sizeof(a));
    memset(b,0,sizeof(b));
    scanf("%d",&t);
    scanf("%d%d",&na,&nb);
    for (int i=1;i<=na;i++) {
      scanf("%d%c%d",&th,&ch,&tm);
      a[i].st=th*60+tm;
      scanf("%d%c%d",&th,&ch,&tm);
      a[i].fin=th*60+tm;
      //      printf("%d %d %d\n",i,a[i].st,a[i].fin);
    }
    for (int i=1;i<=nb;i++) {
      scanf("%d%c%d",&th,&ch,&tm);
      b[i].st=th*60+tm;
      scanf("%d%c%d",&th,&ch,&tm);
      b[i].fin=th*60+tm;
      //      printf("%d %d %d\n",i,b[i].st,b[i].fin);
    }
    sort(a+1,a+na+1,compare_train);
    sort(b+1,b+nb+1,compare_train);
    memset(ba,1,sizeof(ba));
    memset(bb,1,sizeof(bb));
    int ka=0,kb=0;
    while (1) {
      ka=0;kb=0;
      for (int i=1;i<=na;i++) 
	if (ba[i]) {
	  ka=i;
	  break;
	}
      for (int i=1;i<=nb;i++)
	if (bb[i]) {
	  kb=i;
	  break;
	}
      //      printf("%d %d\n",ka,kb,a[ka].st);
      if (ka==0 || kb==0) break;
      if (a[ka].st<b[kb].st) {
	ba[ka]=false;
	ansa++;
	//	printf("shita %d\n",a[ka].fin);
	greedy(2,a[ka].fin);
      } else {
	bb[kb]=false;
	ansb++;
	//	printf("shitb %d\n",b[kb].fin);
	greedy(1,b[kb].fin);
      }
    }
    if (ka==0) {
      for (int i=1;i<=nb;i++) 
	if (bb[i]) ansb++;
    } else {
      for (int i=1;i<=na;i++)
	if (ba[i]) ansa++;
    }
    printf("Case #%d: %d %d\n",++kase,ansa,ansb);
  }
}
