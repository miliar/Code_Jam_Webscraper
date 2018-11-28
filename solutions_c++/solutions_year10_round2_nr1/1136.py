
#include<iostream>
#include<conio.h>
#include<string>
#include<set>

using namespace std;

int main(int arg,char** argv)
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int runs;
    int n;
    int m;
    string* sn;
    string* sm;
    set<string> s1;
    int total;
    
    cin>>runs;
    for(int c=0;c<runs;c++)
    {
        total=0;
        s1.clear();
        cin>>n>>m;
        
        if(n>0)
            sn = new string[n];
        if(m>0)
            sm = new string[m];
            
        for(int i=0;i<n;i++)
            cin>>sn[i];
        for(int i=0;i<m;i++)
            cin>>sm[i];

        set<string>::iterator ite;

        for(int i=0;i<n;i++)
        {
            string sTemp = sn[i];
            s1.insert(sn[i]);
            int l=sTemp.find_last_of("/",string::npos);            
            while(l != 0 && l != string::npos)
            {
                sTemp = sTemp.substr(0,l);
                
                ite= s1.find(sTemp);
                if(ite != s1.end())
                    break;
                
                s1.insert(sTemp);
                l = sTemp.find_last_of("/",string::npos);
            }
        }
        
        for(int i=0;i<m;i++)
        {
            string sTemp = sm[i];
            
            ite = s1.find(sm[i]);
            if(ite==s1.end())
            {
                s1.insert(sm[i]);
                total++;
            }
            int l=sTemp.find_last_of("/",string::npos);
            while(l!=0 && l != string::npos)
            {
                sTemp =sm[i].substr(0,l);
                ite = s1.find(sTemp);
                if(ite==s1.end())
                {
                    s1.insert(sTemp);
                    total++;
                }
                else
                    break;
                
                l = sTemp.find_last_of("/",string::npos);
            }
        }
        
        cout<<"Case #"<<c+1<<": "<<total;
        if(c!=runs-1)
            cout<<"\n";
    }
    
    return 0;
}
