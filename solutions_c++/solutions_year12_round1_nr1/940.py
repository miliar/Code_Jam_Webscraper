#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
double arr[105000];
double p[105000];
double temp;
int t,l,r;
int a,b,c,d;
double best;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;
    int cas=0;
    while (t--)
    {
          cas++;
          temp=1.0;
          cin>>l>>r;
          best=2+r;
          for (a=1;a<=l;a++) {cin>>p[a]; temp*=p[a];}
          //temp��ȫ�Եĸ��ʡ�
          best=min(best,temp*(r-l+1)+(1-temp)*(r-l+2+r));
          arr[0]=1; //����i����ȫ�Եĵĸ���
          for (a=1;a<l;a++)
          {
              arr[a]=arr[a-1]*p[a]; //����a����ȫ��
              //�˸�Ȼ��fuck
              best=min(best,arr[a]*(l-a+r-a+1)+(1-arr[a])*(l-a+r-a+1+r+1));
          }
          printf("Case #%d: %.6lf\n",cas,best);
    }         
    return 0;
}                  
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
