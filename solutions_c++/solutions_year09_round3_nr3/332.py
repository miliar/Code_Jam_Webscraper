#include <cstdio>
#include <cstdlib>
#include <iostream>

int cells[100];
int prisoners[5];
int nprisioners;

int costrelease(int pris) {
   int i=prisoners[pris];
   cells[i]=0;
   int res=0;
   for(int j=i-1;j>=0&&cells[j];j--) {
     res++;
   }
   for(int j=i+1;j<nprisioners&&cells[j];j++) {
     res++;
   }
   return res;
}

int release1(int p1) {
  int res=0;
  p1--;

  res+=costrelease(p1);

  cells[prisoners[p1]]=1;

  return res;
}

int release2(int p1,int p2) {
  int res=0;
  p1--;
  p2--;

  res+=costrelease(p1);
  res+=costrelease(p2);

  cells[prisoners[p1]]=1;
  cells[prisoners[p2]]=1;

  return res;
}

int release3(int p1,int p2,int p3) {
  int res=0;
  p1--;
  p2--;
  p3--;

  res+=costrelease(p1);
  res+=costrelease(p2);
  res+=costrelease(p3);

  cells[prisoners[p1]]=1;
  cells[prisoners[p2]]=1;
  cells[prisoners[p3]]=1;

  return res;
}

int release4(int p1,int p2,int p3,int p4) {
  int res=0;
  p1--;
  p2--;
  p3--;
  p4--;

  res+=costrelease(p1);
  res+=costrelease(p2);
  res+=costrelease(p3);
  res+=costrelease(p4);

  cells[prisoners[p1]]=1;
  cells[prisoners[p2]]=1;
  cells[prisoners[p3]]=1;
  cells[prisoners[p4]]=1;

  return res;
}

int release5(int p1,int p2,int p3,int p4,int p5) {
  int res=0;
  p1--;
  p2--;
  p3--;
  p4--;
  p5--;
  res+=costrelease(p1);
  res+=costrelease(p2);
  res+=costrelease(p3);
  res+=costrelease(p4);
  res+=costrelease(p5);

  cells[prisoners[p1]]=1;
  cells[prisoners[p2]]=1;
  cells[prisoners[p3]]=1;
  cells[prisoners[p4]]=1;
  cells[prisoners[p5]]=1;

  return res;
}

int min(int a, int b) {
  if(a<b) return a;
  else return b;
}

int min1() {
  int res=1000000;
  res=min(res,release1(1));
  return res;
}

int min2() {
  int res=1000000;
  res=min(res,release2(1,2));
  res=min(res,release2(2,1));
  return res;
}

int min3() {
  int res=1000000;
  res=min(res,release3(1,2,3));
  res=min(res,release3(1,3,2));
  res=min(res,release3(2,1,3));
  res=min(res,release3(2,3,1));
  res=min(res,release3(3,1,2));
  res=min(res,release3(3,2,1));
  return res;
}

int min4() {
  int res=1000000;
  res=min(res,release4(1,2,3,4));
  res=min(res,release4(1,2,4,3));
  res=min(res,release4(1,3,2,4));
  res=min(res,release4(1,3,4,2));
  res=min(res,release4(1,4,2,3));
  res=min(res,release4(1,4,3,2));
  res=min(res,release4(2,1,3,4));
  res=min(res,release4(2,1,4,3));
  res=min(res,release4(2,3,1,4));
  res=min(res,release4(2,3,4,1));
  res=min(res,release4(2,4,1,3));
  res=min(res,release4(2,4,3,1));
  res=min(res,release4(3,1,2,4));
  res=min(res,release4(3,1,4,2));
  res=min(res,release4(3,2,1,4));
  res=min(res,release4(3,2,4,1));
  res=min(res,release4(3,4,1,2));
  res=min(res,release4(3,4,2,1));
  res=min(res,release4(4,1,2,3));
  res=min(res,release4(4,1,3,2));
  res=min(res,release4(4,2,1,3));
  res=min(res,release4(4,2,3,1));
  res=min(res,release4(4,3,1,2));
  res=min(res,release4(4,3,2,1));
  return res;
}

