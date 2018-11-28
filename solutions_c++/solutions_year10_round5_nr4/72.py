#include<iostream>
#include<ctime> 
using namespace std;

#define I 5
#define P 6
#define S 3
#define T 120
#define K 36

#define Dmax 
#define Dmin

#define DpVMAXmax 
#define DpVMAXmin
#define DpVMINmax
#define DpVMINmin

#define RDMAXmax
#define RDMAXmin
#define RDMINmax
#define RDMINmin

#define VDmax
#define VDmin

#define DepRMAXmax
#define DepRMAXmin
#define DepRMINmax
#define DepRMINmin

#define VSImax
#define VSImin

#define VSIPmax
#define VSIPmin

#define Ahmax
#define Ahmin
#define Bhmax
#define Bhmin
#define Chmax
#define Chmin

#define Almax
#define Almin
#define Blmax
#define Blmin
#define Clmax
#define Clmin

#define In1X 13
#define In1Y 28
double Input1[In1X][In1Y];
    
    
    /* Depot */
double Dipt[I][P][T]; //D[i][p][t], Demand of type (p) oil product to the depot(i) in operation time period (t)
double DpVMAXipt[I][P][T],DpVMINipt[I][P][T]; //The maximum and minimum storage of (p) in depot (i) in tiem(t)
double RDMAXip[I][P],RDMINip[I][P]; //The maximum and minimum download rate of (p) in depot (i)
double VDip[I][P]; //The beginning inventory of (p) in depot(i)
double RMAXip[I][P],RMINip[I][P]; //The maximum and minimum pipeline flow rate of (p) in the pipeline (i)
double VSi[I]; //The volume capacity of pipeline (i)
double VSip[I][P]; //The beginning volume capacity of oil product (p) in the pipeline (i)
    
    /* Refinery */
double VMAXpt[P][T],VMIN[P][T]; //The maximum and minimum supply volume capacity of (p) in time (t)
double RMAXps[P][S],RMINps[P][S]; //The maximum and minimum feasible flow rate of (p) by pumping configuration (s)
double VDp[P]; //The beginning inventory of (p) at the refinery
double Ahsp[S][P],Bhsp[S][P],Chsp[S][P]; //The coefficients of quadratic function about flow rate per unit during the peak time of electricity rates.
double Alsp[S][P],Blsp[S][P],Clsp[S][P]; //The coefficients of quadratic function about flow rate per unit during the normal time of electricity rates.
  

void read_input()
{
    int i,j;
    for(i=0;i<In1X;i++)
        for(j=0;j<In1Y;j++)
            scanf("%lf",&Input1[i][j]);
}

void show_input()
{
     int i,j;
     for(i=0;i<In1X;i++)
     {
         for(j=0;j<In1Y;j++)
             printf("%lf.0   ",Input1[i][j]);
         putchar('\n');
     }
}

int main()
{
    freopen("Download.txt","r",stdin);
    freopen("Oil Data.txt","w",stdout);
  
    read_input();
    show_input();
    
    generate_Dipt();
    generate_DpVMAX_MINipt();
    
    
    getchar();
    
    return 0;
} 
