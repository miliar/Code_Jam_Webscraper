#include <iostream>
#include <fstream>
#include <math.h>
#include <string>
#include   <iomanip>
using namespace std;

int main()
{
    ifstream input;
    ofstream output;

    string inFileName,outFileName;
    cout<<"Please input the input file's location:"<<endl;
    cin>>inFileName;
    cout<<"Please input the output file's location:"<<endl;
    cin>>outFileName;
    input.open(inFileName.data());
    output.open(outFileName.data());

    int T;
    input>>T;

        for (int i=0;i<T;i++){
            int N,x ,y ,z ,vx ,vy ,vz;
            int totX=0,totY=0,totZ=0,totVx=0,totVy=0,totVz=0;
            double M0x,M0y,M0z;
            double Mvx,Mvy,Mvz;
            double t,dm;

            input>>N;
            for (int j=0;j<N;j++){
                input>>x>>y>>z>>vx>>vy>>vz;
                totX+=x;
                totY+=y;
                totZ+=z;
                totVx+=vx;
                totVy+=vy;
                totVz+=vz;
            }
            M0x=(double)totX/N;
            M0y=(double)totY/N;
            M0z=(double)totZ/N;

            Mvx=(double)totVx/N;
            Mvy=(double)totVy/N;
            Mvz=(double)totVz/N;

            if ((Mvx*Mvx+Mvy*Mvy+Mvz*Mvz)==0)
            t=0;
            else{
               t=-(Mvx*M0x+M0y*Mvy+M0z*Mvz)/(Mvx*Mvx+Mvy*Mvy+Mvz*Mvz);
               t=(t>0)?t:0;
            }
            dm=sqrt( (M0x+Mvx*t)*(M0x+Mvx*t)+(M0y+Mvy*t)*(M0y+Mvy*t)+(M0z+Mvz*t)*(M0z+Mvz*t) );

            cout.setf(cout.showpoint);
            cout.precision(8);
            cout.setf(ios::fixed);
            cout<<dm<<' '<<t<<endl;

            output.setf(cout.showpoint);
            output.precision(8);
            output.setf(ios::fixed);
            output<<"Case #"<<(i+1)<<": "<<dm<<' '<<t<<endl;

        }
        input.close();
        output.close();
        cout<<"result has been saved!"<<endl;
        return 0;


}




