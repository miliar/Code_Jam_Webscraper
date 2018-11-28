#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    vector <int>v1,v2;
    int t,n,c,num=0, count=0;
    cin>>t;
    while(t--)
    {
              cin>>n;
              while(n--)
              {
                        cin>>c;
                        v1.push_back(c);
                        v2.push_back(c);
                        }
                        num++;
                        sort(v1.begin(),v1.end());
                        for(int i=0;i<v1.size();i++)
                        {
                                if(v1[i]!=v2[i])
                                count++;
                                }
                                cout<<"Case #"<<num<<": "<<count<<".000000";
                                count=0;
                        cout<<"\n";
                        v1.clear();
                        v2.clear();
              }
    return 0;
    }
