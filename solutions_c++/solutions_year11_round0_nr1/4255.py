#include<iostream>
#include<queue>
using namespace std;
int N,T;
char i1;
int i2;
struct data
{
int pos;
int index;

};

queue<data*>O,B;
int di,dj;
bool pu;
int main()
{
cin>>T;
for(int i=0;i<T;i++)
{


cin>>N;


for(int i=0;i<N;i++)
{
 cin>>i1>>i2;
 data* temp= new data();
 temp->pos=i2;
 temp->index=i;

 if(i1=='O')
 {
   O.push(temp);

 }
 else
 {
   B.push(temp);


 }
}
di=dj=1;
int t=0;
for(int i=1,j=1,index=0;!O.empty() || !B.empty();i+=di,j+=dj,t++)
{
  pu=false;
  if(!O.empty() && O.front()->index ==index && O.front()->pos==i)
  {
    delete O.front();
    O.pop();
    index++;
    i-=di;
    pu=true;

  }
  else if(!O.empty() && O.front()->pos==i)
  {
    di=0;

  }
  else if(!O.empty() && O.front()->pos<i)
  {
    di=-1;
  }
  else if(!O.empty() && O.front()->pos>i)
  {
    di=1;
  }



  if(!B.empty() && B.front()->index ==index && B.front()->pos==j && !pu)
  {
    delete B.front();
    B.pop();
    index++;
    j-=dj;
  }
  else if(!B.empty() &&B.front()->pos==j)
  {
    dj=0;
  }
  else if(!B.empty() && B.front()->pos<j)
  {
    dj=-1;
  }
  else if(!B.empty() && B.front()->pos>j)
  {
    dj=1;
  }

}

cout<<"Case #"<<i+1<<": "<<t<<endl;




}

return 0;
}
