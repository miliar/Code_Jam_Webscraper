#include <cstdio>
#include <cstdlib>
#include <cmath>
int extract(bool *p, char **q){
   *p=(79-**q)/13;
   *q+=2;
   int temp2=atoi(*q);
   *q+=(int)(log10(temp2))+2;
   return temp2;
}
int main(){
   int N,T;
   int t1,t2;
   int pos1,pos2;
   char temp,temp2,*list;
   bool bot, press[2];
   int *pos[2],*in[2];
   short size[2],step;
   scanf("%d", &T);
   char *pt;
   for(int i=0;i<T;i++){
      scanf("%d", &N);
      pos[0]=new int[N];pos[1]=new int[N];
      in[0]=new int[N];in[1]=new int[N];
      list=new char[N*5];
      size[0]=size[1]=step=0;
      getchar();
      gets(list);
      pt=list;
      for(int j=0;j<N;j++){
         temp=extract(&bot,&pt);
         pos[bot][size[bot]]=temp;
         in[bot][size[bot]++]=j;
         
      }
      t1=t2=0;
      pos1=pos2=1;
      while(t1<size[0]&&t2<size[1]){
		   press[0]=press[1]=1;
		   if(pos1!=pos[0][t1]){pos1+=abs(pos[0][t1]-pos1)/(pos[0][t1]-pos1);press[0]=0;}
		   if(pos2!=pos[1][t2]){pos2+=abs(pos[1][t2]-pos2)/(pos[1][t2]-pos2);press[1]=0;}
		   step++;
		   if(press[0]&&in[0][t1]<in[1][t2]){t1++;continue;}
			if(press[1]&&in[1][t2]<in[0][t1]){t2++;continue;}
		}
      while(t1<size[0]){
         step+=abs(pos1-pos[0][t1]);
			pos1=pos[0][t1];
			t1++;
			step++;
      }
      while(t2<size[1]){
         step+=abs(pos2-pos[1][t2]);
		   pos2=pos[1][t2];
			t2++;
			step++;
      }
      printf("Case #%d: %d\n", i+1,step);
      delete[] pos[1];
		delete[] pos[2];
		delete[] in[0];
		delete[] in[1];
		delete[] list;
   }
}
