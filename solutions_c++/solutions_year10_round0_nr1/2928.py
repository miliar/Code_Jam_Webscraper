#include<iostream>
using namespace std;
//有n个单元，可以按k次，初始全都是off，每次按的时候都是在电流能到的地方全部取反，初始电流只能到1
//问按k次后第n个是否是on且电流能到
//n=1,k=0; off
//n=1,k=1; on
//n=4 k=0 off
//n=4 k=4
// off off off off  k=0
//  on off off off  k=1
// off  on off off  k=2
//  on  on off off  k=3
// off off  on off  k=4
//  on off  on off  k=5
// off  on  on off  k=6
//  on  on  on off  k=7 
// off off off  on  k=8
//  on off off  on  k=9
// off  on off  on  k=10
//  on  on off  on  k=11
// off off  on  on  k=12
//  on off  on  on  k=13
// off  on  on  on  k=14
//  on  on  on  on  k=15            
//第一盏要亮需要1 第二盏要3 第三盏7，第4盏需要15 
// 如果有n盏灯，那么需要2^n-1 需要 2^n变回初始  　   
int main()
{
    int i,j,k,n,test,count=1;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&test); 
    while(test--)
    {
          scanf("%d%d",&n,&k);
          printf("Case #%d: ",count++);
          if(n>=27)puts("OFF");
          else
          {
              k%=(1<<n);
              if(k==(1<<n)-1)puts("ON");
              else puts("OFF");
              }       
          }
    return 0;
    }
