// gcj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<cstdio>
#include<string>
#include<vector>
#include<map>
using namespace std;
#define REP(i,n) for(__int64 i=0;i<(__int64)(n);++i)
char x[26];
__int64 pow(__int64 a,int b) {
__int64 rval=1;
REP(i,b) rval*=a;
return rval;
}
__int64 packstring(string s) {
	__int64 rval=0;
	REP(i,s.size()) {
		__int64 msk=x[(int)s[i]-'a']-'a'+1;
		if(x[(int)s[i]-'a']=='_') msk=28;
		rval|=msk*pow(2,(5*i));
	}
	return rval;
}
vector<string> words;
typedef map<__int64,vector<int> > TT;
TT mp;
string w;
int _tmain(int argc, _TCHAR* argv[])
{
     int t=0;
	 scanf("%d",&t);
	 for(int xx=1;xx<=t;++xx) {
		 int n,m;
		 scanf("%d %d",&n,&m);
		 printf("Case #%d:",xx);
		 words=vector<string>();
		 char p[100];
		 REP(i,n) {
			 scanf("%s",p);
			 words.push_back(p);
		 }
		 REP(i,m) {
			 scanf("%s",p);
			 int best=0;
			 int best_score=0;
			 mp=TT();
			 
			 REP(j,26) x[j]='_';
			 REP(j,n) {
				 mp[packstring(words[j])].push_back(j);
			 }
			 REP(j,26) {
				 //iterate map
				 TT m2;
				 x[(int)p[j]-'a']=p[j];
				 //printf("letter:%c\n",p[j]);
				 for(TT::iterator it=mp.begin();it!=mp.end();++it) {
				//	 printf("kks=%d %lld\n",it->second.size(),it->first);
					 if(it->second.size()>1) {
						 int ma=0;
						 REP(k,it->second.size()) {
							 int wd=it->second[k];
							 if(words[wd].find(p[j])!=string::npos) {
								 ma=1;
							 }
						 }
						
						 REP(k,it->second.size()) {
							 int wd=it->second[k];
							 int score= it->first/pow(2,55);
							 int new_score=score;
							 if(words[wd].find(p[j])==string::npos) {
								 new_score+=ma;
							 } 
							 __int64 hash=packstring(words[wd]);
							 m2[hash | (new_score*pow(2,55))].push_back(wd);
				//			 printf("dbg: %s,%d\n",words[wd].c_str(),new_score);
							 if(new_score>best_score || (new_score==best_score && best>wd)) {
							   best_score=new_score;
							   best=wd;
							 }
						 }

					 }

				 }
				 mp=TT(m2);
			 }
			 printf(" %s",words[best].c_str(),best_score);
		 }
		 printf("\n");


	 }
	return 0;
}

