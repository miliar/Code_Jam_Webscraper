#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0; i<(int)(n); i++)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
typedef vector<int> vi;
typedef long long int64;

#define AtoZ 26
#define MAX_IN 101

int main() {
	int T,C,D,N;
	short com[AtoZ][AtoZ];
	short del[AtoZ][AtoZ];
	short output[MAX_IN];
	short curr;
	char input[MAX_IN];
	cin>>T;
	for(int t=1;t<=T;t++){
		memset(com,-1,sizeof(short)*AtoZ*AtoZ);
		memset(del,-1,sizeof(short)*AtoZ*AtoZ);
		cin>>C;
		for(int c=0;c<C;c++){
			cin >> input;
			com[input[0]-'A'][input[1]-'A']=input[2];
			com[input[1]-'A'][input[0]-'A']=input[2];			
		}
		cin>>D;
		for(int d=0;d<D;d++){
			cin >> input;
			del[input[0]-'A'][input[1]-'A']=1;
			del[input[1]-'A'][input[0]-'A']=1;			
		}
		cin>>N;
		cin>>input;
		curr=0;
		for(int n=0;n<N;n++){
			if((curr>0)&&(com[output[curr-1]-'A'][input[n]-'A']>0)){					
				output[curr-1]=com[output[curr-1]-'A'][input[n]-'A'];
			}
			else{
				output[curr]=input[n];
				curr++;
			}			
			for(int i=curr-2;i>=0;i--){
				if(del[output[i]-'A'][output[curr-1]-'A']>0){
				  curr=0;
				  break;
				}
			}		
		}		
		cout<<"Case #"<<t<<": [";
		for(int i=0; i<curr; i++)
			cout<<(char)(output[i])<<(i+1==curr?"":", ");
		cout<<"]"<<endl;
	}
	return 0;
}
