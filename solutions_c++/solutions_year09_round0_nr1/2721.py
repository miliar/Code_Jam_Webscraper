#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
int wrds[20][26];
vector<string > vs;
vector <string >dic;
int main()
{
    #ifndef ONLINE_JUDGE
	freopen("a.txt", "rt", stdin);
    freopen("b.txt", "wt", stdout);
    #endif

    int L,D,N,it=1;
    scanf("%d%d%d",&L,&D,&N);
    for(int i=0;i<D;i++)
    {
       string str="";cin>>str;
       dic.push_back(str);
    }
    for(int i=0;i<N;i++)
    {
       memset(wrds,0,sizeof(wrds));
       vs=vector<string > ();
       string in="";cin>>in;
       string tm="";
       int flg=0;
       for(int k=0;k<in.size();k++)
       {
          if(in[k]=='(')flg=1,tm="";
          else if(in[k]==')')flg=0,vs.push_back(tm),tm="";
          else if(in[k]>='a'&& in[k]<='z'&&flg)tm+=in[k];
          else {tm="";tm+=in[k];vs.push_back(tm);}
       }
       for(int k=0;k<vs.size();k++)
          for(int j=0;j<vs[k].size();j++)
            wrds[k][vs[k][j]-'a']=1;
          int cnt=0;  
       for(int k=0;k<dic.size();k++)
       {
          int j=0;
          for(;j<dic[k].size();j++)
          {
             if(!wrds[j][dic[k][j]-'a'])break;
          }
          if(j==dic[k].size())cnt++;
       }
        cout<<"Case #"<<it++<<": "<<cnt<<endl;
    }
    return 0;
}




