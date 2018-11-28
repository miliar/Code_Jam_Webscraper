#include <iostream>
#include <fstream>
using namespace std;

enum ROBOTSTATE { WALK, PRESS, WAIT, FINISH };

struct Robot
{
    int state;
    int pos;
    int target;
};
struct OrderList
{
    int current;
    int* who;
    int* where;
    int size;
};
OrderList* readSeq(ifstream & ifile)
{
          OrderList*  seq = new OrderList;
          ifile>> seq->size;
          seq->who = new int[seq->size];
          seq->where = new int[seq->size];
          int i;
          char c;
          for(i=0; i<seq->size; i++)
          {
                 ifile>>c; if ( c == 'O') seq->who[i] = 0; else seq->who[i] = 1;
                 ifile>> seq->where[i];
          }
          return seq;
}
int getNextTraget(int r,int ctime,OrderList* seq)
{
    int order;
    for(order = ctime; order < seq->size; order++)
    {
              if(seq->who[order] == r)
              return seq->where[order];
              }
              return -1;
}
int main()
{
     ifstream ifile; ifile.open("A-large.in", ios::in);
     ofstream ofile; ofile.open("output.txt",ios::out);
    Robot bot[2]; 
    int casesNum;
    ifile>>casesNum;
    int i;
    for(i=1; i<=casesNum; i++)
    {
        OrderList* seq = readSeq(ifile);
        seq->current = 0;
        int time = 0;
        int finished = 0;
        bot[0].pos = 1;           bot[1].pos = 1;
        bot[0].state = WALK;      bot[1].state = WALK;
        bot[0].target = getNextTraget(0,0,seq);
        bot[1].target = getNextTraget(1,0,seq);
        while(!finished)
        {
            if(seq->current == seq->size)
            {
               finished = 1;
               ofile<<"Case #"<<i<<": "<<time<<endl;
            } 
            int r;
            for(r = 0; r<2; r++)
            {
                if(bot[r].pos != bot[r].target){
                      bot[r].state = WALK;
                      bot[r].pos = bot[r].pos + (bot[r].target - bot[r].pos)/ abs(bot[r].target - bot[r].pos);
                }
                else
                {
                  if(seq->who[seq->current] == r)
                  {
                      bot[r].state = PRESS;
                      
                      bot[r].target = getNextTraget(r,seq->current+1,seq);
                  }
                  else{ bot[r].state = WAIT;}
                }
            }   
            if(bot[0].state == PRESS || bot[1].state==PRESS) seq->current++;                   
        time ++;
        }
        delete seq->where;
        delete seq->who;
        delete seq;
    }
    return 0;
}
