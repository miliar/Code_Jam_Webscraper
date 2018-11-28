#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <vector>
using namespace std;

int sizeofint(int a);


int main(){
    ifstream patternfile("A-small-attempt1.in");
    FILE * myfile;
    myfile =fopen("result.txt","w");
    int T;
    int A,B;   
    patternfile>>T;
    
    for(int i=0;i<T;i++){  
         patternfile>>A>>B;
         double *p;
         p= new double[A];
         for(int j=0;j<A;j++){
            patternfile>>p[j];
            cout<<p[j]<<",";
            
         }
         cout<<endl;
         
         if(A==1){
           double a1=p[0]* B   + (1-p[0])*(2*B);
           double a2=p[0]*(B+2)+ (1-p[0])*(1+B+1);
           double a3;
           if(a1>=a2) a3=a2;
           else a3=a1;
           
           fprintf(myfile,"Case #%d: %lf\n",i+1,a3);
         }else if(A==2){
           double p1=p[0]*p[1];
           double p2=p[0]*(1-p[1]);
           double p3=(1-p[0])*p[1];
           double p4=(1-p[0])*(1-p[1]);
           
           double a1=p1*(B-1)+ p2*2*B+ p3*2*B+ p4*2*B;
           double a2=p1*(B+1)+ p2*(B+1)  + p3*(B+2+B) + p4*(B+2+B);
           double a3=B+3;
           double a4=B+2;
           
           double a5;
           
           if(a1>=a2) a5=a2;
           else a5=a1;
           
           if(a5>=a4) a5=a4;
           
            fprintf(myfile,"Case #%d: %lf\n",i+1,a5);
         }else if(A==3){
           double p1=p[0]*p[1]*p[2];
           double p2=p[0]*p[1]*(1-p[2]);
           double p3=p[0]*(1-p[1])*p[2];
           double p4=(1-p[0])*p[1]*p[2];
           double p5=p[0]*(1-p[1])*(1-p[2]);
           double p6=(1-p[0])*(1-p[1])*p[2];
           double p7=(1-p[0])*p[1]*(1-p[2]);
           double p8=(1-p[0])*(1-p[1])*(1-p[2]);
           
           
           double a1= p1*(B-2)  + (1-p1)*(B-1+B);
           double a2= (p1+p2)*B + (1-p1-p2)*(B+1+B);
           double a3= (p1+p2+p3+p5)*(B+2)+ (p4+p6+p7+p8)*(B+B+3);
           double a4= B+4;
           double a5= B+2;
           
           double a6;
           if(a1>=a2) a6=a2;
           else a6=a1;
           
           if(a6>=a3) a6=a4;
           if(a6>=a5) a6=a5;
           
            fprintf(myfile,"Case #%d: %lf\n",i+1,a6);
           
         }
    }
         
            
    
    patternfile.close();
   fclose(myfile);
   // myfile.close();
system("pause");

}




