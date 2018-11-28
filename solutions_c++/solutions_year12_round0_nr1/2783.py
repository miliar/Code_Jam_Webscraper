#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <list>
#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

#define DEBUG
#define REP(i,a) for(i=0;i<a;i++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define VE vector<int>
#define SZ size()
#define PB push_back
#define all(i) (i).begin(), (i).end()

int main()
{

   freopen("inputA.txt","r",stdin);
   freopen("outputA.txt","w",stdout);


    map<char,char> map1 ;
    int test,i,j;
    map1['a']='y';map1['j']='u';map1['s']='n';
    map1['b']='h';map1['k']='i';map1['t']='w';
    map1['c']='e';map1['l']='g';map1['u']='j';
    map1['d']='s';map1['m']='l';map1['v']='p';
    map1['e']='o';map1['n']='b';map1['w']='f';
    map1['f']='c';map1['o']='k';map1['x']='m';
    map1['g']='v';map1['p']='r';map1['y']='a';
    map1['h']='x';map1['q']='z';map1['z']='q';
    map1['i']='d';map1['r']='t';map1[' ']=' ';
    scanf("%d",&test);
    cin.ignore();
    string cad1;
    REP(j,test)
    {
        getline(cin,cad1);
        printf("Case #%d: ",j+1);
        REP(i,cad1.length())
            printf("%c",map1[cad1[i]]);
        printf("\n");
    }

	fclose(stdout);
	fclose(stdin);

   return 0;
}
