#include<iostream>
#include<cmath>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
    ifstream in;
    in.open("input.txt");
    ofstream out;
    out.open("output.txt");
    int n,t;
    in>>t;
    for(int prob=0;prob<t;prob++)
    {
            in>>n;
            int co[n][3];
            int v[n][3];
            for(int i=0;i<n;i++)
            in>>co[i][0]>>co[i][1]>>co[i][2]>>v[i][0]>>v[i][1]>>v[i][2];
            double x=0.0,y=0.0,z=0.0,vx=0.0,vy=0.0,vz=0.0;
            for(int i=0;i<n;i++)
            {
                    x=x+co[i][0];
                    y=y+co[i][1];
                    z=z+co[i][2];
                    vx=vx+v[i][0];
                    vy=vy+v[i][1];
                    vz=vz+v[i][2];
            }
            x=x/((double)n);
            y=y/((double)n);
            z=z/((double)n);
            double distx=x,disty=y,distz=z,dist;
            vx=vx/((double)n);
            vy=vy/((double)n);
            vz=vz/((double)n);
            cout<<x<<" "<<y<<" "<<z<<endl;
            double tmin=(vx*x+vy*y+vz*z)/(vx*vx+vy*vy+vz*vz);
            if(tmin<0)
            {
                      distx=x-(tmin*vx);
                      disty=y-(tmin*vy);
                      distz=z-(tmin*vz);
            }
            else
            tmin=0.0;
            dist=(distx*distx)+(disty*disty)+(distz*distz);
            dist=sqrt(dist);
            
            
            cout<<"Case #"<<prob+1<<": "<<dist<<" "<<(-1)*tmin<<endl;
            out<<"Case #"<<prob+1<<": "<<dist<<" "<<(-1)*tmin<<endl;
    }
    
    in.close();
    out.close();
    system("pause");
    return 0;
}
