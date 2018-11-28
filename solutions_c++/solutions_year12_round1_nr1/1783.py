#include<iostream>
#include<fstream>

using namespace std;
int main()
{
    float nan[7][9]={0};
    float dev[14]={0};
    float ch[7],an;
    int i,j,k;
    ofstream ot;   ot.open("output1a.txt");
    ifstream in ("input1a.txt");       in>>k;
    int test1,l;
    for(j=1;j<=k;j++)
    {
        in>>test1>>l;
        i=0;
        while(i<test1)
        in>>dev[i++];
        if(test1==1)
        {
           nan[0][0]=l*dev[0];  nan[0][1]=(2*l+1)*(1-dev[0]);
           nan[1][1]=(l+2)*(1-dev[0]);    nan[1][0]=(l+2)*dev[0];
           nan[2][1]=(l+2)*(1-dev[0]);     nan[2][0]=(l+2)*dev[0];
           ch[0]=nan[0][1]+nan[0][0];
           ch[1]=nan[1][1]+nan[1][0];
           ch[2]=nan[2][1]+nan[2][0];
           if(ch[0]>ch[1])
           an=ch[1];
           else
           an=ch[0];
           if(an>ch[2])
           an=ch[2];
           else   an=an;
        }
        else if(test1==2)
        {
           nan[0][0]=(l-1)*dev[0]*dev[1];    nan[1][0]=(l+1)*dev[0]*dev[1];
           nan[0][1]=(2*l)*dev[0]*(1-dev[1]);     nan[1][1]=(l+1)*dev[0]*(1-dev[1]);
           nan[0][2]=(2*l)*dev[1]*(1-dev[0]);      nan[1][2]=2*(l+1)*dev[1]*(1-dev[0]);
           nan[0][3]=(2*l)*(1-dev[0])*(1-dev[1]);    nan[1][3]=2*(l+1)*(1-dev[0])*(1-dev[1]);
           ch[0]=nan[0][1]+nan[0][0]+nan[0][2]+nan[0][3];
           ch[1]=nan[1][1]+nan[1][0]+nan[1][2]+nan[1][3];     ch[2]=l+2;
           if(ch[0]>ch[1])   an=ch[1];
           else an=ch[0];
           if(an>ch[2])    an=ch[2];
           else an=an;
        }
        else
        {

           nan[0][0]=(l-2)*dev[0]*dev[1]*dev[2];     nan[1][0]=(l)*dev[0]*dev[1]*dev[2];
           nan[0][1]=(2*l-1)*dev[0]*(1-dev[2])*dev[1];    nan[1][1]=(l)*dev[0]*(1-dev[2])*dev[1];
           nan[0][2]=(2*l-1)*dev[0]*(1-dev[1])*dev[2];    nan[1][2]=(2*l+1)*dev[0]*(1-dev[1])*dev[2];
           nan[0][3]=(2*l-1)*dev[1]*(1-dev[0])*dev[2];      nan[1][3]=(2*l+1)*dev[1]*(1-dev[0])*dev[2];
           nan[0][4]=(2*l-1)*dev[0]*(1-dev[1])*(1-dev[2]);   nan[1][4]=(2*l+1)*dev[0]*(1-dev[1])*(1-dev[2]);
           nan[0][5]=(2*l-1)*dev[1]*(1-dev[0])*(1-dev[2]);    nan[1][5]=(2*l+1)*dev[1]*(1-dev[0])*(1-dev[2]);
           nan[0][6]=(2*l-1)*dev[2]*(1-dev[1])*(1-dev[0]);    nan[1][6]=(2*l+1)*dev[2]*(1-dev[1])*(1-dev[0]);
           nan[0][7]=(2*l-1)*(1-dev[0])*(1-dev[1])*(1-dev[2]);  nan[1][7]=(2*l+1)*(1-dev[0])*(1-dev[1])*(1-dev[2]);
           ch[0]=nan[0][1]+nan[0][0]+nan[0][2]+nan[0][3]+nan[0][4]+nan[0][5]+nan[0][6]+nan[0][7];
           ch[1]=nan[1][1]+nan[1][0]+nan[1][2]+nan[1][3]+nan[1][4]+nan[1][5]+nan[1][6]+nan[1][7];
           ch[2]=l+2;
           if(ch[0]>ch[1])   an=ch[1];
           else an=ch[0];
           if(an>ch[2])  an=ch[2];
           else  an=an;
        }
        ot<<"Case #"<<j<<": "<<an<<endl;
    }
    return 0;
}

