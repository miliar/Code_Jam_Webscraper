#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <cstdlib>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <stack>
#include <set>
#include <functional>
#include <map>
#define eps 1e-3
using namespace std;


int main ()
{
    freopen ("B-small-attempt0.in","r",stdin);
    freopen ("out.txt","w",stdout);
    
    int T;
    while (cin>>T)
    {
        for (int Case = 1; Case<=T; Case++)
        {
            int C,D,N;
            stack <char> res;
            cin>>C;
            vector <string> Combine(C);
            for (int i=0; i<C; i++)
                cin>>Combine[i];
            
            cin>>D;
            vector <string> Clear(D);
            for (int i=0; i<D; i++)
                cin>>Clear[i];
            
            cin>>N;
            
            for (int i=0; i<N; i++)
            {
                char ele;
                cin>>ele;
                res.push(ele);
                char ele1,ele2;
                if (res.size()>=2)
                {
                    ele1=res.top();
                    res.pop();
                    ele2=res.top();
                    res.pop();
                    bool Com = false;
                    bool Clea = false;
                    for (int j=0; j<C; j++)
                    {
                        if ( ( ele1==Combine[j][0] && ele2==Combine[j][1]) || ( ele2==Combine[j][0] && ele1==Combine[j][1]))
                        {
                            res.push(Combine[j][2]);
                            Com = true;
                            break;    
                        }    
                    }    
                    
                    if (Com == false)
                    {
                        res.push(ele2);
                        res.push(ele1);
                        
                        stack <char> temp;
                        temp = res;
                        for (int j=0; j<D && Clea ==false; j++)
                        {
                            if (temp.top()==Clear[j][0])
                            {
                                while (!temp.empty())
                                {
                                    if (temp.top()==Clear[j][1])
                                    {
                                        Clea = true;
                                        break;   
                                    }    
                                    temp.pop();
                                }    
                            }  
                            else if (temp.top()==Clear[j][1])
                            {
                                while (!temp.empty())
                                {
                                    if (temp.top()==Clear[j][0])
                                    {
                                        Clea = true;
                                        break;    
                                    }    
                                    temp.pop();
                                }    
                            }  
                              
                        }
                        if (Clea)
                        {
                            while (!res.empty())
                                res.pop();    
                        }
                                
                    }
                    
                }
            }
            string ans = "";
            while (!res.empty())
            {
                ans+=res.top();
                res.pop();    
            }
            cout<<"Case #"<<Case<<": [";
            for (int i=ans.size()-1; i>=0; i--)
            {
                if (i!=ans.size()-1)
                    cout<<", ";
                cout<<ans[i];    
            }
            cout<<"]"<<endl;
        
        }    
    }
    
    
    
    return 0;
}



