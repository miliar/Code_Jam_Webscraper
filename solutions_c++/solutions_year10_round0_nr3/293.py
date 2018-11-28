#include<iostream>
#include<cassert>

using namespace std;

typedef unsigned long long Int;

#define REP(i, n) for(int i=0;i<n;i++)

int T, R;
Int k, n;
const int N=1010;
Int g[N];

Int ind[N];
Int euro[N];

void find_ind(){
	Int s=0;
	int j=0;
	Int num=0;
	for(int i=0;i<n;i++){
		while(1){
			if(s+g[j]<=k){
				num++;
				s+=g[j];
				j=(j+1)%n;
				if(j==i)break;
			}else{
				break;
			}
		}
		ind[i]=num;
		euro[i]=s;
		num--;
		s-=g[i];
	}
}

int sc[N];
Int esc[N];
bool shortcut=false;

Int find(){
	REP(i, N){
		sc[i]=-1;
	}
	Int i=0, e=0;
	//cout<<limit_ind<<endl;
	Int ii=0;
	REP(j, R){
		if(not shortcut){
			if(sc[i]==-1){
				sc[i]=j;esc[i]=e;
			}else{
				int start=sc[i];
				int jdiff=j-start;
				//				cout<<jdiff<<endl;
				Int ediff=e-esc[i];
				int num=(R-j)/jdiff;
				j+=num*jdiff;
				e+=(Int)num*ediff;
				shortcut=true;
				j--;
				continue;
			}
		}
		e+=euro[i];
		i+=ind[i];
		i%=n;
		ii+=ind[i];
	}
	return e;
}

int main(){
	cin>>T;
	REP(i, T){
		cin>>R>>k>>n;
		REP(j, n)
			cin>>g[j];
		find_ind();
		/*
		REP(j, n){
			cout<<ind[i]<<" ";
		}
		cout<<endl;
		*/
		/*
		   REP(j, n)
		   cout<<ind[j]<<" ";
		   cout<<endl;
		   */
		Int e=find();
		cout<<"Case #"<<i+1<<": "<<e<<endl;
//		printf("Case #%d: %lld\n", i+1, e);
	}
	return 0;
}
