//$CWD$\a.exe input >> output

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;


#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define ALL(a) (a).begin(),(a).end()
#define MP make_pair
#define pb push_back
#define B begin()
#define E end()
#define s(a) ((long long)a.size())
#define vs vector<string>
#define vi vector<int>
#define vp vector<part>
#define ll long long
#define ld long double
#define MOD 100003



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


string itoa(ld n,int k=0)
{
     char ans[100000];
     if(k==0){
     if((ll)n==n)sprintf(ans,"%Ld",(ll)n);
     else sprintf(ans,"%Lf",n);
     }
     else {
     if((ll)n==n)
     sprintf(ans,"%.*Ld",k,(ll)n);
     else
     sprintf(ans,"%.*Lf",k,n);
     }
	 string ans1(ans);
     return ans1;
     }

vi scanvi(){
            vi ans;
            char line[4096];
            int len;
   if(gets(line) == NULL) {
            printf("fgets() fail\n");
            exit (1);
        }
        len = strlen(line);
        if(line[len-1]=='\n') {
            line[len-1] = '\0';
            len--;
        }
      vs input= token(string(line),' ');//make sure you split correctly ..............1
      for(int e1=0;e1<s(input);e1++){
              ans.pb(atoll(input[e1]));
          //    fprintf(stderr,"%d   ",atoll(input[e1]));
              }
            //  fprintf(stderr,"\n");
         return ans;
         }


class part{
      public:
             int a1;
             int a2;
             int a3;
             };





int func(vp data){
int ans=0;
for(int e1=0;e1<s(data);e1++){
	for(int e2=0;e2<s(data);e2++){
	if((data[e1].a1-data[e2].a1)*(data[e1].a2-data[e2].a2)<0)ans++;}}
	return ans;}

int SolveTest(int test)
{
	int N;
	scanf("%d\n", &N);
	//CLEAR(Res, -1);
	vi pos;part temp;vp data;
	for(int e1=0;e1<N;e1++){
	pos=scanvi();
	temp.a1=pos[0];temp.a2=pos[1];
	data.pb(temp);}
    int ans=func(data);
    ans/=2;
    if(ans!=-1)
	printf("Case #%d: %d\n", test + 1,ans );
	else
	printf("Case #%d: IMPOSSIBLE\n", test + 1 );
	return 0;
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
	char buf[1 << 7];
	gets(buf);
	sscanf(buf, "%d\n", &T);
	FOR(t, 0, T)
	{
		//fprintf(stderr, "Solving %d/%d\n", t + 1, T);
		SolveTest(t);
	}

	return 0;
};
