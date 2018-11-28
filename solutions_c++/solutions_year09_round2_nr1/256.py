#include <iostream>
#include <cstdio>
#include <cstring>

using std::cout ;

int times,cases=0,L,A,n,inxn ;
char str[200][200],habit[200][200];
double ans[200];
struct node {
 double p;
 char spe[100];
 int left,right,r,c;      
} N[1000];

int cnt(int r,int c){
 int i,sum=0,TMP=inxn ;
 inxn++;
 double psum = 0 , pp=0.1 ;
 for(i=c+1;str[r][i]==' '||str[r][i]=='(';i++);
 for(;str[r][i]!='.';i++)
 sum*=10,sum+=(str[r][i]-'0');
 //printf("%d\n",sum);
 psum=sum;
 for(i++;str[r][i]>='0'&&str[r][i]<='9';i++)
 psum+=(str[r][i]-'0')*pp,pp/=10;
 for(;str[r][i]==' ';i++);

 if(str[r][i]==')'){
   N[TMP].left=N[TMP].right=-1;
   N[TMP].p=psum;
   N[TMP].r=r;N[TMP].c=i;
   return TMP;       
 } 
 else {
   int j,t=0;
   while(str[r][i]>='a'&&str[r][i]<='z')  
   N[TMP].spe[t++]=str[r][i++];
   N[TMP].spe[t]=0;
   N[TMP].p=psum;
   for(j=0;str[r+1][j];j++)
     if(str[r+1][j]=='('){
     N[TMP].left=cnt(r+1,j);
     break;
     }
   int tr = N[N[TMP].left].r;
   for(j=0;str[tr+1][j];j++)
     if(str[tr+1][j]=='('){
       N[TMP].right=cnt(tr+1,j);
       break;                      
     }   
   tr = N[N[TMP].right].r; 
   int tc = N[N[TMP].right].c;
   for(j=tc+1;str[tr][j];j++)
    if(str[tr][j]==')'){
     N[TMP].r=tr,N[TMP].c=j;
     return TMP;                   
    }
    for(j=0;str[tr+1][j];j++)
      if(str[tr+1][j]==')'){
     N[TMP].r=tr+1,N[TMP].c=j;
     return TMP   ;  
      }
 }
}
int input (){
 scanf("%d",&L);
 gets(str[0]);
 int i,j ;
 for(i=0;i<L;i++)
 gets(str[i]);
 inxn=0;
 for(i=0;i<L;i++)
    for(j=0;str[i][j];j++){
      if(str[i][j]=='('){
        cnt(i,j);
        return 0;                  
      }                       
    }
} 
int trace(int pos,double p,int index){
  if(N[pos].left==-1){
    ans[index]=p*N[pos].p;                    
  }  
  else {
   int  i;
   for(i=0;i<n;i++)
    if(strcmp(habit[i],N[pos].spe)==0)break;
    if(i<n)
    trace(N[pos].left,p*N[pos].p,index);
    else
    trace(N[pos].right,p*N[pos].p,index);     
  }
}
int sol(){

 scanf("%d",&A);
 int i , j ;
// for(i=0;i<inxn;i++){
 //  printf("%d %d %lf\n",N[i].left,N[i].right,N[i].p);                    
 //}
 char name[200];
 for(i=0;i<A;i++){
   scanf("%s %d",name,&n);
   for(j=0;j<n;j++)
   scanf("%s",habit[j]);
   trace(0,1,i);               
 }   
 cases++;
 printf("Case #%d:\n",cases);
 for(i=0;i<A;i++)
 printf("%.7lf\n",ans[i]);
}
int main (){
 scanf("%d",&times);
 while(times--){
   input ();
   sol();
 }   
}
