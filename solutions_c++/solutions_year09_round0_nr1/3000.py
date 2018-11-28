#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
#define f(x,y) for(int x=0;x<y;x++)
#define pb push_back
using namespace std;

int main()
{
    ifstream fin("A-small.in");
    ofstream fout("A-large.out");
    int L,D,N;
    vector<string> v,cv;
    set<char> letters;
    fin>>L>>D>>N;
    
    f(i,D)
    {
        string t;
        fin>>t;
        v.pb(t);
        f(j,t.size())letters.insert(t[j]);
    }
    
    
    vector<vector<set<char> > > s;
    vector<int> res;
    
    f(i,N)
    {
        string t;
        fin>>t;
        cv.pb(t);
        
        vector<set<char> > tmp;
        s.pb(tmp);
        
        set<char> tmp2;
        f(x,50)s[i].pb(tmp2);
        
        res.pb(0);
        
        int ind=-1;
        int spos=-1,epos=-1;
        
        f(j,t.size())
        {
            if(t[j]=='(')
            {
                ind++;
                spos=j;
            }
            else if(t[j]==')')
            {
                epos=j;
            }
            else
            {
                if(spos>epos)
                {
                    s[i][ind].insert(t[j]);
                }
                else if(epos>=spos)
                {
                    ind++;
                    s[i][ind].insert(t[j]);
                }
            }
        }
        
        //resulting...
        f(j,D)
        {
            bool flag=true;
            f(k,L)
            {
                //cout<<i<<" "<<j<<" "<<" "<<v[j][k]<<" in "<<cv[i]<<" "<<s[i][k].count(v[j][k])<<endl;
                
                if(s[i][k].count(v[j][k])==0)
                {
                    flag=false;
                    break;
                }
            }
            
            if(flag)res[i]++;
            
            //cout<<v[j]<<" ";
            //cout<<endl;
        }
        //cout<<endl;
    }
    
    //cout<<"End."<<endl;
    f(i,res.size())cout<<"Case #"<<i+1<<": "<<res[i]<<endl;
    f(i,res.size())fout<<"Case #"<<i+1<<": "<<res[i]<<endl;
    cin.get();
    
    return 0;
}
