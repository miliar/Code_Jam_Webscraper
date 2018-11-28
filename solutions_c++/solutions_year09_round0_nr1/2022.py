#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
 	 ifstream fin1("A-large.in");
 	 ofstream fout1("A-large.out");
     vector< pair<string,int> > m;
     int l,d,n;
     fin1>>l;
     fin1>>n;
     fin1>>d;
     for(int i=0;i<n;i++)
     {
        string s;
        fin1>>s;
        m.push_back(make_pair(s,0));
     }
     for(int i1=0;i1<d;i1++)
     {
        string s;
        fin1>>s;
        int c=0;
        int k,i;
        bool flag=false;
        for( i=0;i<s.size();i++)
        {
		 		
                if(s[i]=='(')
                {
                             k=i+1;
                             while(s[k]!=')')
                             {
	  				            
                                for(int j=0;j<m.size();j++)
                                {
								 		 
                                        if( m[j].first[c] == s[k] )
                                        {m[j].second++;flag=true;}
                                        
                                }
                                k++;
                             }
                 c++;
                 i=k;
                }
                else
                {
                     for(int j=0;j<m.size();j++)
                     {
                       if( m[j].first[c] == s[i] )
                       {m[j].second++;flag=true;}
                     }
                     c++;
                }
                if(flag==false){break;}
                flag=false;
        }
       
        
        int count =0;
        if(i==s.size())
        {
         for(int i=0;i<m.size();i++)
         {
	 		 if(m[i].second==l)count++;
	 		 m[i].second=0;
         }
		}
        fout1<<"Case #"<<i1+1<<": "<<count<<endl;
     }
     return 0;
	  }
                    
                    
                                     
