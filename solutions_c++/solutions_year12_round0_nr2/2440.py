#include<fstream.h>
#include<iostream.h>
main()
{
      ifstream f;
      ofstream o;
      int i,j,s,a,b,c,n,ans=0,m;
      f.open("B-large.in");
      o.open("O.txt");
      f>>n;
      for(i=0;i<n;i++)
      {
                      o<<"Case #"<<i+1<<": ";
                      ans=0;
                      f>>a>>b>>c;
                      for(j=0;j<a;j++)
                      {
                                      f>>s;
                                      if(s/3>=c)
                                                ans++;
                                      else
                                      {
                                          if(s%3==0 && b!=0 && s/3+1>=c && s!=0)
                                          {
                                                    b--;
                                                    ans++;
                                          }
                                          if(s%3==1 && s/3+1>=c)
                                                    ans++;
                                          if(s%3==2)
                                          {
                                                    if(s/3+1>=c)
                                                                ans++;
                                                    else if(b!=0 && s/3+2>=c)
                                                    {
                                                         ans++;
                                                         b--;
                                                    }
                                          }
                                      }
                      }
                      o<<ans<<endl;                                                             
      }
      f.close();
      o.close();
}
