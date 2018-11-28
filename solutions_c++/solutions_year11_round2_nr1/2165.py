#include <iostream>
#include <fstream>
#include <iomanip>
//#include <sstream>
/*
#include <cmath>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <vector>
*/

using namespace std;
/*
typedef  vector<int,int> pvec;
typedef vector<int,int>::iterator pveci;
*/
/*
typedef  map<int,int> pmap;
typedef map<int,int>::iterator pmapi;
*/
/*
typedef  list<int,int> plist;
typedef  list<int,int>::iterator plisti;
*/
/*
typedef  set<int,int> pset;
typedef set<int,int>::iterator pseti;
*/

/*
typedef  multiset<int,int> pmultiset;
typedef  multiset<int,int>::iterator pmultiseti;
*/
/*
typedef  multimap<int,int> pmap;
typedef  multimap<int,int>::iterator pmapi;
*/
int main()
{
      ifstream file("A-large.in");
      int T=0,N=0;
      file>>T;
      for(int i=1;i<=T;i++)
      {
            file>>N;
            char gain[N][N];

            double num[N],den[N],sous[N][N];
            double WP[N],OWP[N],OOWP[N];
            for(int l=0;l<N;l++)
            {
                  for(int k=0;k<N;k++)
                  {
                        sous[l][k]=0;

                  }
                  num[l]=0.;
                  den[l]=0.;
                  WP[l]=0.;
                  OWP[l]=0;
                  OOWP[l]=0.;

            }


            for(int j=0;j<N;j++)
            {
                  for(int k=0;k<N;k++)
                  {
                        file>>gain[j][k];

                        if(gain[j][k]=='1')
                        {
                              num[j]+=1;
                              den[j]+=1;


                        }
                        if(gain[j][k]=='0')
                        {
                              den[j]+=1;
                              sous[j][k]=1;

                        }

                  }
                  if(den[j]>0)
                  WP[j]=num[j]/den[j];
                  else
                  WP[j]=0;
            }

            for(int l=0;l<N;l++)
            {
                  for(int k=0;k<N;k++)
                  {
                        if(gain[l][k]!='.' && den[k]>1 && num[k]>sous[l][k])
                        OWP[l]+=(num[k]-sous[l][k])/(den[k]-1);
                        else
                        OWP[l]+=0;

                  }
                  if(den[l]>0)
                  OWP[l]=OWP[l]/den[l];
                  else
                  OWP[l]=0;


            }
            cout<<"Case #"<<i<<":"<<endl;

            for(int l=0;l<N;l++)
            {
                  for(int k=0;k<N;k++)
                  {
                        if(gain[l][k]!='.')
                        {
                              OOWP[l]+=OWP[k];

                        }


                  }
                  double res=0;
                  if(den[l]>0)
                  res=0.25*WP[l]+0.5*OWP[l]+0.25*OOWP[l]/den[l];
                  else
                  res=0.25*WP[l]+0.5*OWP[l];

                        cout<<setprecision(10)<<res<<endl;

            }

      }
      file.close();

    return 0;
}

