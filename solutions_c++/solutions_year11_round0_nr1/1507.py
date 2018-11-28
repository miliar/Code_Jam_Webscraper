#include <iostream>
#include<math.h>
#include<cstdlib>
#include<fstream>
#include<cstdio>
using namespace std;
int n_case;

int main()
{
    ofstream cout("out.txt");
    freopen("in.txt","r",stdin);
    char color;
    int id;
    int n_b;
    int o_id;
    int b_id;
    int time_o;
    int time_b;
    char flag;
    cin>>n_case;
    for(int t=0;t<n_case;t++)
    {
        int total=0;
        flag='O';
        time_o=0;
        time_b=0;
        o_id=1;
        b_id=1;
        cin>>n_b;
        for(int i=0;i<n_b;i++)
        {
            cin>>color>>id;
            if(color=='O'&&flag=='O')
             {
                 int tmp=abs(id-o_id)+1;
                 time_o+=tmp;
                 total+=tmp;
                 o_id=id;
             }
             else  if(color=='O'&&flag=='B')
             {
                   if(time_b>=abs(id-o_id))
                   {
                       time_o=1;
                       total+=1;
                   }
                   else {
                       time_o= abs(id-o_id)-time_b+1;
                       total+=time_o;
                   }
                flag='O';
                o_id=id;
             }
             else if(color=='B'&&flag=='B')
             {
                  int tmp=abs(id-b_id)+1;
                 time_b+=tmp;
                 total+=tmp;
                 b_id=id;
             }
             else if(color=='B'&&flag=='O')
             {
                 if(time_o>=abs(id-b_id))
                   {
                       time_b=1;
                       total+=1;
                   }
                   else {
                       time_b= abs(id-b_id)-time_o+1;
                       total+=time_b;
                   }
                flag='B';
                b_id=id;
             }
        }
        cout<<"Case #"<<t+1<<": "<<total<<endl;

    }

}





