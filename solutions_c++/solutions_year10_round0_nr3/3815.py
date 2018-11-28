#include<iostream>
#include<sstream>
#include<vector>
#include<fstream>

using namespace std;

template<class T, class U> T cast (U x) { T y; ostringstream a; a<<x; istringstream b(a.str()); b>>y; return y; }


int main()
{
    
    ifstream fi("C-small-attempt0.in");
    ofstream fo("C-small.out");
    
    string st;
    getline(fi,st);
    
    int t;
    t=cast<long long>(st);
    
    for(int x=0;x<t;x++)
    {
    long long k;
    long long ret=0;
    
    vector<long long>v1,v;
    
    long long sum=0;
    long long check=0;
    long long r;
    
    int in=-1;
    
    st="";
          
    getline(fi,st);
    
    stringstream ss;
    ss<<st;
    long long s;
    
    while(ss>>s)
    {
          v1.push_back(s);
    }     
     
    st="";
    getline(fi,st);
    stringstream ss1;
    ss1<<st;
    
    while(ss1>>s)
    {
          v.push_back(s);
    }     
    
    r=v1[0];
    k=v1[1];
    
//    int check=0;
    
    while(1)
    {
           // cout<<v.size()<<endl;
            for(int i=0;i<v.size();i++)
            {
                    if( sum+v[i] <= k )
                    {
                        sum+=v[i];
                    }
                    else
                    {
                        in=i;
                        break;
                    }
            }
            
            for(int i=0;i<in;i++)
            {
                    v.push_back(v[i]);
            }
            
           // for(int i=0;i<v.size();i++)
             //       cout<<"vold"<<v[i]<<endl;
            if(in!=-1)        
                        v.erase(v.begin(),v.begin()+in);
            
            //for(int i=0;i<v.size();i++)
            //        cout<<"vnew"<<v[i]<<endl;
            
            //cout<<v.size()<<endl;
            
            check++;
            
            ret+=sum;
            
            if(check>=r)
                        break;
                        
            
            sum=0;
            
    }
    
    fo<<"Case #"<<x+1<<":"<<" "<<ret<<endl;
    }
    //system("pause");
    
    return 0;
}
