#include<iostream>
#include<string>
typedef unsigned long long dt;
using namespace std;
const int N=52;
const int M=1000;
class HugeInt{
	int a[N],n;
public:
	HugeInt(){
		n=0;
	}
	void init(string s){
		n=s.size();
		for (int i=0;i<n;i++)
			a[i]=s[n-i-1]-'0';
	}
	friend ostream& operator<<(ostream& os,HugeInt b){
		for (int i=b.n-1;i>=0;i--)
			os<<b.a[i];
		return os;
	}
	bool operator<(HugeInt b){
		if (n!=b.n)
			return n<b.n;
		else{
			for (int i=n-1;i>=0;i--)
				if (a[i]!=b.a[i])
					return a[i]<b.a[i];
			return 0<0;
		}
	}
	friend HugeInt gcd(HugeInt a,HugeInt b){
		if (a.n==1 && a.a[0]==0)
			return b;
		if (b.n==1 && b.a[0]==0)
			return a;
		int i=0;
		while (1)
			if (a.a[0]%2==0 && b.a[0]%2==0){
				a.div2();b.div2();i++;
			}else if (a.a[0]%2==0)
				a.div2();
			else if (b.a[0]%2==0)
				b.div2();
			else if (a<b)
				b=b-a;
			else if (b<a)
				a=a-b;
			else{
				while (i)
					a.mul2(),i--;
				return a;
			}
	}
	void div2(){
		int j=0,k=0;
		for (int i=n-1;i>=0;i--){
			k=a[i]+j*10;
			a[i]=k/2;
			j=k%2;
		}
		if (a[n-1]==0 && n!=1)
			n--;
	}
	void mul2(){
		int j=0,k=0;
		for (int i=0;i<n;i++){
			k=a[i]*2+j;
			a[i]=k%10;
			j=k/10;
		}
		if (j!=0)
			a[n++]=j;
	}
	HugeInt operator-(HugeInt b){
		int j=0,k=0,l=b.n;
		if (l<n){
			for (int i=l;i<n;i++)
				b.a[i]=0;
			l=n;
		}else
			for (int i=n;i<l;i++)
				a[i]=0;
		for (int i=0;i<n;i++){
			k=a[i]-b.a[i]+j;
			if (k<0)
				b.a[i]=k+10,j=-1;
			else
				b.a[i]=k,j=0;
		}
		while (b.a[l-1]==0 && l!=1)
			l--;
		b.n=l;
		return b;
	}
	HugeInt operator%(HugeInt b){
		HugeInt result;
		result.init("0");
		for (int i=n-1;i>=0;i--){
			for (int j=result.n-1;j>=0;j--)
				result.a[j+1]=result.a[j];
			result.a[0]=a[i];
			result.n++;
			while (result.a[result.n-1]==0 && result.n!=1)
				result.n--;
			while (b<result)
				result=result-b;
		}
		return result;
	}
};
HugeInt c,a[M];
string s;
int n;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int Test;
	cin>>Test;
	for (int test=1;test<=Test;test++){
		cin>>n;
		for (int i=0;i<n;i++){
			cin>>s;
			a[i].init(s);
		}
		c.init("0");
		for (int i=0;i<n;i++)
			for (int j=0;j<i;j++)
				if (a[i]<a[j])
					c=gcd(c,a[j]-a[i]);
				else
					c=gcd(c,a[i]-a[j]);
		cout<<"Case #"<<test<<": "<<(c-a[0]%c)%c<<endl;
	}
	return 0;
}
