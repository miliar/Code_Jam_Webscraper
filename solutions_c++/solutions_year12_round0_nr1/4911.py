#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <map>  
#include <string>
#include <vector> 
#include <list>
#include <iostream>  
#include <sstream> 
#include <queue>
#include <algorithm>

using namespace std; 
 
#define PB 		push_back
#define FOR(a,start,end) 	for(int a=int(start); a<int(end); a++)
#define INF 		INT_MAX
#define SORT(a) 	sort(a.begin(),a.end())
#define CL(a,x) 		memset(a,x,sizeof(a))
#define REP(a,x)	for(int a=0;a<x;a++)
#define REP1(a,x)	for(int a=1;a<=x;a++)
#define MP 		make_pair

typedef long long 	ll;
typedef vector<int> 	vi;
typedef pair<int,int> 	pii;
typedef vector<pair<int,int> >	vpii;

long amax,i,k,i2,i1,r,k1,j,m,l,n,i3,j10,j2,j3,a1,a2,a3; 
long cas,c,a,k2,z,t,ng,b,p,s;
pair<long,long> p2;
long ta[200];
vector<pair<long,long> > vp;
vector<long> va,vk1,vk2,vk3;
vector<vector<int> > vb;
vi vk,vh,vr;
double pi,dx,ax;
string w1="ejp mysljylc kd kxveddknmc re jsicpdrysi",w2="our language is impossible to understand";
string w3 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", w4 = "there are twenty six factorial possibilities";
string w5 = "de kr kd eoya kw aej tysr re ujdr lkgc jv", w6 = "so it is okay if you want to just give up";
string w,wx;
char ww[1000],ch;
int main() { 
	//freopen( "c:\\wojtek\\uva\\uva\\debug\\t1.in", "rt", stdin); 
	//	int czas=clock(); 
	pi=2*acos(0.0);
	 
	
	//scanf("%ld",&t);
	cin>>t; 
	CL(ta,0);

	k=w1.size();
	for(i=0;i<k;i++){
		if(w1[i]!=' '){
			ta[w1[i]-'a']=w2[i]-'a';
		}
	}
	k=w3.size();
	for(i=0;i<k;i++){
		if(w3[i]!=' '){
			ta[w3[i]-'a']=w4[i]-'a';
		}
	}
	k=w5.size();
	for(i=0;i<k;i++){
		if(w5[i]!=' '){
			ta[w5[i]-'a']=w6[i]-'a';
		}
	}
	ta['q'-'a']='z'-'a';
	ta['z'-'a']='q'-'a';

	scanf("%c",&ch);

	for(cas=1;cas<=t;cas++){  
		wx.clear();
		//cin>>w;
		w.clear();
		scanf("%c",&ch);

		while(ch!='\n'){
			w+=ch;
			scanf("%c",&ch);
		}
		k=w.size();
		for(i=0;i<k;i++){
			if(w[i]!=' '){
				wx+=ta[w[i]-'a']+'a';
			}
			else
				wx+=' ';
		}
		cout<<"Case #"<<cas<<": "<<wx<<endl;
	}



//	czas = clock() - czas;
//	printf("%lf\n",double(czas)/CLOCKS_PER_SEC);					

			
	return 0;

} 
