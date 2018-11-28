#include<iostream>
#include<string>
using namespace std;

const int maxlen=100;
class HP{
public:
	int len,s[maxlen]; HP(){(*this)=0;}
	HP(int inte) {(*this)=inte;} HP(const string str){(*this)=str;}
	HP operator=(int inte);   HP operator=(const string str);
	HP operator*(const HP&b);  HP operator+(const HP&b);
	HP operator-(const HP&b);  HP operator/(const HP&b);
	HP operator%(const HP&b);   int Compare(const HP&b);
};

HP HP::operator=(const string str)
{
	len=str.length();
	for(int i=1;i<=len;i++) s[i]=str[len-i]-'0';
	return *this;
}

HP HP::operator=(int inte)
{
	if(inte==0) { len=1;s[1]=0; return (*this);};
	for(len=0;inte>0;)
	{
		s[++len]=inte%10;
		inte/=10;
	}
	return (*this);
}

HP HP::operator*(const HP &b)
{
	int i,j; HP c; c.len=len+b.len;
	for(i=1;i<=c.len;i++) c.s[i]=0;
	for(i=1;i<=len;i++)
		for(j=1;j<=b.len;j++)
			c.s[i+j-1]+=s[i]*b.s[j];
		for(i=1;i<c.len;i++)
		{
			c.s[i+1]+=c.s[i]/10;
			c.s[i]%=10;
		}
		while(c.s[i]) { c.s[i+1]=c.s[i]/10; c.s[i]%=10;i++;}
		while(i>1&&!c.s[i]) i--;
		c.len=i;
		return c;
}

HP HP::operator+(const HP&b)
{
	int i; HP c; c.s[1]=0;
	for(i=1;i<=len || i<=b.len || c.s[i]; i++)
	{
		if(i<=len) c.s[i]+=s[i];
		if(i<=b.len) c.s[i]+=b.s[i];
		c.s[i+1]=c.s[i]/10;
		c.s[i]%=10;
	}
	c.len=i-1;
	if(c.len==0) c.len=1;
	return c;
}

HP HP::operator-(const HP&b)
{
	int i,j; HP c;
	for(i=1,j=0; i<=len ;i++){
		c.s[i]=s[i]-j; if(i<=b.len) c.s[i]-=b.s[i];
		if(c.s[i]<0)
		{
			j=1; c.s[i]+=10; 
		}
		else j=0;
	}
	c.len=len ; while(c.len>1&&!c.s[c.len]) c.len--;
	return c;
}

int HP::Compare(const HP&y)
{
	if(len>y.len) return 1;
	if(len<y.len) return -1;
	int i=len;
	while((i>1)&&(s[i]==y.s[i])) i--;
	return s[i]-y.s[i];
}

HP HP::operator/(const HP&b)
{
	int i,j; HP d(0),c;
	for(i=len;i>0;i--){
		if(!(d.len==1&&d.s[1]==0))
		{
			for(j=d.len;j>0;j--)
				d.s[j+1]=d.s[j];
			++d.len;
		}
		d.s[1]=s[i];
		c.s[i]=0;
		while( (j=d.Compare(b))>=0)
		{ d=d-b; c.s[i]++; if(j==0) break; }
	}
	c.len=len; while((c.len>1)&&(c.s[c.len]==0)) c.len--;
	return c;
}

HP HP::operator%(const HP &b)
{
	int i,j; HP d(0);
	for(i=len;i>0;i--){
		if(!(d.len==1&&d.s[1]==0))
		{
			for(j=d.len;j>0;j--)
				d.s[j+1]=d.s[j];
			++d.len;
		}
		d.s[1]=s[i];
		while((j=d.Compare(b))>=0)
		{
			d=d-b;
			if(j==0)break;
		}
		}
	return d;
}
HP zero=0;
HP gcd(HP a,HP b)                     
{ 
	if(a.Compare(zero)==0)
		return b;
	HP t;
	while(b.Compare(zero)!=0)
	{
		t=a%b;
		a=b;
		b=t;
	}
	return a;
}
void quicksort(int b,int e,HP a[])
{
	int i=b,j=e;
	HP x=a[(b+e)/2];
	do
	{
		while(a[i].Compare(x)<0) i++;
		while(a[j].Compare(x)>0) j--;
		if(i<=j) std::swap(a[i++],a[j--]);
	}while(i<j);
	if(i<e) quicksort(i,e,a);
	if(j>b) quicksort(b,j,a);
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
	int T;
	cin>>T;
	int j;
	for(j=1;j<=T;j++)
	{
		int n;
		cin>>n;
		int i;
		HP a[1001];
		string str;
		for(i=0;i<n;i++)
		{
			cin>>str;
			a[i]=str;
		}
		if(n==1)
		{
			cout<<"Case #"<<j<<": "<<0<<endl;
			continue;
		}
		quicksort(0,n-1,a);
		HP b[1001];
		for(i=1;i<n;i++)
			b[i-1]=a[i]-a[i-1];
		HP ans=b[0];
		for(i=1;i<n-1;i++)
			ans=gcd(ans,b[i]);
		if(ans.Compare(zero)==0)
		{
			cout<<"Case #"<<j<<": "<<0<<endl;
			continue;
		}
		if((a[0]%ans).Compare(zero)!=0)
		{
		cout<<"Case #"<<j<<": ";
		HP temp=ans-a[0]%ans;
		for(i=temp.len;i>0;i--)
			cout<<temp.s[i];
		cout<<endl;
		}
		else
		cout<<"Case #"<<j<<": "<<0<<endl;
	}
//	system("pause");
	return 0;
}
