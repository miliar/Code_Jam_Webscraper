#include <math.h>
#include <conio.h>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>


using namespace std;
FILE *fin,*fout;
int N;
string n_2_s(long long n);
int main()
{
   fin=fopen("C:/Documents and Settings/iconoclast/Desktop/codejam/B-large.in","r"); 
   fout=fopen("C:/Documents and Settings/iconoclast/Desktop/codejam/B-large.out","w");
   cout<<"amup";
   fscanf(fin,"%d\n",&N); 
   cout<<N;   
   for(int i=1;i<=N;i++)
   {int n;
    vector<int> x,y,z,vx,vy,vz;
     fscanf(fin,"%d\n",&n);
     
     for(int j=0;j<n;j++)
     {int i1,i2,i3,i4,i5,i6;
       fscanf(fin,"%d %d %d %d %d %d\n",&i1,&i2,&i3,&i4,&i5,&i6); 
       x.push_back(i1); 
       y.push_back(i2); 
        z.push_back(i3); 
        vx.push_back(i4); 
        vy.push_back(i5); 
        vz.push_back(i6);   
     } 
     double Cx=0.0,Cy=0.0,Cz=0.0,Vx=0.0,Vy=0.0,Vz=0.0,tmin=0.0,dmin=0.0;
      for(int j=0;j<n;j++)
      {Cx=Cx+x[j];Cy+=y[j];Cz+=z[j];
       Vx+=vx[j];Vy+=vy[j];Vz+=vz[j];       
      }      
      Cx=Cx/n;Cy=Cy/n;  Cz=Cz/n;  Vx=Vx/n;Vy=Vy/n; Vz=Vz/n; 
      if((Vx*Vx+Vy*Vy+Vz*Vz) == 0.0) tmin=0;
      else      
       tmin=(-1.0*(Cx*Vx+Cy*Vy+Cz*Vz))/(Vx*Vx+Vy*Vy+Vz*Vz);
       if (tmin<0) tmin=0;
       dmin=sqrt((Cx+tmin*Vx)*(Cx+tmin*Vx)+ (Cy+tmin*Vy)*(Cy+tmin*Vy)+(Cz+tmin*Vz)*(Cz+tmin*Vz));
       
       fprintf(fout,"Case #%d: %10.10f %10.10f\n",i,dmin,tmin);   
           
   }
   
   cout<<"***end***"; 
   fclose(fin);
   fclose(fout);
   getch(); 
 return 0;   
}

string n_2_s(long long n)
{string s;char c;
do
{c=48+n%10;s.insert(0,1,c);n=n/10;
        
}while(n !=0);
       
 return s;      
       
}       
