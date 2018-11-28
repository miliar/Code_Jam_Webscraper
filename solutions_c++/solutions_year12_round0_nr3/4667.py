#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
using namespace std;

string f1(long int n)
{
    string temp="";
    while(n){
      temp=temp+(char)(n%10+(int)'0');
      n/=10;
    }
    reverse(temp.begin(),temp.end());
    return temp;
}
int f2(string s)
{
    long int temp=0;
    for(int i=0;i<s.length();i++)
    {
        temp=10*temp+((int)s[i]-(int)'0');
    }
    return temp;
}
bool allsame(string s)
{
    bool temp=true;
    for(int i=1;i<s.length();i++)
      if(s[i]!=s[i-1]){
        temp=false;
        break;
        }
    return temp;
}
int main()
{//cout<<"here";
    ifstream fin("1.in");
    ofstream fout("1a.out");
    long int t,a,b,count=0;
    string s;
    fin>>t;
    for(int cn= 1;cn<= t;cn++)
    {
        vector<string> record[1001];
        count=0;
        fin>>a>>b;

        for(int i=a;i<=b;i++)
        {
           s=f1(i);
           record[i].push_back(s);
           if(allsame(s))
             continue;
           for(int j=1;j<s.length();j++){
             rotate(s.begin(),s.begin()+1,s.end());
             if(s[0]=='0')
               continue;
             bool check=false;
             for(int s_i=0;s_i<record[i].size();s_i++)
               if(record[i][s_i]==s){
                 check=true;
                 break;
                 }
             if(check)
               continue;
             if(f2(s)<=b && f2(s)>=a){
               record[i].push_back(s);
               record[f2(s)].push_back(f1(i));
               count++;
               //cout<<i<<": "<<s<<endl;
             }
           }
        }
        fout<<"Case #"<<cn<<": "<<count<<endl;
    }
    return 0;
}

