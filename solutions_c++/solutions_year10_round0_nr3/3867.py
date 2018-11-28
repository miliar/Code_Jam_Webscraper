#include<conio.h>
#include<iostream.h>
#include<fstream.h>
#define MAX2 50
#define MAX 100
class queue
{
 public:
long double data[MAX];
 int r,f;
 //rear add
 void init()
 {
 r=f=-1;
 }
 void insert(long double x);
 long double delet();
 int empty()
 {
 if((r==f)&&(f==-1))
 return(1);
 else
 return(0);
 }
};
void queue::insert(long double x)
{
if(r==-1)
f=0;
r++;
r=r%MAX;
       data[r]=x;
}

long double queue::delet()
{
   long  double x=data[f];
    f++;
    f=f%MAX;
    if((r+1)==f)
    r=f=-1;
    return(x);

}
void main()
{
queue q;
q.init();
clrscr();
long double a,b[MAX2][3],i,j,k,grp[MAX2],sum=0,total=0;
fstream abc,out;
abc.open("blow.txt",ios::in);
out.open("output.txt",ios::out);
abc>>a;
for(i=0;i<a;i++)
{
q.init();
total=0;
abc>>b[i][0]>>b[i][1]>>b[i][2];
 for(j=0;j<b[i][2];j++)
 {
 abc>>grp[j];
 q.insert(grp[j]);
 }
 for(k=0;k<b[i][0];k++)
 {
 long double cnt=-1,a[MAX];
 sum=0;
  for(;;)  // 1 ride
  {
   if(sum+q.data[q.f]<=b[i][1]&& !q.empty())
   {
   cnt=cnt+1;
   sum=sum+q.data[q.f];
  //  q.insert(q.delet());
   a[cnt]=q.delet();
   }
   else
   {
     break;
   }
  }// 1 ride
    for(j=0;j<=cnt;j++)
    q.insert(a[j]);
  total=total+sum;

 }//all rides
out<<"Case #"<<i+1<<": "<<total<<"\n";
}
abc.close();
out.close();
getch();
}


