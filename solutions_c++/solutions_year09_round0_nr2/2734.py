#include<iostream.h>
#include<conio.h>
#include<fstream.h>


int et[50][50];  //elevation table
  int st[50][50]; //sink table..nonzero implies sink,0 implies not a sink
  int ist[50][50];   //indirect sink table,contains final sink for each cell
  char result[50][50];
  char db[30];    //drainagebasin symbols array
 int r=2,c=13;


int leastneigh(int i,int j) //returns ht of least neighbour
{
  int h;
  if(i!=0)
     h=et[i-1][j];
  else
    if(j!=0)
     h=et[i][j-1];
    else
     h=et[i][j+1];

  if(j!=0 && h > et[i][j-1])
    h=et[i][j-1];
  if(j+1<c && h > et[i][j+1])
    h=et[i][j+1];
  if(i+1<r && h > et[i+1][j])
    h=et[i+1][j];

   return h;
}

int flow(int i,int j)   //rturns id of cell to which flow occurs from cell[i][j]
{
   int lht=leastneigh(i,j);
   if(i!=0 && et[i-1][j]==lht)  //north
	 return (i-1)*c+j;
   else if(j!=0 && et[i][j-1]==lht) //west
	 return i*c+j-1;
   else if(j+1<c && et[i][j+1]==lht)//east
	 return i*c+j+1;
   else
	return (i+1)*c+j;
}



int sink(int k)
{
  int i=k/c,j=k%c;
  if(st[i][j]!=0)
     return st[i][j];
  else
     return sink(flow(i,j));
}

int notexists(int n)
{
  if(db[n]==0)
   return 1;
  else
  return 0;
}


void main()
{

  ifstream in("input.txt");
  ofstream out("output.txt");

  int n,i,j;
  in>>n;
  for(int x=0;x<n;x++)
  {
  in>>r>>c;
  for(i=0;i<r;i++)
    for(j=0;j<c;j++)
      in>>et[i][j];

  int p=0;
  for(i=0;i<r;i++)
    for(j=0;j<c;j++)
    {
	if((leastneigh(i,j) >=et[i][j]))
	   st[i][j]=++p;
	else
	   st[i][j]=0;
    }

  p=0;
  for(i=0;i<30;i++)
   db[i]=0;
  for(i=0;i<r;i++)
  {
    for(j=0;j<c;j++)
   {
       ist[i][j]=sink(i*c+j);
       if(notexists(ist[i][j]))
	  db[ist[i][j]]=97+(p++);
     //  cout<<ist[i][j]<<" ";
   }
    //cout<<endl;
  }

  out<<"Case #"<<x+1<<": "<<endl;

   for(i=0;i<r;i++)
   {
     for(j=0;j<c;j++)
    {
      result[i][j]=db[ist[i][j]];
      out<<result[i][j]<<" ";
     }
    out<<endl;
   }



}
   cout<<"done";
   getch();
}
