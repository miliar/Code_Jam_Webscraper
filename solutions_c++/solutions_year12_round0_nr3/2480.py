#include<fstream.h>
#include<iostream.h>
#include<conio.h>
#include<math.h>
main()
{
      ifstream f;
      ofstream o;
      long i,j,ctr=0,c,s,a,b,n,k,ans=0,m;
      double p;
      f.open("C-large.in");
      o.open("O.txt");
      f>>n;
      for(i=0;i<n;i++)
      {
                      o<<"Case #"<<i+1<<": ";
                      ans=0;
                      ctr=0;
                      f>>a>>b;
                      m=a;
                      while(m!=0)
                      {
                                 ctr++;
                                 m=m/10;
                      }
                      p=(pow(10,ctr-1));
                      for(j=a;j<=b;j++)
                      {
                                       s=j;
                                       long q=0;
                                       c=1;
                                       while(c<ctr && s!=q)
                                       {
                                                   q=j;
                                                   c++;
                                                   k=(s%10);
                                                   
                                                   s=s/10+k*p;
                                                   if(s>j && s<=b)
                                                          ans++;
                                       }
                      }
                      o<<ans<<endl;                                                            
      }
      f.close();
      o.close();
}
