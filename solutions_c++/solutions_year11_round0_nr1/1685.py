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


int n,m;
//this function should also print the result
void solveTest(int t){
char ch;string str;
vector<int> pos;
int otime,opos,btime,bpos;
scanf("%d",&n);
rep(e1,0,n){
scanf(" %c %d",&ch,&m);
str.pb(ch);pos.pb(m);}
otime=0;opos=1;
btime=0;bpos=1;
rep(e1,0,n){
if(str[e1]=='O'){
otime=max(abs(opos-pos[e1])+otime,btime)+1;
opos=pos[e1];}
else{
btime=max(abs(bpos-pos[e1])+btime,otime)+1;
bpos=pos[e1];}}

printf("Case #%d: %d\n",t+1,max(otime,btime));
}




int main(int argc, char **argv)
{

    if(argc!=2) {
        printf("usage: %s input_file\n", argv[0]);
        exit (1);
    }
	freopen(argv[1], "r", stdin);
//	freopen("c.out", "w", stdout);



	int T, t;
	char buf[1 << 7];//................needs to take care of this
	gets(buf);
	sscanf(buf, "%d\n", &T);
	rep(t, 0, T)
	{
		//fprintf(stderr, "Solving %d/%d\n", t + 1, T);
		solveTest(t);
	}

	return 0;
};
