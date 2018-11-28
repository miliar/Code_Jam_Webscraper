#include<iostream>
#include<vector>

using namespace std;

int t,A[150][150],D[150][150],c,d,n,t1,t2,t3;
vector<int> V,W;
char c1,c2,c3;

int main()
{
    cin>>t;
    
    for(int q=1;q<=t;q++)
    {
        V.clear();
        W.clear();
        for(int i=int('A');i<=int('Z');i++)
            for(int j=int('A');j<=int('Z');j++)
                {
                    A[i][j]=0;
                    D[i][j]=0;
                }
        
        
        cin>>c;
        for(int i=1;i<=c;i++)
        {
            cin>>c1>>c2>>c3;
            A[int(c1)][int(c2)]=int(c3);
            A[int(c2)][int(c1)]=int(c3);
        }
        
        cin>>d;
        
        for(int i=1;i<=d;i++)
        {
            cin>>c1>>c2;
            D[int(c1)][int(c2)]=1;
            D[int(c2)][int(c1)]=1;
        }
        
        cin>>n;
        for(int i=1;i<=n;i++)
        {
            cin>>c1;
            V.push_back(int(c1));
        }
        
        /*for(int i=0;i<V.size();i++)
            cout<<V[i]<<" ";
        cout<<"\n";
        
        
        for(int i=int('A');i<=int('Z');i++)
        {
            for(int j=int('A');j<=int('Z');j++)
                cout<<A[i][j]<<" ";
            cout<<"\n";
        }
        
        cout<<"\n\n\n";
        
        for(int i=int('A');i<=int('Z');i++)
        {
            for(int j=int('A');j<=int('Z');j++)
                cout<<D[i][j]<<" ";
            cout<<"\n";
        }
        */
        
        for(int i=0;i<V.size();i++)
        {
            W.push_back(V[i]);
            
            while(1)
            {
                if(W.size()==1)
                    break;
                
                t1=W[(W.size())-1];
                t2=W[(W.size())-2];
                
                if(A[t1][t2]==0)
                    break;
                
                t3=A[t1][t2];
                W.pop_back();
                W.pop_back();
                W.push_back(t3);
            }
            
            
            for(int e=0;e<W.size();e++)
            {
                if(D[W[e]][W[(W.size())-1]]==1)
                {
                    W.clear();
                    break;
                }
            }
        }
        
        if(W.size()==0)
        {
            cout<<"Case #"<<q<<": []\n";
            continue;
        }
        
        cout<<"Case #"<<q<<": [";
        for(int i=0;i<W.size()-1;i++)
            cout<<char(W[i])<<", ";
        cout<<char( W[(W.size()-1)])<<"]\n";
    }
}
        
            
        