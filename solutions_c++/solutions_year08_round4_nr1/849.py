#include <stdio.h>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <stack>
#include <queue>

using namespace std;

#define S(t,z) scanf("%"#t,&z)
#define P(t,z) printf("%"#t,z)
#define PLN(t,z) printf("%"#t"\n",z)
#define PS(t,z) printf("%"#t" ",z)

#define Z(t,n) memset((t),(0),sizeof((t)[0])*(n))
#define MCP(d,s,n) memcpy((d),(s),sizeof((s)[0])*(n))

#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)

#define LL long long

using namespace std;

int i,j,x,w,v,k,m,n,c;
int CC;
LL res;
int vc[20000];
int vg[20000];
int vl[20000];
int ch[20000]; 
//priority_queue<int> PQ;
//queue<int>Q;
//stack<int>S;
int main(){
   int C;
   S(d,C);
   int CC=0;
   int V;
   int M;
   while (CC++,C--) {
   
     cin >> M >> V;
     int interior=((M-1)/2);
     
     REP(i,interior) {
        int c,g;
	cin >> c>> g;
        vc[i] = V?c:(1-c);
	vg[i] = (g);
     }
     
     int leafs= (M+1)/2;
     FOR(i,interior,interior+leafs-1) {
        int c;
	cin >> c;
        vl[i]= (V)?c:(1-c) ;
	//cout<<" leaf "<<vl[i];
     }	     
     
     REP(i,M) {
       ch[i]=-1;//impossible
     }
     
     FOR(i,interior,interior+leafs-1) {
        //cout<<" x " <<i<<"="<<vl[i]<<" ";
        if (vl[i])
	    ch[i] = 0;
     }	 
     //cout << endl;
     //cout <<" leafs : "<<leafs<<endl;
     //cout <<" int   : "<<interior<<endl; 
     
     for (int j = interior-1;j>=0;j--) {
       int childa = j*2 + 1;
       int childb = j*2 + 2;
       
       if (vc[j]) { //and
         if (ch[childa]>=0 && ch[childb]>=0) {
	   ch[j] = ch[childa] + ch[childb];
	 } 
	 if (vg[j]) {
	    int tmp = ch[j] ;
	    if (ch[childa] >= 0 && (ch[childa] +1 < tmp || tmp < 0)) 
		tmp = ch[childa];
		
	    if (ch[childb] >= 0 && (ch[childb] +1 < tmp || tmp < 0)) 
		tmp = ch[childb];
		
	    if (tmp >=0 && ((tmp +1) < ch[j] || ch[j] < 0 ))
		ch[j] = tmp + 1;     
	 }
	 
       } else {//OR
       
         //cout<<" or dla wezla "<<j<<" "<<childa<<" "<<ch[childa]<<" "<<childb<<" "<<ch[childb]<<endl;
         if (ch[childa] >= 0)
	    ch[j] = ch[childa];
	    
	 if (ch[childb] >= 0 && (ch[childb] < ch[j] || ch[j]<0))
	    ch[j] = ch[childb];
	 //cout<<" efekt  "<<ch[j]<<endl;
    
       }
     }
     
      //REP(i,M) {
    // 	cout << ch[i] <<" "<<vl[i]<<" "<<vc[i]<<endl;    
     //}

     
     if (ch[0]>=0)
       cout <<"Case #"<<CC<<": "<<ch[0]<<endl;
     else
       cout <<"Case #"<<CC<<": IMPOSSIBLE"<<endl;      
   }
    return 0;
}

