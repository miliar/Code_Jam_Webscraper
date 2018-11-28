# include <iostream>
# include <vector>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    int count=1;
    while (count<=test)
    {
          int p;
          cin>>p;
          vector < vector <int> > ansarray;
          ansarray.clear ();
          ansarray.resize(p);
          int value = 1<<p;
          for (int i=0;i<ansarray.size();i++)
          {
              ansarray[i].resize(value/2);
              value = value/2;
          }    
          vector <int> most;
          for (int i=0;i<(1<<p);i++)
          {
              most.push_back (0);
              cin>>most[i];
          }
          for (int i=0;i< (1<<p) -1;i++)
          {
              int temp;
              cin>>temp;
          }
          for (int i=0;i<most.size();i++)
          {
              for (int j=most[i];j<p;j++)
              {
                  ansarray[j][i/(1 << (j+1))] = 1;
              }
          }
          int ans = 0;
          for (int i=0;i<ansarray.size ();i++)
          {
              for (int j=0;j<ansarray[i].size();j++)
              {
                  if (ansarray[i][j] == 1)
                  {
                       ans++;
                  }
              }
          }                                     
          cout<<"Case #"<<count<<": "<<ans<<endl; 
          count++;
    }
    return 0;
}        
              
