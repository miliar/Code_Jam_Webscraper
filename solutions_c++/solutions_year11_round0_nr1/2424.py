#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
//ifstream fin("BOTTRUST.IN");

struct button
{
    char type;   
    int pos;      
};

void process(int t)
{
    fout<<"Case #"<<t<<": ";
    int N;
    fin>>N;
    button B[101];
    for(int i=1;i<=N;i++)
       fin>>B[i].type>>B[i].pos;
    int b=1,o=1;
    int time = 0;
    for(int i=1;i<=N;i++)
    {
       char type = B[i].type;
       int pos = B[i].pos;

       if(type == 'O')
       {
           int m = abs(pos-o);
           o = pos;
           time += m+1;
           int nb = -1;
           for(int j=i+1;j<=N;j++)
               if(B[j].type=='B')
               {
                  nb = B[j].pos;          
                  break;
               }
           if(nb!=-1)
           {
               if(nb<b)
                  b -= min(m+1,b-nb);
               else
                  b += min(m+1,nb-b);
           }
          
       }
       else
       {
           int m = abs(pos-b);
           b = pos;
           time += m+1;
           int no = -1;
           for(int j=i+1;j<=N;j++)
               if(B[j].type=='O')
               {
                  no = B[j].pos;          
                  break;
               }
           if(no!=-1)
           {
               if(no<o)
                  o -= min(m+1,o-no);
               else
                  o += min(m+1,no-o);
           }
       }
    }
    fout<<time<<endl;
}

int main()
{
    int T;
    fin>>T;
    for(int i=1;i<=T;i++)
        process(i);    
    //system("pause");
    return 0;
}
