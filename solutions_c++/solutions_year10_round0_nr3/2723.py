#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

 ifstream in;
 ofstream out;//,out1;

typedef struct ParkPoint
{unsigned next;
unsigned pre;
unsigned ID;
unsigned value;
unsigned time;
double profit;
double sum;
}Point,*Plink;

Point p[1001]={0};
unsigned T,R,k,N;


void getpoint()
{unsigned i;
 for(i=0;i<N;i++)
 {in>>p[i].value;
  p[i].next=-1;
  p[i].pre=-1;
  p[i].ID=i;
  p[i].profit=0;
  p[i].time=0;
  p[i].sum=0;
 // out1<<p[i].value<<" ";
 }
// out1<<endl;
}

double run()
{unsigned step=0,i,state=0;
 double sum=0,popu=0;
 unsigned pend,pbeg,num;
 
 while(p[(state)%N].next==-1&&R>0)
 {popu=0;
  p[state].time=step;
  for(i=0;popu<=k&&i<=N;i++)
  {popu+=p[(state+i)%N].value;
  }
  i--;
  popu-=p[(state+i)%N].value;
  p[state].sum=sum;
  p[state].profit=popu;
  p[state].next=(state+i)%N;
  p[(state+i)%N].pre=state;
  sum+=popu;
  R--;
  state=p[state].next;
  step++;
 }

 pbeg=state;pend=p[state].pre;
 num=floor(R/(p[pend].time-p[pbeg].time+1));
 sum+=(p[pend].sum-p[pbeg].sum+p[pend].profit)*num;
 R-=unsigned(num)*(p[pend].time-p[pbeg].time+1);
 
 while(R>0)
 {popu=0;
  p[state].time=step;
  for(i=0;popu<=k&&i<=N;i++)
  {popu+=p[(state+i)%N].value;
  }
  i--;
   popu-=p[(state+i)%N].value;
  p[state].sum=sum;
  p[state].profit=popu;
  p[state].next=(state+i)%N;
  p[(state+i)%N].pre=state;
  sum+=popu;
  R--;
  state=p[state].next;
  step++;
 }
return sum;
}



int main()
{unsigned i;

 in.open("C-small-attempt5.in");
 out.open("output.txt");
 //out1.open("question.txt");
 in>>T;
// out1<<T<<endl;
 for(i=1;i<=T;i++)
 {in>>R>>k>>N;
  //out1<<R<<" "<<k<<" "<<N<<endl;
  getpoint();
  out<<"Case #"<<i<<": "<<run()<<endl;
 }
 return 0;
}