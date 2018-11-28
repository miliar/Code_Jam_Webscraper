//Author  :   MAK(Kader)
//Problem no:  
//Title:  Cse DU

#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cctype>
#include<iostream>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;
//-------------------------------------------------------
typedef pair<int,int> ii;
typedef vector<int> vi;
#define pb push_back
#define sz(c) (c).size()
#define all(c) (c).begin(),(c).end()
#define vtr(c,i) for(vi::iterator i=c.begin();i!=c.end();i++)
#define INF  (1<<30)
#define EPS  1e-8
#define SET(NAME)   (memset(NAME,-1,sizeof(NAME)))
#define CLR(NAME)   (memset(NAME,0,sizeof(NAME)))
#define max(a,b) ((a)>(b)?(a):(b))

//--------------------------------------------------------
void reset(){}
char Tree[80000];
set<string> feat;

bool isLeaf(int i){

	int k;
	for(k=i;;k++)
	if(isalpha(Tree[k]))
		return false;
	else if(Tree[k]==')')
		return true;
}
int FRP(int i){

	int k;

	stack<char> st;
	for(k=i;;k++)
		if(Tree[k]=='(')
			st.push('(');
		else if(Tree[k]==')'){
		
			st.pop();
			if(st.empty())
				return k;
		}
	return 0;

}
int FLP(int i){

	stack<char> st;
	int k;
	for(k=i;;k--)
	if(Tree[k]==')')	
		st.push(')');
	else if(Tree[k]=='(')
	{
	
		st.pop();
		if(st.empty())
			return k;
	
	}

	return 0;

}
bool isLeft(int i){

	int j;
	for(j=i;!isalpha(Tree[j]);j++)
		;
	char str[1000];
	sscanf(&Tree[j],"%s",str);

	string tmp=str;
	if(feat.find(tmp)==feat.end())
		return false;
	return true;

}
double fun(int i,int j){

	
	double p;
	int k;
	sscanf(&Tree[i+1],"%lf",&p);
	if(isLeaf(i+1))	
		return p;
	
	if(isLeft(i+1)){
	
		for(k=i+1;Tree[k]!='(';k++)
			;

		int rp=FRP(i+1);
		return p*fun(k,rp);	
	}
	
	{
		for(k=j-1;Tree[k]!=')';k--)
			;
		int lp=FLP(j-1);
		
		return p*fun(lp,k);
	
	}
	
}
void process(){


	int i,j;
	for(i=0;Tree[i]!='(';i++)
		;
	for(j=strlen(Tree)-1;Tree[j]!=')';j--)
		;
		
	printf("%.7lf\n",EPS+fun(i,j));

}

int main()
{
	freopen("contest/A-small-attempt0.in","rt",stdin);
	freopen("contest/out.txt","w",stdout);

	char str[1000];
	int L,t,A,nf,cas=1;
	
	gets(str);
	sscanf(str,"%d",&t);
	while(t--){
	
		Tree[0]=NULL;

		gets(str);
		sscanf(str,"%d",&L);
		while(L--){
			gets(str);
			strcat(Tree,str);
		}
		gets(str);
		sscanf(str,"%d",&A);


		printf("Case #%d:\n",cas++);
		while(A--){

				scanf("%s%d",&str,&nf);//name
				feat.clear();
				while(nf--){
				
					scanf("%s",str);
					string tmp=str;
					feat.insert(tmp);
				}

				
				process();
		}
		gets(str);
	
	}	
	return 0;
}
