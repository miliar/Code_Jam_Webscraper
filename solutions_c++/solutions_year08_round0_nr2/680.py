#include<iostream>
#include<algorithm>
using namespace std;
int A,B,buffA,buffB;
int t,a,b;
int arrA[110],depA[110],arrB[110],depB[110];
int main()
{
  int T;
  int p,q,r,s,j,k;
  scanf("%d",&T);
  for(int i=1;i<=T;i++){
    A=B =buffA=buffB=0;
    scanf("%d",&t);
    scanf("%d %d",&a,&b);
    for(j=0;j<a;j++){
        scanf("%d:%d %d:%d",&p,&q,&r,&s);
        depA[j]=p*60+q;
        arrB[j]=r*60+s+t;
      //  if(arrB[j] >= 1440) arrB[j] -= 1440;
    }
    
    for(j=0;j<b;j++){
        scanf("%d:%d %d:%d",&p,&q,&r,&s);
        depB[j]=p*60+q;
        arrA[j]=r*60+s+t;
//        if(arrA[j] >= 1440) arrA[j] -= 1440;   
    }
    sort(depA,depA+a);
    sort(arrA,arrA+b);
    sort(depB,depB+b);
    sort(arrB,arrB+a);
    j=k=0;
    while(j<a && k<b){
        if(depA[j] < arrA[k]){
          if(buffA==0)
            A++;
          else
            buffA--;
          j++;
        }
        else{
          buffA++;
          k++;
        }
    }
    if(a-j-buffA > 0)
      A+=a-j-buffA;
    j=k=0;
    while(j<b && k<a)
    {
      if(depB[j]<arrB[k]){
        if(buffB==0)
          B++;
        else
          buffB--;
        j++;
      }
      else{
        buffB++;
        k++;
      }
    }
    if(b-j-buffB > 0)
      B+=b-j-buffB;
        
    printf("Case #%d: %d %d\n",i,A,B);
  }
}

