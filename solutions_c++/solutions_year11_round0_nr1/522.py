#include<iostream>
#include<vector>

using namespace std;

int n,t,int1,curro,currb,currot,currbt,currt;
char ch[100],ch1;
vector<int> O,B;
vector<char> V;

int main()
{
    cin>>t;
    
    for(int q=1;q<=t;q++)
    {
        O.clear();
        B.clear();
        V.clear();
        cin>>n;
        
        for(int i=1;i<=n;i++)
        {
            cin>>ch1;
            cin>>int1;
            
            V.push_back(ch1);
            
            if(ch1=='O')
                O.push_back(int1);
            else if(ch1=='B')
                B.push_back(int1);
        }
        
        O.push_back(99999999);
        B.push_back(99999999);
        
        curro=1;
        currb=1;
        currot=0;
        currbt=0;
        currt=0;
        
        for(int w=1;;w++)
        {
            if(currt>=V.size())
            {
                cout<<"Case #"<<q<<": "<<w-1<<"\n";
                break;
            }
            
            
            if(curro==O[currot])
            {
                if(V[currt]=='O')
                {
                    currt++;
                    currot++;
                    
                    if(currb<B[currbt])
                        currb++;
            
                    else if(currb>B[currbt])
                        currb--;
                    
                    continue;
                    
                }
            }
            
            if(currb==B[currbt])
            {
                if(V[currt]=='B')
                {
                    currt++;
                    currbt++;
                    
                    if(curro<O[currot])
                        curro++;
            
                    else if(curro>O[currot])
                        curro--;
                    continue;
                }
            }
            
            
                    
                    
                    
            
            
            if(curro<O[currot])
                curro++;
            
            else if(curro>O[currot])
                curro--;
            
            if(currb<B[currbt])
                currb++;
            
            else if(currb>B[currbt])
                currb--;
        }
    }
}
            
            
            
            
            
            
            