int min5() {
  int res=1000000;
  res=min(res,release5(1,2,3,4,5));
  res=min(res,release5(1,2,4,3,5));
  res=min(res,release5(1,3,2,4,5));
  res=min(res,release5(1,3,4,2,5));
  res=min(res,release5(1,4,2,3,5));
  res=min(res,release5(1,4,3,2,5));
  res=min(res,release5(2,1,3,4,5));
  res=min(res,release5(2,1,4,3,5));
  res=min(res,release5(2,3,1,4,5));
  res=min(res,release5(2,3,4,1,5));
  res=min(res,release5(2,4,1,3,5));
  res=min(res,release5(2,4,3,1,5));
  res=min(res,release5(3,1,2,4,5));
  res=min(res,release5(3,1,4,2,5));
  res=min(res,release5(3,2,1,4,5));
  res=min(res,release5(3,2,4,1,5));
  res=min(res,release5(3,4,1,2,5));
  res=min(res,release5(3,4,2,1,5));
  res=min(res,release5(4,1,2,3,5));
  res=min(res,release5(4,1,3,2,5));
  res=min(res,release5(4,2,1,3,5));
  res=min(res,release5(4,2,3,1,5));
  res=min(res,release5(4,3,1,2,5));
  res=min(res,release5(4,3,2,1,5));
  res=min(res,release5(1,2,3,5,4));
  res=min(res,release5(1,2,4,5,3));
  res=min(res,release5(1,3,2,5,4));
  res=min(res,release5(1,3,4,5,2));
  res=min(res,release5(1,4,2,5,3));
  res=min(res,release5(1,4,3,5,2));
  res=min(res,release5(2,1,3,5,4));
  res=min(res,release5(2,1,4,5,3));
  res=min(res,release5(2,3,1,5,4));
  res=min(res,release5(2,3,4,5,1));
  res=min(res,release5(2,4,1,5,3));
  res=min(res,release5(2,4,3,5,1));
  res=min(res,release5(3,1,2,5,4));
  res=min(res,release5(3,1,4,5,2));
  res=min(res,release5(3,2,1,5,4));
  res=min(res,release5(3,2,4,5,1));
  res=min(res,release5(3,4,1,5,2));
  res=min(res,release5(3,4,2,5,1));
  res=min(res,release5(4,1,2,5,3));
  res=min(res,release5(4,1,3,5,2));
  res=min(res,release5(4,2,1,5,3));
  res=min(res,release5(4,2,3,5,1));
  res=min(res,release5(4,3,1,5,2));
  res=min(res,release5(4,3,2,5,1));
  res=min(res,release5(1,2,5,3,4));
  res=min(res,release5(1,2,5,4,3));
  res=min(res,release5(1,3,5,2,4));
  res=min(res,release5(1,3,5,4,2));
  res=min(res,release5(1,4,5,2,3));
  res=min(res,release5(1,4,5,3,2));
  res=min(res,release5(2,1,5,3,4));
  res=min(res,release5(2,1,5,4,3));
  res=min(res,release5(2,3,5,1,4));
  res=min(res,release5(2,3,5,4,1));
  res=min(res,release5(2,4,5,1,3));
  res=min(res,release5(2,4,5,3,1));
  res=min(res,release5(3,1,5,2,4));
  res=min(res,release5(3,1,5,4,2));
  res=min(res,release5(3,2,5,1,4));
  res=min(res,release5(3,2,5,4,1));
  res=min(res,release5(3,4,5,1,2));
  res=min(res,release5(3,4,5,2,1));
  res=min(res,release5(4,1,5,2,3));
  res=min(res,release5(4,1,5,3,2));
  res=min(res,release5(4,2,5,1,3));
  res=min(res,release5(4,2,5,3,1));
  res=min(res,release5(4,3,5,1,2));
  res=min(res,release5(4,3,5,2,1));
  res=min(res,release5(1,5,2,3,4));
  res=min(res,release5(1,5,2,4,3));
  res=min(res,release5(1,5,3,2,4));
  res=min(res,release5(1,5,3,4,2));
  res=min(res,release5(1,5,4,2,3));
  res=min(res,release5(1,5,4,3,2));
  res=min(res,release5(2,5,1,3,4));
  res=min(res,release5(2,5,1,4,3));
  res=min(res,release5(2,5,3,1,4));
  res=min(res,release5(2,5,3,4,1));
  res=min(res,release5(2,5,4,1,3));
  res=min(res,release5(2,5,4,3,1));
  res=min(res,release5(3,5,1,2,4));
  res=min(res,release5(3,5,1,4,2));
  res=min(res,release5(3,5,2,1,4));
  res=min(res,release5(3,5,2,4,1));
  res=min(res,release5(3,5,4,1,2));
  res=min(res,release5(3,5,4,2,1));
  res=min(res,release5(4,5,1,2,3));
  res=min(res,release5(4,5,1,3,2));
  res=min(res,release5(4,5,2,1,3));
  res=min(res,release5(4,5,2,3,1));
  res=min(res,release5(4,5,3,1,2));
  res=min(res,release5(4,5,3,2,1));
  res=min(res,release5(5,1,2,3,4));
  res=min(res,release5(5,1,2,4,3));
  res=min(res,release5(5,1,3,2,4));
  res=min(res,release5(5,1,3,4,2));
  res=min(res,release5(5,1,4,2,3));
  res=min(res,release5(5,1,4,3,2));
  res=min(res,release5(5,2,1,3,4));
  res=min(res,release5(5,2,1,4,3));
  res=min(res,release5(5,2,3,1,4));
  res=min(res,release5(5,2,3,4,1));
  res=min(res,release5(5,2,4,1,3));
  res=min(res,release5(5,2,4,3,1));
  res=min(res,release5(5,3,1,2,4));
  res=min(res,release5(5,3,1,4,2));
  res=min(res,release5(5,3,2,1,4));
  res=min(res,release5(5,3,2,4,1));
  res=min(res,release5(5,3,4,1,2));
  res=min(res,release5(5,3,4,2,1));
  res=min(res,release5(5,4,1,2,3));
  res=min(res,release5(5,4,1,3,2));
  res=min(res,release5(5,4,2,1,3));
  res=min(res,release5(5,4,2,3,1));
  res=min(res,release5(5,4,3,1,2));
  res=min(res,release5(5,4,3,2,1));
  return res;
}

int main() {
  int ncases=0;
  for(int i=0;i<100;i++) {
    cells[i]=1;
  }

  scanf(" %d",&ncases);

  for(int i=0;i<ncases;i++) {
    int ntorelease;
    scanf(" %d %d",&nprisioners,&ntorelease);
    for(int j=0;j<ntorelease;j++) {
      int iread;
      scanf(" %d",&iread);
      prisoners[j]=iread-1;
    }
    int res;
    switch(ntorelease) {
      case 1: res=min1(); break;
      case 2: res=min2(); break;
      case 3: res=min3(); break;
      case 4: res=min4(); break;
      case 5: res=min5(); break;
    }

    printf("Case #%d: %d\n",i+1,res);


  }

  return 0;

}










