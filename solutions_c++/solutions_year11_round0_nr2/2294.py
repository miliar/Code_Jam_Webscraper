# include <iostream>
# include <vector>

# define p push_back

using namespace std;


bool destroy(string a,vector <string> clr)
{
     int sz,i,j;
     string tmp;
     sz = clr.size();
     for(i=0;i<sz;i++)
        if(a==clr[i])
           return 1;
     tmp = a;
     tmp[0] = a[1];
     tmp[1] = a[0];     
     for(i=0;i<sz;i++)
        if(tmp==clr[i])
           return 1;
     return 0;
}

string combine(string a,vector <string> app)
{
       int sz,i,j;
       sz = app.size();
       string ret;
       ret = "";
       for(i=0;i<sz;i++)
       {
            if(a[0]==app[i][0] && a[1] == app[i][1])
            {
                ret = app[i][2];
                return ret;                
            }
            else if(a[0]==app[i][1] && a[1] == app[i][0])
            {
                ret = app[i][2];
                return ret;                
            }                 
       }
       return ret;       
}

int main()
{
    int t,cnt=1;
    cin>>t;
    while(t--)
    {
              int c,d,n,i,j;
              string t1,t2,t3,str;
              vector <string> clr,app;
              char y,z;
              cin>>c;
              for(i=0;i<c;i++)
              {
                   cin>>t1;
                   app.p(t1);
              }
              cin>>d;
              for(i=0;i<d;i++)
              {
                   cin>>t1;
                   clr.p(t1);
              }       
              cin>>n;
              cin>>str;   
              for(i=1;i<n;i++)
              {
                  t1 = str[i];
                  t2 = str[i-1];
                  t1 += t2;
                  t3 = combine(t1,app);
                  if(t3 != "")
                  {
                      //cout<<"combine\n";
                      str.erase(i-1,2);
                      str.insert(i-1,t3);
                      //cout<<str<<endl;
                      n -= 1;
                      i -= 1;
                      continue;
                  }
                  y = str[i];
                  for(j=i-1;j>=0;j--)
                  {
                  z = str[j];
                  t1 = y;
                  t2 = z;
                  t1 += t2;
                  //cout<<t1<<endl;
                  if(destroy(t1,clr))
                  {
                      //cout<<"erase all\n";
                      str.erase(0,i+1);
                      //cout<<str<<endl;
                      i = 0;
                      n = str.size(); 
                      break;               
                  }   
                  }     
              }
         if(n!=0)
                 cout<<"Case #"<<cnt++<<": ["<<str[0];//<<str<<endl;
         if(n==0)
                 cout<<"Case #"<<cnt++<<": [";//<<str<<endl;
         
         //cout<<str[0]<<",";
         for(i=1;i<n;i++)
         {
              cout<<", "<<str[i];                
         }
         cout<<"]\n";
    }
    //system("pause");    
}
