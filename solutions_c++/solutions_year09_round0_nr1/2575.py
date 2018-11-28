// Coder: Ad
#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<math.h>
#include<sstream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<list>
#include<deque>
#include<queue>
#include<numeric>
#define F(i,a,b) for(int i=a;i<b;++i)
#define FE(it,sto) for(typeof(sto.begin())it=sto.begin();it!=sto.end();++it)

#define pb push_back
#define all(x) x.begin(),x.end()
using namespace std;
int main(){
 int A[500][26];
 int L,D,N;
 cin>>L>>D>>N;
 string s;
 vector<string>v;
 F(i,0,D){cin>>s;s+="_",v.pb(s);}
 F(k,0,N){ 
    cin>>s;
    
    map<char,int>m;
    int ct=0;
    F(j,0,s.size())if(isalpha(s[j])&&m.find(s[j])==m.end())m[s[j]]=ct++;
    m['_']=ct;
    int q=0;
 	int i=0; 
   
 	memset(A,-1,sizeof A);
    while(i<s.size()){
    if(s[i]=='('){
  	i++;
  	while(i<s.size()&&s[i]!=')')
   	{A[q][m[s[i]]]=q+1;
    i++;
    }
  	q++; 
 	}
 	else{A[q][m[s[i]]]=q+1;
	      q++; 
        }
      i++;
    }
   A[q][m['_']]=ct+1;

 /*  F(i,0,q+1)
    {F(j,0,ct+1)
    cout<<A[i][j]<<" ";
    cout<<endl;
    }
*/
   //reconociendo
   int ad=0;
   F(i,0,D){
    string s=v[i];
    int j=0,q=0;
     while(q!=-1&&q!=ct+1)
     { if(m.find(s[j])==m.end())q=-1;
       else{
       q=A[q][m[s[j]]];
       j++;
      }
     }
    
    if(q==ct+1)ad++;
   }
  cout<<"Case #"<<k+1<<": "<<ad<<endl;
 }

}
