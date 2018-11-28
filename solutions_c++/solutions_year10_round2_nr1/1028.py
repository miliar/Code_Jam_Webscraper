#include <string>
#include <iostream>
#include <set>
using namespace std;

set<string>  a;

int f(const string &s)
{
    size_t p=0;
    int sum=0;
    string t;
    
    while(1)
    {
        p=s.find_first_of('/',p+1);
        if(p==string::npos)
        {
            sum++;
            a.insert(s);
            break;
        }
        t=s.substr(0,p);
        if(a.count(t)==1)
            continue;
        sum++;
        a.insert(t);
    }
    
    return sum;
}
int main(void)
{
    int T,N,M;
    int i;
    string s;
    int sum;
    
    cin>>T;
    for(int caseid=1;caseid<=T;caseid++)
    {
        cin>>N>>M;
        for(i=0;i<N;i++)
        {
            cin>>s;
            a.insert(s);                                
        }   
        sum=0;
        for(i=0;i<M;i++)
        {
            cin>>s;
            if(a.count(s)==1)
                continue;
            sum+=f(s);                      
        }
                
        cout<<"Case #"<<caseid<<": "<<sum<<endl;
        a.clear();
    }
//    system("PAUSE");
    return 0;
}
