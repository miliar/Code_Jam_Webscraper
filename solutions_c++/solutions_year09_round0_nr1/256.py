#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)

bool tengo[16][32];

int main(){
	int i,j,c,L,D,N;
	
	cin>>L>>D>>N;
	vector<string> palabras(D);
	
	for (i=0;i<D;i++) cin>>palabras[i];
	for (c=0;c<N;c++){
		cout<<"Case #"<<c+1<<": ";
		
		memset(tengo,0,sizeof(tengo));
		string actual;
		cin>>actual;
		
		int pos=0;
		for (i=0;i<L;i++){
			if (actual[pos]=='('){
				pos++;
				while (actual[pos]!=')'){
					tengo[i][actual[pos]-'a']=true;
					pos++;
				}
			}else{
				tengo[i][actual[pos]-'a']=true;
			}
			pos++;
		}
		int ind,rta=0;
		for (j=0;j<(int)palabras.size();j++){
			for (ind=0;ind<L;ind++) if (!tengo[ind][palabras[j][ind]-'a']) break;
			if (ind==L) rta++;
		}
		cout<<rta<<endl;
	}
	
	return 0;
}
