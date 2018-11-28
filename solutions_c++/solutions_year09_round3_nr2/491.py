#include<vector>
#include<stdio.h>
#include<iostream>
#include<fstream>
#include<bitset>
#include<algorithm>
#include<string.h>
#include<math.h>

using namespace std;

int main()
{
    long long int temp,sum=0,max;
    int n_test_cases,n,i,j,k,N;
    char ch;
    double t,Vx,Vy,Vz,X,Y,Z,x[550],y[550],z[550],vx[550],vy[550],vz[550],d;
    
    long long int freq[1002];
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>n_test_cases;
    for(n=1;n<=n_test_cases;n++)
    {
                                fin>>N;
                                k=0;
                                for(i=0;i<=N-1;i++)
                                fin>>x[i]>>y[i]>>z[i]>>vx[i]>>vy[i]>>vz[i];
                                
                                X=Y=Z=Vx=Vy=Vz=0;
                                for(i=0;i<=N-1;i++)
                                {
                                                   Vx=Vx+vx[i];
                                                   Vy=Vy+vy[i];
                                                   Vz=Vz+vz[i];    
                                                   
                                                   X=X+x[i];
                                                   Y=Y+y[i];
                                                   Z=Z+z[i];               
                                }
                                Vx=Vx/N;Vy=Vy/N;Vz=Vz/N;
                                X=X/N;Y=Y/N;Z=Z/N;
                                
                                if(Vx==0 && Vy==0 && Vz==0)
                                t=0;
                                else
                                t=-1*(X*Vx+Y*Vy+Z*Vz)/(Vx*Vx+Vy*Vy+Vz*Vz);
                                
                                if(t<0)
                                t=0;
                                
                                cout<<Vx<<' '<<Vy<<' '<<Vz<<' '<<X<<' '<<Y<<' '<<Z<<endl;
                                
                                d=pow( ( ((X+t*Vx)*(X+t*Vx)) + ((Y+t*Vy)*(Y+t*Vy)) + ((Z+t*Vz)*(Z+t*Vz)) ) ,0.5) ;
                                
                                fout<<"Case #"<<n<<":";
                                fout<<' '<<d<<' '<<t;
                                fout<<endl;
                                                 
                                
    }
    fout.close();
    fin.close();
    
    
}
