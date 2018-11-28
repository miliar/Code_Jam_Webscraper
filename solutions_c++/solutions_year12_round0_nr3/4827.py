#include<iostream>
#include<fstream>
#include<cstdio>
#include<vector>
#include<algorithm>
#define s(i) scanf("%d",&i)
#define ps(i) printf("%d ",i)
#define pa(i) printf("%d\n",i)
#define ph printf("here\n");
#define fr(i,s,n) for(long int i=s;i<n;i++)

using namespace std;

string tostring(long int n)
{
    string toret="";
    while(n){
      toret=toret+(char)(n%10+(int)'0');
      n/=10;
    }
    reverse(toret.begin(),toret.end());
    return toret;
}
int toint(string s)
{
    long int toret=0;
    fr(i,0,s.length())
    {
        toret=10*toret+((int)s[i]-(int)'0');
    }
    return toret;
}
bool allsame(string s)
{
    bool toret=true;
    fr(i,1,s.length())
      if(s[i]!=s[i-1]){
        toret=false;
        break;
        }
    return toret;
}
int main()
{//cout<<"here";
    ifstream fin("q3.in");
    ofstream fout("a1.out");
    long int t,a,b,count=0;
    string s;
    fin>>t;
    fr(cn, 1, t+1)
    {
        vector<string> table[1001];
        count=0;
        fin>>a>>b;

        fr(i,a,b+1)
        {
           s=tostring(i);
           table[i].push_back(s);
           if(allsame(s))
             continue;
           fr(j,1,s.length()){
             rotate(s.begin(),s.begin()+1,s.end());
             if(s[0]=='0')
               continue;
             bool already_counted=false;
             fr(s_i,0,table[i].size())
               if(table[i][s_i]==s){
                 already_counted=true;
                 break;
                 }
             if(already_counted)
               continue;
             if(toint(s)<=b && toint(s)>=a){
               table[i].push_back(s);
               table[toint(s)].push_back(tostring(i));
               count++;
               //pout<<i<<": "<<s<<endl;
             }
           }
        }
        fout<<"Case #"<<cn<<": "<<count<<endl;
    }
    return 0;
}

