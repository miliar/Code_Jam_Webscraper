#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;

#define MINI(a,b) ( (a<b)?(a):(b) )

int rle(string s)
    {
    int c=1;
    int l=s.length();  
    for(int i=1;i<l;i++)
            if(s[i]!=s[i-1]) c++;
    
    return c;
    }
    
string sper(string s,vector<int> v)
       {
      int z=v.size();
      int l=s.size();
      int n=(l/z); 
      
      string s2;
      for(int i=0;i<n;i++)
              {  
              for(int j=0;j<z;j++)
                            s2+=s[(i*z)+v[j]];
              }
       return s2;
       }
        
int main()
{
int N,K;
string s,s1;
    cin>>N;
int min;


    for(int x=0;x<N;x++)
            {
            cin>>K>>s;
            vector<int> v;
             for(int y=0;y<K;y++) v.push_back(y);
             min=rle(s);    
           
           while(next_permutation(v.begin(),v.end()) )
                                                    {
                                                    s1=sper(s,v);
             //                                       cout<<s1<<"  "<<min<<endl;
                                                    min=MINI(rle(s1),min);
                                                    }
            cout<<"Case #"<<x+1<<": "<<min<<endl;
            }

//s="aabaaaaa";
//cout<<rle(s)<<endl;
//system("pause");
return 0;
}
