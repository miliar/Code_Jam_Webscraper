#include<algorithm>
#include<cstdio>
#include<iostream>
#include<map>
#include<stack>
#include<string>
#include<vector>
#include<queue>
using namespace std;
int f(int x,int b)
{
    int res=0;
    while(x)
    {
     res+=((x%b)*(x%b));
     x/=b;
    }    
    return res;
}

    int t[11][100000];
int main()
{

    for(int k=2;k<=10;k++)
    {
            for(int i=1;i<100000;i++)
                    t[k][i]=0;
            t[k][1]=-1;
            for(int i=2;i<100000;i++)
            {
                    vector<int> V;
                    int j=i;
                    while(!t[k][j])
                    {
                                  t[k][j]=1;
                                  V.push_back(j);
                                  j=f(j,k);
                                  
                                  //cout << "\n "<< j << " "<<k;
                    }
                    if(t[k][j]==-1) 
                                    for(int it=0;it<V.size();it++)
                                            t[k][V[it]]=-1;
                    
                    
                    }
    }
    int T;
    cin >> T;
    for(int te=0;te<=T;te++)
    {
     vector<int> V;
     string str;
     getline(cin, str);
     if( te ==0)  continue;
     for(int i=0;i<str.size();i++)
     
             if(str[i]=='1')
                          {V.push_back(10);
                           i++;
                           } else 
                                        if(str[i]!=' ')
                                                     V.push_back(str[i]-'0');
     
     
            for(int i=2;i<100000;i++)
            {
                    
                    
                    int res=0;
                        for(int k=0;k<V.size();k++)
                              res+=t[V[k]][i];
                              if( res==-V.size())
                              {
                                cout <<"Case #"<<te <<": "<<i<< endl;
                                break;
                                }
            }
    }
    return 0;
}
