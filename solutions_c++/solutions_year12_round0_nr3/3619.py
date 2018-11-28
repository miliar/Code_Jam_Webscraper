#include<iostream>
#include<fstream>



int rot(int x,int y)
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
using namespace std;
ifstream fi;ofstream fo;
fi.open("data.in",ios::in);
fo.open("data.out",ios::out);

int test;
fi>>test;
for(int k=0;k<test;k++)
{
 fo<<"Case #"<<(k+1)<<": ";
 int a,b,total=0;
 fi>>a>>b;

 for(int x=a;x<=b;x++)
 for(int y=a;y<=b;y++)
 { if(x!=y)
 	if (rot(x,y)==1) total++;
 }
   fo<<total/2<<endl;
}

}
