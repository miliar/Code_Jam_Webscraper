# include <iostream>
# include<algorithm>
# include<vector> 

using namespace std;

int main ()
{
    int test;
    cin>>test;
    int j=1;
    while (test--)
    {
          int P,Q;
          vector <int> values;
          bool flag [101];
          //memset (flag,0,sizeof (flag));
          cin>>P>>Q;
          int finalans=-1;
          for (int i=0;i<Q;i++)
          {
              int num;
              cin>>num;
              values.push_back (num);
          }   
          sort (values.begin(),values.end ());
          do
          {
              memset (flag,0,sizeof (flag));
              int ans=0;
              for (int i=0;i<values.size ();i++)
              {
                  flag[values[i]]=true;
                  for (int k=values[i]-1;k>0;k--)
                  {
                      if (flag[k]==true)
                      {
                         break;
                      }
                      ans++;
                  }
                  for (int k=values[i]+1;k<=P;k++)
                  {
                      if (flag[k]==true)
                         break;
                      ans++;          
                  }
              }
              if (finalans==-1)
              {
                  finalans=ans;
              }
              else
              {
                  if (ans<finalans)
                  {
                      finalans=ans;
                  }
              }                                                 
          }while (next_permutation (values.begin (),values.end ()));
          cout<<"Case #"<<j<<": "<<finalans<<endl;
          j++;
    }     
    return 0;
}          
                     
