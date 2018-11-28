#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int Falses(vector <bool> found)
{
    int count=0;    
    for(int i=0;i<found.size();i++)
    {
            if(found[i]==false)
                               count++;
    }
    return count;
}
int savingTheUniverse(vector <string> engine, vector <string> query)
{
    vector <bool> found(engine.size(),false);   
    int switches=0; 
    for(int i=0;i<query.size();)
    {
            //cout<<"hi1"<<endl;
            int j=i-1;
            bool flag=true;
            while(flag==true)
            {
                    j++;
                    for(int k=0;k<engine.size();k++)
                    {
                            if(j>=query.size())
                            {i=j;break;return switches;} 
                            if(query[j]==engine[k])
                                    found[k]=true;
                            int noOfFalses=Falses(found); 
                              
                            if(noOfFalses==1)
                            {flag=false;      break;  }
                    }  
                     
                    if(j>=query.size())
                            {i=j;break;}       
            }  
            
            if(j>=query.size())
                   {i=j;break;}
            //cout<<"hi2"<<endl;
            string cur;
            int m=-1;
            while(true)
            {  
               m++;
               if((found[m]==false)||m>=engine.size())
               {
                     cur=engine[m];                    
                     break;
               }
               
            }
            //cout<<"current and i"<<cur<<endl<<i<<endl;;
            int l=i;
            while(query[l]!=engine[m])
            {
                    l++;
                    if(l>=query.size())
                          break;                    
            }
            i=l;
            //cout<<l<<endl;
            for(int n=0;n<found.size();n++)
                    found[n]=false;
            if(i<query.size())
                    switches++;             
    }
    //cout<<"hiend";
    //switches--;
    //hi:
    return switches;
}
int main()
{
    int k;
    cin>>k;
    for(int i=0;i<k;i++)
    {
           int s,q;
           cin>>s;
           vector <string> engine;
           cin.clear(); cin.ignore();
           for(int j=0;j<s;j++)
           {
                   string str;
                   //cout<<"Hi";
                   char a[101];
                   cin.getline(a,101);
                   str=a;
                   engine.push_back(str);        
           }
           cin>>q;
           vector <string> query;
           cin.clear(); cin.ignore();
           for(int j=0;j<q;j++)
           {
                   string str;
                   char a[101];
                   //   cout<<"Hi";
                   cin.getline(a,101);
                   str=a;
                   query.push_back(str);        
           }
           int ans=savingTheUniverse(engine, query);  
           cout<<"Case #"<<(i+1)<<": "<<ans;
           
           if(i!=(k-1))
                       cout<<endl;
    }
    getchar();
    getchar();
    return 0;    
}



