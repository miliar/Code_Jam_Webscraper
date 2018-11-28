#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int i,t,j,n,x,a,b;
    float prob[10]={0},pro[5][8]={0},p[8],ans[3],an;
    ofstream ot;
    ifstream in ("input.txt");
    ot.open("output.txt");
    in>>t;
    for(j=1;j<=t;j++)
    {
        in>>a>>b;
        for(i=0;i<a;i++)
        in>>prob[i];
        if(a==1)
        {
           pro[0][0]=b*prob[0];
           pro[0][1]=(2*b+1)*(1-prob[0]);
           pro[1][0]=(b+2)*prob[0];
           pro[1][1]=(b+2)*(1-prob[0]);
           pro[2][0]=(b+2)*prob[0];
           pro[2][1]=(b+2)*(1-prob[0]);
           ans[0]=pro[0][1]+pro[0][0];
           ans[1]=pro[1][1]+pro[1][0];
           ans[2]=pro[2][1]+pro[2][0];
           an=(ans[0]>ans[1])?ans[1]:ans[0];
           an=(an>ans[2])?ans[2]:an;
        }
        else if(a==2)
        {
           pro[0][0]=(b-1)*prob[0]*prob[1];
           pro[0][1]=(2*b)*prob[0]*(1-prob[1]);
           pro[0][2]=(2*b)*prob[1]*(1-prob[0]);
           pro[0][3]=(2*b)*(1-prob[0])*(1-prob[1]);
           pro[1][0]=(b+1)*prob[0]*prob[1];
           pro[1][1]=(b+1)*prob[0]*(1-prob[1]);
           pro[1][2]=2*(b+1)*prob[1]*(1-prob[0]);
           pro[1][3]=2*(b+1)*(1-prob[0])*(1-prob[1]);
           ans[0]=pro[0][1]+pro[0][0]+pro[0][2]+pro[0][3];
           ans[1]=pro[1][1]+pro[1][0]+pro[1][2]+pro[1][3];
           ans[2]=b+2;
           an=(ans[0]>ans[1])?ans[1]:ans[0];
           an=(an>ans[2])?ans[2]:an;
        }
        else
        {

           pro[0][0]=(b-2)*prob[0]*prob[1]*prob[2];
           pro[0][1]=(2*b-1)*prob[0]*(1-prob[2])*prob[1];
           pro[0][2]=(2*b-1)*prob[0]*(1-prob[1])*prob[2];
           pro[0][3]=(2*b-1)*prob[1]*(1-prob[0])*prob[2];
           pro[0][4]=(2*b-1)*prob[0]*(1-prob[1])*(1-prob[2]);
           pro[0][5]=(2*b-1)*prob[1]*(1-prob[0])*(1-prob[2]);
           pro[0][6]=(2*b-1)*prob[2]*(1-prob[1])*(1-prob[0]);
           pro[0][7]=(2*b-1)*(1-prob[0])*(1-prob[1])*(1-prob[2]);

           pro[1][0]=(b)*prob[0]*prob[1]*prob[2];
           pro[1][1]=(b)*prob[0]*(1-prob[2])*prob[1];
           pro[1][2]=(2*b+1)*prob[0]*(1-prob[1])*prob[2];
           pro[1][3]=(2*b+1)*prob[1]*(1-prob[0])*prob[2];
           pro[1][4]=(2*b+1)*prob[0]*(1-prob[1])*(1-prob[2]);
           pro[1][5]=(2*b+1)*prob[1]*(1-prob[0])*(1-prob[2]);
           pro[1][6]=(2*b+1)*prob[2]*(1-prob[1])*(1-prob[0]);
           pro[1][7]=(2*b+1)*(1-prob[0])*(1-prob[1])*(1-prob[2]);

           ans[0]=pro[0][1]+pro[0][0]+pro[0][2]+pro[0][3]+pro[0][4]+pro[0][5]+pro[0][6]+pro[0][7];
           ans[1]=pro[1][1]+pro[1][0]+pro[1][2]+pro[1][3]+pro[1][4]+pro[1][5]+pro[1][6]+pro[1][7];
           ans[2]=b+2;
           an=(ans[0]>ans[1])?ans[1]:ans[0];
           an=(an>ans[2])?ans[2]:an;
        }
        ot<<"Case #"<<j<<": "<<an<<endl;
    }
    return 0;
}
