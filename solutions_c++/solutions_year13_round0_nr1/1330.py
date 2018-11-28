#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int X=4, Y=4;

const string state [4]={"X won","O won","Draw","Game has not completed"};
int a[X][Y];
void result(int msg, int no){
    cout<<"Case #"<<no<<": "<<state[msg]<<endl;
}

int solve(){
   int cstate=2;
   for (int iy=0; iy<4; iy++)
       for (int ix=0; ix<4; ix++)
       {
           char c; cin>>c;
           a[ix][iy]=(c=='T')?3:(c=='X')?2:(c=='O')?1:0;
       }

   // ROW
   int proc=0;
   int cx=0,co=0;
   for (int iy=0; iy<4; iy++)
   {
       cx=co=0;
       for (int ix=0; ix<4; ix++)
       {
           if(a[ix][iy]==1 || a[ix][iy]==3) co++;
           if(a[ix][iy]==2 || a[ix][iy]==3) cx++;
           if (a[ix][iy]!=0) proc++;
       }

       if (cx==4) cstate=0;
       if (co==4) cstate=1;
   }

   // COL
   cx=0,co=0;
   for (int iy=0; iy<4; iy++)
   {
       cx=co=0;
       for (int ix=0; ix<4; ix++)
       {
           if(a[iy][ix]==1 || a[iy][ix]==3) co++;
           if(a[iy][ix]==2 || a[iy][ix]==3) cx++;
       }
       if (cx==4) cstate=0;
       if (co==4) cstate=1;
   }

   // DIA 1
   cx=0,co=0;
   for (int ix=0; ix<4; ix++)
   {
       if(a[ix][ix]==1 || a[ix][ix]==3) co++;
       if(a[ix][ix]==2 || a[ix][ix]==3) cx++;
   }
   if (cx==4) cstate=0;
   if (co==4) cstate=1;

   // DIA 2
   cx=0,co=0;
   for (int ix=0; ix<4; ix++)
   {
       if(a[3-ix][ix]==1 || a[3-ix][ix]==3) co++;
       if(a[3-ix][ix]==2 || a[3-ix][ix]==3) cx++;
   }
   if (cx==4) cstate=0;
   if (co==4) cstate=1;

   return (cstate==0 || cstate==1)?cstate:(proc==16)?2:3;
}

int main()
{
    int t; cin>>t;
    for (int i=1; i<=t; i++)
        result(solve(),i);
    return 0;
}



