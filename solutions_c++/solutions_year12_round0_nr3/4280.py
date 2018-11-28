#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<algorithm>
#include<string>
#include<iostream>
#include<sstream>
#include<complex>

using namespace std;

const int inf = 2147483647;
const double eps = 1e-9;
const double pi = acos(-1.0);

const int maxn = 1000;
const int mod = 1000003;

int n, m,i ,j, k, s, t, p, be, ed;
int c[1001];
int sum;
void comp1(int x)
{
    int val;
    val = x/10+10*(x%10);
    if(val<=ed&&val>x) sum++;
    return ;
}

void comp2(int x)
{
     int val1,val2;
     val1 = x/10+100*(x%10);
     val2 = x/100+10*(x%100);     
     if(val1<=ed&&val1>x) sum++;
     if(val2<=ed&&val2>x) sum++;
}
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int ntest;
	cin>>ntest;
	for(int test=1; test<=ntest; test++){
        scanf("%d%d",&be,&ed);
        sum = 0;
		for(i=be;i<=ed;i++){
            if(i>=10&&i<=99) comp1(i); 
            if(i>=100&&i<=999) comp2(i);
        }
		cout<<"Case #"<<test<<": "<<sum<<endl;
	}
	return 0;
}
