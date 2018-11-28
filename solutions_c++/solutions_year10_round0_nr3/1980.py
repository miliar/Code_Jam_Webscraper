# include <iostream>
# include <vector>

using namespace std;

bool array [1005];
int sum [1005];
int next [1005];
int main ()
{
    int test;
    cin>>test;
    int i=1;
    while (i<=test)
    {
          int R,k,g;
          cin>>R>>k>>g;
          vector <int> group;
          for (int j=0;j<g;j++)
          {
              group.push_back (0);
              cin>>group[j];
              array [j] = false;
              sum[j]=0;
              next[j]=-1;
          }
          for (int j=0;j<g;j++)
          {
              int temp=j;
              while ((sum[j]+group[temp]) <= k)
              {
                    sum[j]+=(group[temp]);
                    temp = (temp + 1)%g;
                    if (temp == j)
                       break;
              }
              next[j]=temp;
          }
          int start = 0;
          vector <int> circle;
          while (array[start]!= true)
          {
              circle.push_back (start);
              array[start] = true;
              start = next[start];
          }
          long long ans = 0LL;
          if (circle.size () >= R)
          {
             for (int j=0;j<R;j++)
             {
                 ans += sum[circle[j]];
             }
             cout<<"Case #"<<i<<": "<<ans<<endl;
          }
          else
          {
             for (int j=0;j<circle.size ();j++)
             {
                 ans += sum[circle[j]];
             }                        
             int index = -1;
             for (int j=0;j<circle.size ();j++)
             {
                 if (circle[j] == start)
                 {
                     index = j;
                     break;
                 }
             }
             long long tempans = 0LL;
             for (int j=index;j<circle.size ();j++)
             {
                 tempans += sum[circle[j]];
             }
             ans += ((R - circle.size ())/(circle.size () - index))* tempans;
             int tempindex = (R - circle.size ())%(circle.size () - index);
             if (tempindex != 0)
             {
                 for (int j=0;j<tempindex;j++)
                 {
                     ans += (sum[circle[index+j]]);
                 }
             }
             cout<<"Case #"<<i<<": "<<ans<<endl;
          }
          i++;
    }
    return 0;
}                      
                                
