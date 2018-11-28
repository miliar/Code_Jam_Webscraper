#include<iostream>
#include<algorithm>
using namespace std;

long long int k,m,*sk,*tk,*sm,*tmz;

long long int big(long long int a,long long int b){
	if(a>b)
		return a;
	else
		return b;
}

long long int find(long long int fk,long long int uk,long long int fm,long long int um){
	if(fk==k||fm==m)
		return 0;
	else{
		if(tk[fk]==tmz[fm]){
			if(sk[fk]-uk>sm[fm]-um)
				return find(fk,uk+sm[fm]-um,fm+1,0)+sm[fm]-um;
			else if(sk[fk]-uk<sm[fm]-um)
				return find(fk+1,0,fm,um+sk[fk]-uk)+sk[fk]-uk;
			else
				return find(fk+1,0,fm+1,0)+sm[fm]-um;
		}
		else
			return big(find(fk,uk,fm+1,0),find(fk+1,0,fm,um));
	}
}

int main(){
	int t,counter,b;
	cin>>t;
	for(counter=1;counter<=t;++counter){
		cin>>k>>m;
		sk=new long long int[k];
		tk=new long long int[k];
		sm=new long long int[m];
		tmz=new long long int[m];
		for(b=0;b<k;++b)
			cin>>sk[b]>>tk[b];
		for(b=0;b<m;++b)
			cin>>sm[b]>>tmz[b];
		cout<<"Case #"<<counter<<": "<<find(0,0,0,0)<<endl;
	}
	return 0;
}
