#include<iostream>
#include<vector>
#include<string>
using namespace std;
char arr[1000]="";
int main()
{ int L,D,N;
  cin>>L>>D>>N;
  vector<string>words;
  for(int i=0;i<D;i++)
  { cin>>arr;
    words.push_back(arr);
  }
  for(int i=0;i<N;i++)
  { cin>>arr;
    string str=arr;
    vector<int>pat(L);
    int len=str.size();
    int cur=0;
    for(int j=0;j<len;)
    if(str[j]=='(')
    { j++;
      while(j<len&&str[j]!=')')
      pat[cur]|=(1<<(str[j++]-'a'));
      j++;
      cur++;
    }
    else
    { pat[cur]|=(1<<(str[j]-'a'));
      cur++;
      j++;
    }
    int res=0;
    for(int j=0;j<D;j++)
    { int valid=1;
      for(int k=0;k<L;k++)
      if((pat[k]&(1<<(words[j][k]-'a')))==0)
      { valid=0;
        break;
      }
      res+=valid;
    }
    cout<<"Case #"<<i+1<<": "<<res<<"\n";
  }
}
