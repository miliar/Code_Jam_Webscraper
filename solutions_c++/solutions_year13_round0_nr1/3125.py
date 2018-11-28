#include<iostream>
#include<stdio.h>
using namespace std;
int i,i1,j,k,l,n,m;
char a[20][20];
char ch;
int did(int n1,int n2,int n3,int n4)
{
    int o1=0,o2=0;
    for(i=0;i<=3;i++)
    {
                     if(a[n1+i*n3][n2+i*n4]=='X')o1++;
                     else if(a[n1+i*n3][n2+i*n4]=='O')o2++;
                     else if(a[n1+i*n3][n2+i*n4]=='T'){o1++;o2++;}
                     else {break;}
    }
    if(o1==4)return 1;
    if(o2==4)return 2;
    return 0;
}
void print()
{
     if(k==1)printf("Case #%d: X won\n",i1);
     if(k==2)printf("Case #%d: O won\n",i1);
}
main()
{
      freopen("A-large.in","r",stdin);
      freopen("A-large.out","w",stdout);
      scanf("%d",&n);
      for(i1=1;i1<=n;i1++)
      {
              m=0;
              for(i=1;i<=4;i++)
              {
                               for(j=1;j<=4;j++)
                               {
                                                scanf("%c",&a[i][j]);
                                                while(a[i][j]!='X'&&a[i][j]!='O'&&a[i][j]!='T'&&a[i][j]!='.')scanf("%c",&a[i][j]);
                                                if(a[i][j]=='.')m=1;
                               }
              }
              k=did(1,1,0,1);
              if(k!=0){print();continue;}
              k=did(1,1,1,0);
              if(k!=0){print();continue;}
              k=did(1,1,1,1);
              if(k!=0){print();continue;}
              k=did(4,1,0,1);
              if(k!=0){print();continue;}
              k=did(4,1,-1,1);
              if(k!=0){print();continue;}
              k=did(1,4,1,0);
              if(k!=0){print();continue;}
              k=did(1,2,1,0);
              if(k!=0){print();continue;}
              k=did(1,3,1,0);
              if(k!=0){print();continue;}
              k=did(2,1,0,1);
              if(k!=0){print();continue;}
              k=did(3,1,0,1);
              if(k!=0){print();continue;}

              
              if(m==0)printf("Case #%d: Draw\n",i1);
              else printf("Case #%d: Game has not completed\n",i1);
              
      }
}
