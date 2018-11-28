#include<iostream>
#include <fstream>
#include<cmath>
using namespace std;
    ofstream fout ("file.out");
    ifstream fin ("file.in");
    const double tt=0.00001;
    void pri(int i,double j1,double j2){
         fout.setf(ios::fixed,ios::floatfield);
         fout.precision(8);
         fout<<"Case #"<<i+1<<": "<<j1<<" "<<j2<<endl;
    }
int main(){
    int n;
    fin>>n;
    for(int i=0;i<n;i++){
      int k;
      fin>>k;
      int a[6],x;
      for(int j=0;j<6;j++)
        a[j]=0;
      for(int j=0;j<k;j++)
        for(int t=0;t<6;t++){
          fin>>x;
          a[t]+=x;
        }
      double b[6];
      bool mark=true;
      for(int j=3;j<6;j++)
        if(a[j]!=0){
          mark=false;
          break;
        }
      for(int j=0;j<6;j++)
        b[j]=(double)a[j]/k;
      double c1=b[0]+b[3],c2=b[1]+b[4],c3=b[2]+b[5];
      double d1=b[0]*c2-b[1]*c1,d2=b[1]*c3-b[2]*c2,d3=b[2]*c1-b[0]*c3;
      double dm=sqrt(d1*d1+d2*d2+d3*d3)/sqrt(b[3]*b[3]+b[4]*b[4]+b[5]*b[5]);
      double tm=sqrt(b[0]*b[0]+b[1]*b[1]+b[2]*b[2]-dm*dm)/sqrt(b[3]*b[3]+b[4]*b[4]+b[5]*b[5]);
      if(mark||(sqrt(b[0]*b[0]+b[1]*b[1]+b[2]*b[2])
               <sqrt((b[0]+tt*b[3])*(b[0]+tt*b[3])+(b[1]+tt*b[4])*(b[1]+tt*b[4])+(b[2]+tt*b[5])*(b[2]+tt*b[5])))){
               tm=0;
               dm=sqrt(b[0]*b[0]+b[1]*b[1]+b[2]*b[2]);
               }
      pri(i,dm,tm);
    }
    return 0;
}
      
          
    
