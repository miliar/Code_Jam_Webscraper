#include<iostream.h>
#include<fstream.h>



int rotate(int x,int y)
{
if(x<=99 && y<=99)
{
 y=((y%10)*10)+(y/10);
 if (y==x)
 return 1;
}
else if( x>=100 && y>=100)
{
 y=((y%10)*100)+(y/10);

 if (y==x)
 return 1;
 y=((y%10)*100)+(y/10);
 if (y==x)
 return 1;
}


return 0;

}


int main()
{
ifstream fin;ofstream fout;
fin.open("data.in",ios::in);
fout.open("data.out",ios::out);

int t;
fin>>t;
for(int i=0;i<t;i++)
{
 fout<<"Case #"<<(i+1)<<": ";
 int a,b,count=0;
 fin>>a>>b;

 for(int x=a;x<=b;x++)
 for(int y=a;y<=b;y++)
 { if(x!=y)
 	if (rotate(x,y)==1) count++;
 }
   fout<<count/2<<endl;
}

}