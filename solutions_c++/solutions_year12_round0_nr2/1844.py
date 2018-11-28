#include <iostream>
#include <bitset>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

void ProblemB()
{
      ifstream in("B-large.in");
      int T;
      in>>T;
      for(int i=1;i<=T;i++)
      {
            int N,S,p,t;
            in>>N>>S>>p;
            int count=0,nbS=0;
            for(int j=0;j<N;j++)
            {
                  in>>t;
                  bool isAllSurprise=true,solfound=false,hasOneS=false,stop=false,Bhas=false;

                  for(int k=0;k<=10;k++)
                  {
                        for(int l=0;l<=10;l++)
                        {
                              int m=t-k-l;
                              int diff1=abs(k-l),diff2=abs(k-m),diff3=abs(l-m);
                              if(m>=0 && m<=10)
                              {
                                    if((m>=p || k>=p || l>=p) && diff1<=2 && diff2<=2 && diff3 <=2)
                                    {
                                          solfound=true;


                                          if(diff1!=2 && diff2!=2 && diff3!=2)
                                          {
                                                isAllSurprise=false;

                                          }
                                          else
                                          {
                                                hasOneS=true;

                                          }
                                          if(isAllSurprise==false && hasOneS==true)
                                          {
                                                stop=true;
                                                break;
                                          }

                                    }

                                    else if (diff1<=2 && diff2<=2 && diff3<=2){

                                          if(!(diff1!=2 && diff2!=2 && diff3!=2))
                                          {
                                                Bhas=true;

                                          }



                                    }


                              }
                        }
                        if(stop)
                        break;
                  }

                  if(solfound)
                  {
                        if(isAllSurprise)
                        {
                              if(S>0)
                              {
                                    S--;
                                    count++;
                              }


                        }
                        else{
                              count++;
                              if(hasOneS)
                              nbS++;

                        }
                  }
                  else{
                  if(Bhas)
                  nbS++;
                  }

            }

            if(nbS<S)
            count=count-S-nbS;
            if(count<0)
            count=0;
            cout<<"Case #"<<i<<": "<<count<<endl;

      }
      in.close();

}


int main()
{
    ProblemB();
    return 0;
}
