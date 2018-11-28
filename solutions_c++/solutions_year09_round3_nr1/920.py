#include<iostream>
#include<cstring>
#include<cmath>

using namespace std;

#define FOR(i,N) for(int i=0; i<(N); ++i)

bool ispresent(char*,char,int);

int main()
  {

    char s[70];

    int T,c,cnt,K;
    
    int N[300];

    long long int ans;

    cin>>T;

    FOR(i,T)
      {
	cin>>s;
	
	cnt=0;
	FOR(j,strlen(s)) if(!ispresent(s,s[j],j)) cnt++;
	
	FOR(j,300) N[j]=-1;
	
	c=0;
	
	FOR(j,strlen(s))
	  {
	    if(N[s[j]]==-1) 
	      {
		N[s[j]]=c;
		c++;
		
		//cout<<s[j]<<' '<<N[s[j]]<<' '<<c<<'\n';
	      }
	  }
	
	
	
	ans=0;
	
	N[s[0]]=-1;

	K=strlen(s);

	if(cnt==1) cnt=2;
	
	//FOR(j,K) cout<<N[s[j]]; cout<<'|';

	if(cnt!=2)
	  {
    
	    FOR(j,300) if(N[j]==1) N[j]=0; else if(N[j]==-1) N[j]=1;
	    
	    FOR(j,strlen(s)) ans=ans+N[s[j]]*pow(cnt,K-j-1);
	  }
	
	else
	  {
	    FOR(j,300) N[j]=0;
	    N[s[0]]=1;
	    
	    FOR(j,strlen(s)) ans=ans+N[s[j]]*pow(cnt,K-j-1);
	  }


	//FOR(j,K) cout<<N[s[j]];
	cout<<"Case #"<<i+1<<": "<<ans<<'\n';
      }
    
    return(0);
  }

bool ispresent(char*s,char c,int j)
  {

    FOR(i,j)
      {
	if(s[i]==c)
	  return(true);
      }
    return(false);
  }
