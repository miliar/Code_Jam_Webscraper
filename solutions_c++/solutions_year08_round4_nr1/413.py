#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <utility>
#include <algorithm>

using namespace std;
#define MAXV 10011
bool inp[MAXV]; //1=and 0=or
bool chg[MAXV];
bool res[MAXV];
int cnt[MAXV][2];
int m,op,bl;
bool v;
int rec(int inx,bool val){ //val=required value
	//cout<<inx<<" "<<val<<endl;
	if(inx>=op+bl)return 0;
	if(inx>=op){
		if(val==res[inx]) return 0;
		else return MAXV;
	}
	int &ret=cnt[inx][val];
	if(ret!=-1)return ret;
	ret=MAXV;
	if(res[inx]==val){ ret=0;return ret;}  //required value equals result
	if(val){  //required value is 1
		if(inp[inx]){ //and operator
			ret=min(ret,rec(2*inx+1,true)+rec(2*inx+1+1,true));	
			if(chg[inx]){
				ret=min(ret,1+rec(2*inx+1,true)+rec(2*inx+1+1,false));
				ret=min(ret,1+rec(2*inx+1,false)+rec(2*inx+1+1,true));
				ret=min(ret,1+rec(2*inx+1,true)+rec(2*inx+1+1,true));
			}
		}
		else { //or operator
			ret=min(ret,rec(2*inx+1,true)+rec(2*inx+1+1,false));
			ret=min(ret,rec(2*inx+1,false)+rec(2*inx+1+1,true));
			ret=min(ret,rec(2*inx+1,true)+rec(2*inx+1+1,true));
			if(chg[inx]){
				ret=min(ret,1+rec(2*inx+1,true)+rec(2*inx+1+1,true));
			}
		}
	}
	else{ //required value is 0
		if(inp[inx]){ //and operator
			ret=min(ret,rec(2*inx+1,true)+rec(2*inx+1+1,false));
			ret=min(ret,rec(2*inx+1,false)+rec(2*inx+1+1,true));
			ret=min(ret,rec(2*inx+1,false)+rec(2*inx+1+1,false));
			if(chg[inx]){
				ret=min(ret,1+rec(2*inx+1,false)+rec(2*inx+1+1,false));
			}
		}
		else{  //or operator
			ret=min(ret,rec(2*inx+1,false)+rec(2*inx+1+1,false));
			if(chg[inx]){
				ret=min(ret,1+rec(2*inx+1,true)+rec(2*inx+1+1,false));
				ret=min(ret,1+rec(2*inx+1,false)+rec(2*inx+1+1,true));
				ret=min(ret,1+rec(2*inx+1,false)+rec(2*inx+1+1,false));
			}
		}
	}
	//cout<<" "<<inx<<" "<<val<<" "<<ret<<endl;
	return ret;

}

int main(){
	int t,ret;
	cin>>t;
	for(int tc=1;tc<=t;tc++){
		memset(inp,0,sizeof(inp));
		memset(res,0,sizeof(res));
		memset(chg,0,sizeof(chg));
		memset(cnt,-1,sizeof(cnt));
		m=op=bl=0;
		cin>>m>>v;
		op=(m-1)/2;
		bl=(m+1)/2;
		//cout<<op<<" "<<bl<<endl;
		for(int i=0;i<op;i++)
			cin>>inp[i]>>chg[i];
		//cout<<"read ops"<<endl;
		for(int i=op;i<bl+op;i++){
			cin>>inp[i];
			res[i]=inp[i];
		}
		for(int i=op-1;i>=0;i--){
			if(inp[i]) //and
				res[i]=res[i*2+1]&res[i*2+2];
			else
				res[i]=res[i*2+1]|res[i*2+2];
		}
		//for(int i=0;i<m;i++)cout<<res[i]<<" ";
		//cout<<endl;
		ret=rec(0,v);
		if(ret>=MAXV)printf("Case #%d: IMPOSSIBLE\n",tc);
		else printf("Case #%d: %d\n",tc,ret);
		//cout<<"Case #"<<tc<<": "<<res<<endl;
	}
	return 0;
}


