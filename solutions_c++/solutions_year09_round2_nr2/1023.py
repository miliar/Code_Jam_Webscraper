#include<iostream>
#include<vector>
#include<string>
using namespace std;
char arr[100]="";
int main()
{ int T=0;
  gets(arr);
  string t=arr;
  for(int i=0;i<t.size();i++)
  T=T*10+t[i]-'0';
  for(int t=0;t<T;t++)
  { gets(arr);
    string str=arr;
    int len=str.size();
    string res="";
    int done=0;
    //cout<<t<<" "<<str<<"\n";
    for(int i=len-2;i>=0;i--)
    if(str[i]<str[i+1])
    { //cout<<i<<" ";
      char ch=str[i];
      string temp="";
      int pos=i+1;
      for(int j=i+1;j<len;j++)
      if(str[j]>str[i]&&(ch==str[i]||str[j]<ch))
      { ch=str[j];
        pos=j;
      }
      for(int j=i+1;j<len;j++)
      if(j!=pos)
      temp+=str[j];
      temp+=str[i];
      sort(temp.begin(),temp.end());
      res=str.substr(0,i);
      res+=ch;
      res+=temp;
      done=1;
      break;
    }
    if(done==0)
    { string temp=str;
      sort(temp.begin(),temp.end());  
      string zero="";
      res="";
      for(int i=0;i<len;i++)
      if(temp[i]=='0')
      zero+="0";
      else
      res+=temp[i];
      if(res.size()==1)
      { res+=zero;
        res+="0";
      }
      else
      res.insert(1,zero+"0");
    }    
    cout<<"Case #"<<t+1<<": "<<res<<"\n";
  }
}  
