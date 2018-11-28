# include <iostream>
# include <vector>

using namespace std;
int main()
{
    int L,D,N,I=0;
    cin>>L>>D>>N;
    string str;
    bool brac=false;
    int K=0,J=0;
    vector <string >dic;   
    int test=1;
     
     
    while (I++<D)
    {
                    cin>>str;
                    dic.push_back(str);                                
    }
        
    while (N--)
    {
          cin>>str;
          long int count=0;
          vector<string>  arr;
    string sub;
          for (I=0;I<str.length();I++)
          {
              if (str[I]=='(')
              {string sub;brac=true;continue;}
              else if (str[I]==')')
              {arr.push_back(sub);sub.erase(sub.begin(),sub.end());brac=false;continue;}
              if (brac==true)
              {
                            sub.push_back(str[I]);
              }
              if (brac==false)
              {
                 string s;
                 s.push_back(str[I]);
                 arr.push_back(s);
              }
          }
            
              
              for (I=0;I<dic.size();I++)
              {
                  K=0;
                  for ( J=0;J<dic[I].size();J++)
                  {if (find(arr[K].begin(),arr[K].end(),dic[I][J])==arr[K].end())
                  {break;}
                  K++;}
                  
                  if (J==dic[I].size())
                  {count++;}
              }
              
              cout<<"Case #"<<test++<<": "<<count<<endl;
              
                  
                  
                  
                  
              
              
              }
              
}                        
                            
              
              
              
              
          
          
          
          
                 
          
          
          
          
     
                             
          
    
        
                     
