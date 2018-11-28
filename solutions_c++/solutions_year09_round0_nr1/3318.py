#include<iostream>
#include<vector>

using namespace std;

bool isthere(char arr[11][30],string str)
{
              int flag=0,cflag;
              for(int a=0;a<11;a++)
              {
              for(int b=0;arr[a][b]!='*';b++)
              {
              
              if(arr[a][b]==str[a]) {flag =1;break;}
              else flag=0; 
                           }
              if(flag!=1) return false;
               
              }
          return true;
}

int main()
{
    
    int l,d,n,r=0;
  cin>>l>>d>>n;
   n++;
   vector<string> dic;
    
    for(int i=0;i<d;i++)
    {
            string str;
            cin>>str;
            dic.push_back(str);
            }
//cout<<"**dic:";
  //  for(int i=0;i<d;i++)
    //{
      //      cout<<dic[i]<<endl;
        //    }


    while(n--)
    {
              char arr[5010][30];    
              for(int a=0;a<11;a++)
              for(int b=0;b<30;b++)
              arr[a][b]='*';
              char ch;
              int i=-1,j=0;
              int flag=0;
              while(scanf("%c",&ch))
              {
                    if(ch=='\n') {break;}
                    ////...now..fuck..
                    if(ch=='(')
                          {flag=1;i++;j=-1;continue;}
                    else if(ch==')')
                          {flag=0;continue;}
                    
                    if(flag==1) j++;
                    
                    else {i++;j=0;}                
                    arr[i][j]=ch;
                    
                    }
                    
              
              int len=dic.size();
              i=0;
              int count=0;
              while(len--)
              {
                          if(isthere(arr,dic[i]))
                                                 count++;
                          i++;
                          }
              
              
              if(r==0) {r++;}
              else cout<<"Case #"<<r++<<": "<<count<<endl;
              
                          
                    
                    
                    
                    
                    
                    
                    }                       
              return 0;
              }
              
    
    
    
    
    
    
