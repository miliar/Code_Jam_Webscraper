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
#define vvi vector<vi>
#define vll vector<long long>
#define vvll vector<vll>
#define vd vector<double>
#define vvd vector<vd>
#define rep(a,b,c) for(long long(a)=(b);(a)<(c);(a)++)
#define repd(a,b,c) for(long long(a)=(b);(a)>=(c);(a)--)
#define ll long long



#define lim 550
char buff[lim];
string scanstr(){
cin.getline(buff,lim);
//fprintf(stderr,"%s\n",buff);
return string(buff);
}
char letter[26];

//ll memo[
//ll A[
void solveTest(int test){
//memset(memo,0,sizeof(memo));
//memset(A,0,sizeof(A));

string str = scanstr();
rep(e1,0,s(str)){
if (str[e1]!=' ')
str[e1]=letter[str[e1]-'a'];

}










printans:;
printf("Case #%d: %s\n",test,str.c_str());
return;
printerr:;
printf("Case #%d: IMPOSSIBLE\n",test);//......................check if different case is not required i.e. Impossible
return;}


int main(int argc, char **argv)
{
    if(argc!=2){printf("usage: %s input_file\n", argv[0]);exit (1);}freopen(argv[1], "r", stdin);
    string source = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz";
    string target = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq";
    rep(e1,0,s(source)){
    if (source[e1]!=' ')
    letter[source[e1]-'a']=target[e1];
    }

	int T, t;
	scanf("%d\n", &T);
	rep(t, 1, T+1){
		//fprintf(stderr, "Solving %d/%d\n", t, T);
		solveTest(t);}
	return 0;
};
