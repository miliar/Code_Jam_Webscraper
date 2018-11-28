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
#include <string>

using namespace std;
#define MOD 100003
#define CMBMAX 501 //MAX can be 58
long long comb[CMBMAX][CMBMAX]; //select n1 from n2;
int mem[501][501],n; //pos, num

void cmbpopulate(){
    memset(comb,0,sizeof(comb));
    for(int i=0;i<CMBMAX;i++){
        comb[0][i]=1; 
    }
    for(int i=1;i<CMBMAX;i++)
    for(int j=1;j<=i;j++){
        comb[j][i]=(comb[j-1][i]*(i-j+1)/j);
		comb[j][i]%=MOD;
    }
}


int rec(int pos, int num){
	if(num>n)return 0;
	if(num==n)return 1;
	if(mem[pos][num]!=-1)return mem[pos][num];
	int ret=0, diff, na, nb; //select na from nb
	long long tempret;
	diff=num-pos;
	for(int i=num+diff;i<=n;i++){
		tempret=rec(num,i);
		nb=i-num-1;na=num-pos-1;
		tempret*=comb[na][nb];
		tempret%=MOD;
		ret=(ret+tempret)%MOD;
	}
	mem[pos][num]=ret;
	return ret;
}

void doit(){
	int ret=0;
	cin>>n;
	memset(mem,-1,sizeof(mem));
	for(int i=2;i<=n;i++){
		ret+=rec(1,i); 
		ret%=MOD;
	}
	cout<<ret<<endl;
}
int main(){
    int tc;
	cmbpopulate();
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}

