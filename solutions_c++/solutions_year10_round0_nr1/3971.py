
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
#define rep(a,b) for(int(a)=0;(a)<s(b);(a)++)
#define ll long long




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



string func(ll n,ll k){
if((k+1)%(ll)pow(2.L,(long double)n))return "OFF";
return "ON";
}



char * str= "welcome to code jam";
int    count = 0;
char line[4096];
#define MAX_LINE_LEN    512
#define MAX_STR_LEN        32

int main(int argc, char **argv)
{
    FILE *    fp;
    int        i, N;

    size_t    len;
    size_t  str_len = strlen(str);

    if(argc!=2) {
        printf("usage: %s input_file\n", argv[0]);
        exit (1);
    }

    /* build database from file*/
    if((fp = fopen(argv[1], "r")) == NULL) {
        printf("fopen() fail\n");
        exit (1);
    }

    if(fgets(line, sizeof(line), fp) == NULL) {
        printf("fgets() fail\n");
        exit (1);
    }
    if(sscanf(line, "%d", &N)!=1) {
        printf("invalid format\n");
        exit (1);
    }
#ifdef DEBUG
    printf("N=%d\n", N);
#endif

    for(i=0;i<N;i++) {
        if(fgets(line, sizeof(line), fp) == NULL) {
            printf("fgets() fail\n");
            exit (1);
        }
        len = strlen(line);
        if(line[len-1]=='\n') {
            line[len-1] = '\0';
            len--;
        }
#ifdef DEBUG
        printf("line=[%d]%s\n", i+1, line);
#endif




      vs input= token(string(line),' ');//make sure you split correctly ..............1
      string out = func(atoll(input[0]), atoll(input[1]));
      printf("Case #%d: %s\n",i+1, out.c_str());//make sure you print correctly..............2


    }

    fclose(fp);
    return 0;
}




