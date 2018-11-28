#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cmath>
#include<algorithm>



using namespace std;


int main()
{
 int N;
 cin>>N;
 for(int i=0;i<N;i++)
 {
  cout<<"Case #"<<i+1<<": ";
  long long cant00=0,cant01=0,cant02=0,cant10=0,cant11=0,cant12=0,cant20=0,cant21=0,cant22=0;
  //Puntos con coordenadas multiplos, mas 1 y mas 2 a partir de esa x
  long long A,B,C,D,x0,y0,M,n;
  cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
  long long x=x0,y=y0;
  
for (int j=0; j<n;j++)
{
     if(x%3==0)
     {
       if(y%3==0)
        cant00++;
       if(y%3==1)
        cant01++;
       if(y%3==2)
        cant02++;           
     }
     if(x%3==1)
     {
       if(y%3==0)
        cant10++;
       if(y%3==1)
        cant11++;
       if(y%3==2)
        cant12++;           
     }
     if(x%3==2)
     {
       if(y%3==0)
        cant20++;
       if(y%3==1)
        cant21++;
       if(y%3==2)
        cant22++;           
     }
     x=(A*x+B)%M;
     y=(C*y+D)%M;
}
 cout<<(cant00*(cant00-1)*(cant00-2))/6+cant00*(cant01)*(cant02)+cant00*(cant10)*(cant20)
 +cant00*(cant11)*(cant22)+cant00*(cant12)*(cant21)+
 (cant01*(cant01-1)*(cant01-2))/6+cant01*(cant10)*(cant22)+cant01*(cant11)*(cant21)
 +cant01*(cant12)*(cant20)+
 (cant02*(cant02-1)*(cant02-2))/6+cant02*(cant10)*(cant21)+cant02*(cant11)*(cant20)
 +cant02*(cant12)*(cant22)+
 (cant10*(cant10-1)*(cant10-2))/6+cant10*(cant11)*(cant12)+
 (cant11*(cant11-1)*(cant11-2))/6+
 (cant12*(cant12-1)*(cant12-2))/6+
 (cant20*(cant20-1)*(cant20-2))/6+cant20*(cant21)*(cant22)+
  (cant21*(cant21-1)*(cant21-2))/6
  +(cant22*(cant22-1)*(cant22-2))/6<<endl;
 
 }
}
