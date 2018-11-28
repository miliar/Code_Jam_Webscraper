# include<iostream>
# include<vector>
# include<string>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    int j=1;
    while (test--)
    {
          string str;
          cin>>str;
          int array[36];
          memset (array,0,sizeof (array));
          for (int i=0;i<str.size ();i++)
          {
              if (isdigit (str[i]))
              {
                    array [str[i]-'0']++;
              }
              else
              {
                  array[str[i]+10-'a']++;
              }
          }
          int array1[36];
          for (int i=0;i<36;i++)
          {
              array1[i]=-1;
          }   
          vector <int> str2;
          int num=1; 
          if (isdigit(str[0]))
          {
              array1[str[0]-'0']=1;
          }
          else
          {
              array1[str[0]-'a'+10]=1;
          }  
          str2.push_back (1);      
          int index=0;                
          for (int i=1;i<str.size ();i++)
          {
              if(isdigit (str[i]))
              {
                    if (array1[str[i]-'0']==-1)
                    {
                           array1[str[i]-'0']=index;
                           str2.push_back (index);
                           if (index==0)
                              index++;
                           index++;
                    }
                    else
                    {
                        str2.push_back (array1[str[i]-'0']);
                    }    
              }
              else
              {
                    if (array1[str[i]-'a'+10]==-1)
                    {
                          array1[str[i]-'a'+10]=index;
                          str2.push_back (index);
                          if (index==0)
                             index++;
                          index++;
                    }
                    else
                    {
                        str2.push_back (array1[str[i]-'a'+10]);
                    }
              }
          } 
          int base;
          if (index==0)
          {
               base=2;
          }
          else
          {
              base=index;
          }
          unsigned long long ans=0LL;    
          for (int i=0;i<str2.size();i++)
          {
              ans*=base;
              ans+=str2[i];
          }   
          //cout<<base<<endl;
          cout<<"Case #"<<j<<": "<<ans<<endl;
          j++;
    }
    return 0;
}         
                                                                                                                                           
