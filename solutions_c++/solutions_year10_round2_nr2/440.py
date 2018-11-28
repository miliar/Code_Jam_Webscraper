# include <iostream>
# include <vector>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    int index = 1;
    while (index <=test)
    {
          int N;
          long long K,B,T;
          vector <long long> Vi;
          vector <long long> Xi;
          vector <bool> truth;
          long long temp;
          cin>>N>>K>>B>>T;
          for (int i=0;i<N;i++)
          {
              cin>>temp;
              Xi.push_back (temp);
          }
          int count = 0;
          for (int i=0;i<N;i++)
          {
              cin>>temp;
              Vi.push_back (temp);
              Xi[i] = Xi[i] + T * Vi[i];
              if (Xi[i] >= B)
              {
                  count++;
                  truth.push_back (true);
              }
              else
              {
                  truth.push_back (false);
              }                  
          }
          if (count < K)
          {
              cout<<"Case #"<<index<<": IMPOSSIBLE"<<endl;
              index++;
              continue;
          }
          count = 0;
          vector <int> pos;
          for (int i=truth.size () - 1,j = 0;j < K;i--)
          {
              if (truth[i] == true)
              {
                 pos.push_back (i);
                 j++;
              }
          }
          int ans = 0;
          for (int i=0;i<pos.size ();i++)
          {
              ans += (N-i-1) - pos[i];             
          }
          cout<<"Case #"<<index<<": "<<ans<<endl;
          index++;
    }
    return 0;
}               
                                     
              
                        
