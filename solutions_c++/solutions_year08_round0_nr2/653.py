#include<cstdio>
#include<algorithm>

using namespace std;

struct train{
  int st,et;
  bool bt;
};
int ansa,ansb,i,t,s,I,w,T;
train Left[1000],Right[1000];

bool operator <(const train &a,const train &b){
  return a.st<b.st || a.st==b.st && a.et<b.et;
}

void in(train &o){
  int a,b,c,d;
  scanf("%d:%d %d:%d",&a,&b,&c,&d);
  o.st=a*60+b;o.et=c*60+d;
  o.bt=true;
}

void go2(int);

void go1(int a){
  for (int i=0;i<s;++i)
    if (Left[i].bt && Left[i].st>=a){
      Left[i].bt=false;
      go2(Left[i].et+w);
      return ;
    }
}

void go2(int a){
  for (int i=0;i<t;++i)
    if (Right[i].bt && Right[i].st>=a){
      Right[i].bt=false;
      go1(Right[i].et+w);
      return ;
    }
}

int mi;

main(){
  scanf("%d",&T);
  while (T--){
    scanf("%d",&w);
    scanf("%d%d",&s,&t);
    for (i=0;i<s;++i) in(Left[i]);
    sort(Left,Left+s);
    for (i=0;i<t;++i) in(Right[i]);
    sort(Right,Right+t);
    ansa=ansb=0;
    while (1){
      //      printf("%d %d\n",ansa,ansb);
      mi=10000000;
      for (i=0;i<s;++i) 
	if (Left[i].bt){
	  mi=Left[i].st;
	  break;
	}
      for (i=0;i<t;++i) 
	if (Right[i].bt) {
	  if (mi<Right[i].st) go1(0),++ansa;
	  else go2(0),++ansb;
	  mi=-1;
	  break;
	}
      if (mi>=1000000) break;
      else if (mi!=-1) go1(0),++ansa;
    }
    printf("Case #%d: %d %d\n",++I,ansa,ansb);
  }
}
