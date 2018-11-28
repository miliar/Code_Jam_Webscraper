#include <iostream>
#include <string>
using namespace std;


int digits(int);

int main ()
{
  int i,j,k,t,m,n,d1,d2,c=0,total,x1,x2;
  string s1="",s2="";

  cin >> t;
  total = t;

  while(t--)
  {
   cin>>m>>n;

   for(i=m;i<=n;i++)
   {
     for(j=i+1;j<=n;j++)
     {
         d1 = digits(i);
         d2 = digits(j);

        // if(d1!=d2 || d1==1 || d2==1)
        // continue;


          if(d2==2)
          {
            int z = (j%10)*10 + j/10;
           // cout<<z<<" "<<i<<endl;
            if(z==i)
            c++;

          }
            else if(d2==3)
          {
            //int y = (j%100 - j%10)/10;
            //int z = (j%10)*100 + y*10 + j/100;
           // cout<<" "<<z<<" "<<i<<endl;


               x1 = i/10;
               x1=x1%10;
               x2 = j/10;
               x2=x2%10;

            if( (j%10) == (i/100) && (j/100)==x1 && (i%10)==x2 )
            c++;

            int z = x2*100 + (j%10)*10 + j/100;

           // cout<<z<<"---- "<<i<<endl;
            if(z==i)
            c++;
          }



      }
   }
   cout<<"Case #"<<total-t<<": "<<c<<endl;
   c=0;
  }
 return 0;
}

   int digits ( int i)
  {

    int d1;

        if(i/10 == 0)
         d1 = 1;

          else if(i/100 > 0)
           d1 = 3;

             else
              d1=2;

              return d1;
   }

