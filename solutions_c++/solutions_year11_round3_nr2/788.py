#include<iostream>
using namespace std;
bool cx(long long a,long long b){
	return (a>b);
}
bool pr(long long remain[1001],long long c){
	//for(long long x=0;x<c;++x)
		////cout<<remain[x]<<' ';
	////cout<<endl;
}
int main(){
	long long T,l,t,n,c,ans;
	long long cs[1001],ct,remain[1001],total,*s[1001],q[1001];;
	bool ok;
	cin>>T;
	for(long long x=0;x<1001;++x)
		s[x] = new long long[2];
	for(long long x=1;x<=T;++x){
		cin>>l>>t>>n>>c;
		total=ct=0;
		for(long long i=0;i<c;++i){
			cin>>cs[i];
			/*ct+=cs[i];
			if(i<n%c){
				remain[i]=1;
				total+=remain[i];
			}
			else
				remain[i]=0;*/
		}
		total=0;
		int qc=0;
		for(int i=0;i<n;++i){
			if(total>=t){
				total+=cs[i%c]*2;
				//cout<<cs[i%c]<<endl;
				q[qc]=cs[i%c];
				qc++;
			}
			else{
				total+=cs[i%c]*2;
				if(total>t){
					q[qc]=(total-t)/2;
					qc++;
					//cout<<(total-t)/2<<endl;
				}
			}
		}
		sort(q,q+qc,cx);
		for(int i=0;i<l;++i){
			total-=q[i];
		}
			
		/*
		pr(remain,c);
		////cout<<"!!"<<n/c<<','<<t/ct<<endl;
		for(long long i=0;i<c;++i){
			remain[i] += n/c;
			remain[i] -= t/(ct*2);
		}
		pr(remain,c);
		total += ct*(n/c);
		////cout<<total<<endl;
		t=t%(ct*2);
		long long less=0;
		for(long long i=0;i<c;++i){
			////cout<<t<<"  "<<cs[i]<<"qq"<<endl;
			if(t>=2*cs[i]){
				remain[i]--;
				t -= 2*cs[i];
			}
			else if(t < 2*cs[i]){
				remain[i]--;
				less = (2*cs[i]-t)/2;
				break;
			}
			if(t==0)	break;
		}
		if(less){
			cs[c]=less;
			////cout<<"!!!!"<<less<<endl;
			remain[c]=1;
			c++;
		}
		for(long long i=0;i<c;++i){
			s[i][0]=i;
			s[i][1]=cs[i];
		}
		pr(remain,c);
		for(long long i=0;i<c;++i){
			cout<<s[i][1]<<' '<<s[i][0]<<':'<<remain[s[i][0]]<<endl;
		}
		sort(s,s+c,cx);
		for(long long i=0;i<c;++i){
			cout<<s[i][1]<<' '<<s[i][0]<<':'<<remain[s[i][0]]<<endl;
		}

		total*=2;
		for(long long i=c-1;i>=0;i--){
			if(remain[s[i][0]]==0)
				continue;
			if(remain[s[i][0]] < l){
				total -= s[i][1]*remain[s[i][0]];
				l -= remain[s[i][0]];
			}
			else if(remain[s[i][0]] >= l){
 				total -= s[i][1]*l;
				break;
			}
		}*/
		printf("Case #%lld: %lld\n",x,total);
	}
}
