#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

int n;
const int cmax=100+10;
bool type[cmax]={0};//false for orange, true for blue
int pos[cmax];

int now=0,po=1,pb=1;
//now is the aim right now

char read()
{
   char chr;
   while((chr!='O')&&(chr!='B')) fin>>chr;
   return chr;
}

void moveo()
{
     int apo; //aim for O and aim for B
     int i=now;
     while((i<n)&&(type[i])) i++;
     apo=pos[i];
     if(po<apo) po++; 
       else if(po>apo) po--;
}
void moveb()
{
     int apb;
     int i=now;
     while((i<n)&&(!type[i])) i++;
     apb=pos[i];
     if(pb<apb) pb++;
       else if(pb>apb) pb--;
}
int main()
{
    int T;
    fin>>T;
    for(int i=0;i<T;i++)
    {
       fin>>n;
       for(int j=0;j<n;j++)
       {
          type[j]=(read()=='B');
          fin>>pos[j];
       }
       int tm=0;
       now=0;po=1;pb=1;
       while(now<n)
       {
          tm++;
          if(type[now])
          {
             if(pos[now]==pb)
             {
               moveo();
               now++;
             }else
             {
               moveo();
               moveb();
             }
          }else
          {
             if(pos[now]==po)
             {
                moveb();
                now++;
             }else
             {
                moveo();
                moveb();
             }
          }
       }
       fout<<"Case #"<<i+1<<": "<<tm<<endl;
    }
}
