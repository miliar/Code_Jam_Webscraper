
# include <iostream>
# include <vector>

# define  p push_back 

using namespace std;

int main()
{
    int t,cnt = 1;
    cin>>t;
    while(t--)
    {
              int n,i,j,tp,sm;
              vector <int> c;  
              cin>>n;
              tp = 0;
              for(i=0;i<n;i++)
              {
                  cin>>j;
                  c.p(j);
                  tp ^= j;                
              }        
              if(tp != 0)
                 cout<<"Case #"<<cnt++<<": NO\n";
              else
              {
                  sort(c.begin(),c.begin()+n);
                  sm = 0;
                  for(i=1;i<n;i++)
                    sm += c[i];
                  cout<<"Case #"<<cnt++<<": "<<sm<<endl;   
              }
    }
}
