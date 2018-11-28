//$CWD$\a.exe input >> output

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cctype>
#include <complex>
#include <cassert>
#include <string>
#include <valarray>
#include <queue>
#include <iterator>
using namespace std;
#define pb push_back
#define B begin()
#define E end()
#define s(a) ((long long)a.size())
#define vs vector<string>
#define vi vector<int>
#define rep(a,b,c) for(int(a)=(b);(a)<(c);(a)++)
#define ll long long
#define ld long double




vector<string> token(string start,char a)
{
        vector<string> splitted;
        while(s(start)!=0)
        {
             size_t k= start.find(a,0);
             if(k==string :: npos)
               {  
                   splitted.push_back(start);
                   start="";
                   break;
               }               
             string temp(start.begin(),start.begin()+k); 
             if(s(temp)>0)      
               splitted.push_back(temp);
             start.erase(0,k+1);       
       }
       return splitted;
}

long long atoll(string k){                          
long long ans=0;                              
for(int i=0;i<s(k);i++){
ans=ans*10+k[i]-'0';
}
return ans;
}





























void solveTest(int t){
char buf[150];
string ans;
int c,d,n;
char x,y,z;
map<pair<char,char>,char> trans;
set<pair<char,char> >enemy;
scanf("%d",&c);
rep(e1,0,c){
scanf(" %c%c%c",&x,&y,&z);
trans[make_pair(x,y)]=z;}

scanf(" %d",&d);
rep(e1,0,d){
scanf(" %c%c",&x,&y);
enemy.insert(make_pair(x,y));}

scanf(" %d ",&n);
scanf("%s\n",buf);string str(buf);

//ans.pb(str[0]);
rep(e1,0,n){
ans.pb(str[e1]);
if(s(ans)>=2){
if(trans.find(make_pair(ans[s(ans)-1],ans[s(ans)-2]))!=trans.E){
x=trans[make_pair(ans[s(ans)-1],ans[s(ans)-2])];
ans.resize(s(ans)-2);ans.pb(x);}
else if(trans.find(make_pair(ans[s(ans)-2],ans[s(ans)-1]))!=trans.E){
x=trans[make_pair(ans[s(ans)-2],ans[s(ans)-1])];
ans.resize(s(ans)-2);ans.pb(x);}
else{
rep(e1,0,s(ans)-1){
if(enemy.find(make_pair(ans[e1],ans[s(ans)-1]))!=enemy.E||
enemy.find(make_pair(ans[s(ans)-1],ans[e1]))!=enemy.E){
ans="";break;}}}}}

printf("Case #%d: [",t);
rep(e1,0,s(ans)){
if(e1)printf(" ");
printf("%c",ans[e1]);
if(e1<s(ans)-1)printf(",");}
printf("]\n");


}








int main(int argc, char **argv)
{
    if(argc!=2){printf("usage: %s input_file\n", argv[0]);exit (1);}freopen(argv[1], "r", stdin);
	int T, t;
	scanf("%d\n", &T);
	rep(t, 1, T+1){
		//fprintf(stderr, "Solving %d/%d\n", t, T);
		solveTest(t);}
	return 0;
};
