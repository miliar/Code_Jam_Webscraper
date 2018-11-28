# include<iostream>
# include <sstream>

using namespace std;

int main ()
{
    int array [501][20];
    int test,test1=1;
    string str2;
    getline (cin,str2);
    istringstream in (str2);
    in>>test;
    //cout<<test<<endl;
    while (test--)
    {
          memset (array,0,sizeof (array));
          string str,str1;
          getline(cin,str);
          str1="welcome to code jam";
          for (int j=1;j<=str.size();j++)
          {
              if (str1[0]==str[j-1])
                  {
                     array[j][1]=1;
                  }
          }
          for (int i=2;i<=str1.size ();i++)
          {
              for (int j=1;j<=str.size ();j++)
              {
                  if (str1[i-1]==str[j-1])
                  {
                       for (int k=1;k<=j;k++)
                       {
                           array[j][i]+=(array[k][i-1]);
                           array[j][i]%=10000;
                       }
                  }
              }
          }
          int ans=0;
          for (int i=1;i<=str.size ();i++)
          {
              ans+=array[i][str1.size ()];
              ans%=10000;
          }
          int ans1=ans;
          int dig=0;
          string value="";
          while (ans1)
          {
                dig++;
                value.push_back ((ans1%10)+'0');
                ans1/=10;
          }
          for (int i=0;i<4-dig;i++)
              value.push_back ('0');
          string prrr;
          reverse (value.begin(),value.end());    
          cout<<"Case #"<<test1<<": "<<value<<endl;
          test1++;                                            
    }
    return 0;
}          
