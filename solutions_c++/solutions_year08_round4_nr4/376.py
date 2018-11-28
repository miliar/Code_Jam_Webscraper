#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<string>

using namespace std;
#define MAXK 20 
int size(string pS){}
int main(){
	int k; string S;
	int p[MAXK];
	int N; cin >> N;
	for(int t=1; t<=N; t++){
		cin >> k >> S;
		for(int i=0; i<k; i++)
			p[i]=i;
		int res=S.size()+1;
		do{
			string pS="";
			for(int i=0; i<S.size(); i+=k)
				for(int j=0; j<k; j++)
					pS+=S[i+p[j]];
			int sz=1;
			for(int i=1; i<pS.size(); i++)
				if(pS[i]!=pS[i-1])sz++;
			res = min(sz,res);
		}while(next_permutation(p,p+k));
		cout << "Case #" << t << ": " << res << "\n";
	}
}
