#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    int T,R,k,N,Rbak;
    int i,j,x;
    int E,s,total,repeat,temp;
    vector <int>g,r,e;
    cin>>T;
    for(i=0;i<T;i++)
    {
                    cin>>R>>k>>N;
                    g.clear();
                    total =0;
                    for(j=0;j<N;j++)
                    {
                                    cin>>x;
                                    g.push_back(x);
                                    total+=x;
                                    e.push_back(-1);
                                    r.push_back(-1);
                    }
                    if(total<k)
                    {
                               cout<<"Case #"<<i+1<<": "<<R*total<<endl;
                               continue;
                    }
                    j=0;
                    E=0;
                    repeat = 0;
                    Rbak =R;
                    while(R>0)
                    {
                              s=0;
                              //system("PAUSE");
                              while(s+g[j] <= k)
                              {
                                           s = s+g[j++];
                                           if(j==N)
                                                   j=0;
                              }
                              E+=s;
                              R--;
                              if(j==0)
                              {
                                  if((Rbak - R)>R && !repeat)
                                  {
                                                temp = R/(Rbak - R);
                                                E = E + (E* temp);
                                                R-=(temp*(Rbak - R));
                                                repeat = 1;
                                  }
                                  else
                                  {
                                      e[k-1] = E;
                                      r[k-1] = R;
                                  }
                              }
                              else
                              {
                                  if(e[j-1]!=-1 && (r[j-1]-R)>R && !repeat)
                                  {
                                                temp = R/(r[j-1]-R);
                                                E = E + ((E - e[j-1])* temp);
                                                R-=(temp*(r[j-1]-R));
                                                repeat = 1;
                                  }
                                  else
                                  {
                                                e[j-1] = E;
                                                r[j-1] = R;
                                  }
                              }
                    }
                    cout<<"Case #"<<i+1<<": "<<E<<endl;
                    //system("PAUSE");
    }
    
}
