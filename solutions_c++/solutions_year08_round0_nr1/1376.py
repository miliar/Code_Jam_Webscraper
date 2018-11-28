#include <iostream>
#include <vector>
#include <cassert>
#include <map>
#include <string>
#include <queue>
#define D 0
using namespace std;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef priority_queue<PII> PQPII;
typedef pair<int,PII> PIPII;
typedef priority_queue<PIPII , vector<PIPII>, greater<PIPII> > PQPIPII;
VI querry;
int ma;
void rek(int pos,int cnt,int s){
	if(cnt>ma) return; int akt=querry[pos];
	for(int i=0;i<s;i++){
		if(i==akt)continue; int ok=0; for(int j=pos+1;j<(int)querry.size();j++)
			if(querry[j]==i){ rek(j,cnt+1,s); ok=1; break; }
		if(!ok) ma=min(ma,cnt);	} }
int main(){
	int N;
	cin >> N;
	for(int ii=1;ii<=N;ii++){
		string t;
		int s,q,cnt=1<<29;
		cin >> s;
		MSI mymap;
		for(int i=0;i<s;i++){
			getline(cin,t);
			if(t.size()==0){
				i--;
				continue;
			}
			mymap[t]=i;
		}
		cin >> q;
		querry.clear();
		for(int i=0;i<q;i++){
			getline(cin,t);
			if(t.size()==0){
				i--;
				continue;
			}
			querry.push_back(mymap[t]);
		}
if(D)	for(int i=0;i<(int) querry.size();i++)
			fprintf(stderr,"q[%d]=%d\n",i,querry[i]);


		int pos=0;
		cnt=0;

		while(pos<(int)querry.size()){
			int found=0,np=-1;
			for(int i=0;i<s;i++){
if(D) 			cerr << "i: "<<i<<" " << pos << endl;			
				for(int j=pos,k=0;j<=(int)querry.size();j++,k++){
					if(j==(int)querry.size()){
						np=querry.size();
						break;
					}
					if(querry[j]==i){
if(D) 					cerr << i << " gefunden bei " <<j <<endl					;
						np=max(np,j);
						found=1;
						break;
					}
				}
				if(!found){
if(D) 				cerr << "i: " << i << " " << pos << " wurde nicht gefunden\n";
					np=querry.size();		
					break;
				}
			}
			pos=max(np,pos);
			cnt++;
		}
		cnt--;
		printf("Case #%d: %d\n",ii,max(cnt,0));
	}
	return 0;
}
