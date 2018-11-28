#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

struct command;
int max(int a, int b)
{return (a>b)?a:b;}
int min(int a, int b)
{return (a<b)?a:b;}
int get_dist(int a, int b)
{return max(a,b)-min(a,b);}


int Opos,Bpos,B_time,O_time;
const int PRESS=1;

int wait_cost(char me)
{
        if(me=='B')
        {
                if(O_time>B_time)
                {
                        return O_time-B_time;
                }
                else
                        return 0;

        }
        else
        {
                if(B_time>O_time)
                {
                        return B_time-O_time;
                }
                else
                        return 0;

        }
}

int main()
{
        int numCases,lines;

        cin>>numCases>>ws;
        int N,num;
        char C;

        for(int k=1;k<=numCases;k++)
        {
                Opos=1;
                Bpos=1;
                B_time=0;
                O_time=0;
                cin>>N;

                for(int i=0;i<N;i++)
                {
                        cin>>C>>num;
                        if(C=='B')
                        {
                                if(wait_cost('B')>get_dist(Bpos,num))
                                {
                                        B_time+=PRESS+wait_cost('B');
                                }
                                else
                                {
                                        B_time+=PRESS+get_dist(Bpos,num);
                                }
                                Bpos=num;
                        }
                        else
                        {
                                if(wait_cost('O')>get_dist(Opos,num))
                                {
                                        O_time+=PRESS+wait_cost('O');
                                }
                                else
                                {
                                        O_time+=PRESS+get_dist(Opos,num);
                                }
                                Opos=num;
                        }

                }
                cin>>ws;


                cout<<"Case #"<<k<<": "<<max(B_time,O_time)<<endl;
        }

return 0;
}
