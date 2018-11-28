#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>

using namespace std;

int main()
{
    int t;
    
    ifstream fin("input.txt");
    ofstream fout("ans.txt");
    if(!fin)
    {
            cout<<"Wrong Location";
            cin>>t;
            exit(1);
    }
    fin>>t;
    
    int m=t;
    while(t--)
    {
               long long int n,A,B,C,D,x0,y0,M;
               fin>>n>>A>>B>>C>>D>>x0>>y0>>M;
               vector<int> X,Y;
               long long int tempX = x0;
               long long int tempY = y0;
               X.push_back(tempX);
               Y.push_back(tempY);
              // cout<<tempX<<" "<<tempY<<" ";  
               for(long long int i=0;i<n-1;i++)
               {
                  tempX = (((A%M)*(tempX%M))%M+B%M)%M;
                  tempY = (((C%M)*(tempY%M))%M+D%M)%M;
                  X.push_back(tempX);
                  Y.push_back(tempY);
                //  cout<<tempX<<" "<<tempY<<" ";
               }
               int ans=0;
               for(long long int i=0;i<X.size();i++)
               {
                       for(long long int j=i+1;j<X.size();j++)
                       {
                               for(long long int k=j+1;k<X.size();k++)
                               {
                                       long long int x1=X[i]+X[j]+X[k];
                                       long long int y1=Y[i]+Y[j]+Y[k];
                                       if((x1%3!=0)||(y1%3!=0))
                                         continue;
                                         else
                                         ans++;/*{
                                       x1/=3;
                                       y1/=3;
                                       for(int l=0;l<X.size();l++)
                                          if(X[l]==x1&&Y[l]==y1)
                                            ans++;}*/
                                            }
                                            }
                                            }
                                            fout<<"Case #"<<m-t<<": "<<ans<<"\n";
 
               }
cin>>t;
}                  

               
               
               
               
               
               
               
               
               
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
