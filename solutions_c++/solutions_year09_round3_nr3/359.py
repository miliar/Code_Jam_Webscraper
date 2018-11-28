#include<iostream>

using namespace std;

int main()
{
 int i,j,k,N,c,l;
 int cuts[1000],cuts1[1000],in,cas=0;
 cin>>N;
 while(cas++<N)
 {
  int Arr[150][150]={0};
  int Temp[1001]={0};
  cin>>l>>c;
  cuts1[0]=0;
  for(i=0;i<c;i++)
   {
    cin>>cuts[i];
    cuts1[i+1]=cuts[i];
   }
   
  cuts[c]=l;
  for(i=0;i<=c;i++)
     Arr[i][i]=0;
     
  for(i=1;i<=c;i++)
  {
    for(j=0;j<=c-i;j++)
     {
        in=0;
        for(k=j;k<i+j;k++)
        {
          Temp[in++]=Arr[j][k]+Arr[k+1][i+j];
        }
        Arr[j][j+i]=Temp[min_element(Temp,Temp+in)-Temp]+cuts[j+i]-cuts1[j]-2;
        if(cuts[j+i]==l) Arr[j][j+i]++;
      }
   }
   cout<<"Case #"<<cas<<": "<<Arr[0][c]<<endl;
     
  }
  return 0;
}

