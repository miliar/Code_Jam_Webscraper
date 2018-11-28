#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;
vector<string> vec_dic;

string str_deal;
int n_result=0;
int mydo(int n_start,int n_checkStart=0,int n_checkEnd=vec_dic.size(),int n_level=0)
{
if(n_checkStart>=n_checkEnd) return 0;
if(n_start>=str_deal.length())
    n_result++;
else{
    int n_new_start=n_start;
   if(str_deal[n_start]=='(')
   {
      while(str_deal[n_new_start]!=')')
        {n_new_start++;}
     for(n_start++;n_start<n_new_start;n_start++)
     {
        char c_check=str_deal[n_start];
        int n_checkTempStart=n_checkStart;

        while(n_checkTempStart<n_checkEnd&&vec_dic[n_checkTempStart][n_level]!=c_check)
                n_checkTempStart++;
        int n_checkTempEnd=n_checkTempStart;
        while(n_checkTempEnd<n_checkEnd&&vec_dic[n_checkTempEnd][n_level]==c_check)
                n_checkTempEnd++;
        if(n_checkTempEnd >n_checkTempStart)
           mydo(n_new_start+1,n_checkTempStart,n_checkTempEnd,n_level+1);
     }
   }
    else{
        char c_check=str_deal[n_start];
        int n_checkTempStart=n_checkStart;

        while(n_checkTempStart<n_checkEnd&&vec_dic[n_checkTempStart][n_level]!=c_check)
                n_checkTempStart++;
        int n_checkTempEnd=n_checkTempStart;
        while(n_checkTempEnd<n_checkEnd&&vec_dic[n_checkTempEnd][n_level]==c_check)
                n_checkTempEnd++;
        if(n_checkTempEnd >n_checkTempStart)
           mydo(n_new_start+1,n_checkTempStart,n_checkTempEnd,n_level+1);
        }

}

}
int main()
{
    ifstream in("a.in");
    ofstream out("a.out");

int l =0,d=0,n=0;
in>>l>>d>>n;

string str_temp;
int i=0;
for(i=0;i<d;i++)
{
in>>str_temp;
vec_dic.push_back(str_temp);
    }
sort(vec_dic.begin(),vec_dic.end());

for(i=1;i<=n;i++)
{
    in>>str_deal;
    n_result=0;
    mydo(0);
    out<<"Case #"<<i<<": "<<n_result<<endl;

}

    return 0;
}
