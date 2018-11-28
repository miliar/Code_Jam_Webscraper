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



void doit(){
	int n;
	double wp[101], owp[101], oowp[101];
	double iowp[101][101];
	double nopp[101], nwin[101];
	double nnum, nden,res;
	string inp;
	string in[101];
	cin>>n;
	//memset(iowp,0,sizeof(iowp));
	for(int i=0;i<n;i++)for(int j=0;j<n;j++)iowp[i][j]=0;
	for(int i=0;i<n;i++){
		cin>>inp;
		in[i]=inp;
		nopp[i]=nwin[i]=0;
		for(int j=0;j<n;j++)
		if(inp[j]!='.'){
			nopp[i]=nopp[i]+1;
			if(inp[j]=='1')nwin[i]=nwin[i]+1;
		}
		wp[i]=0;
		if(nopp[i]>0)wp[i]=nwin[i]/nopp[i];
		for(int j=0;j<n;j++)
		if(inp[j]!='.'){
			 nnum=nwin[i];nden=nopp[i]-1;
			 if(inp[j]=='1')nnum=nnum-1;
			 if(nden>0)iowp[i][j]=nnum/nden;
		}
	}
	for(int i=0;i<n;i++){
		owp[i]=0;
		nnum=0;nden=0;
		for(int j=0;j<n;j++)
		if(in[i][j]!='.'){
			nnum=nnum+iowp[j][i];
			nden=nden+1;
		}
		if(nden>0)owp[i]=nnum/nden;
	}
	cout<<endl;
	for(int i=0;i<n;i++){
		oowp[i]=0;
		nnum=0;nden=0;
		for(int j=0;j<n;j++)
		if(in[i][j]!='.'){
			nnum=nnum+owp[j];
			nden=nden+1;
		}
		if(nden>0)oowp[i]=nnum/nden;
		res= (wp[i] * 0.25) + (owp[i] * 0.5) + (oowp[i] * 0.25);
		printf("%0.12f\n",res);
		//cout<<res<<endl;
	}

	return;
}
int main(){
    int tc;
    cin>>tc;
    for(int i=1;i<=tc;i++){
        cout<<"Case #"<<i<<": ";
        doit();
    }
    return 0;
}

