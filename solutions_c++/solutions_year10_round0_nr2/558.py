#include <iostream>
#include <math.h>
#include <stdio.h>
using namespace std;
const int maxlen = 150;
class HP{
public:
	int len,s[maxlen]; HP(){(*this)=0;}
	HP(int inte) {(*this)=inte;} HP(const char*str){(*this)=str;}
	friend ostream& operator<<(ostream & cout,const HP & x);
	HP operator=(int inte);   HP operator=(const char *str);
	HP operator*(const HP&b);  HP operator+(const HP&b);
	HP operator-(const HP&b);  HP operator/(const HP&b);
	HP operator%(const HP&b);   int Compare(const HP&b);
};

ostream& operator<<(ostream&cout,const HP&x)
{ for(int i=x.len;i>=1;i--) cout<<x.s[i]; return cout; }

HP HP::operator=(const char *str)
{
	len=strlen(str);
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
HP events[1100];
char num[200];
HP gcd(HP x,HP y)
{
	if (y.Compare(HP("0")) == 0)
		return x;
	return gcd(y,x%y);
}
int main()
{
	int t,n;
	int cha;
	HP ans;
	HP t1,t2;
	HP temp;
	freopen("B-large.in","r",stdin);
	freopen("pro.out","w",stdout);
	scanf("%d",&t);
	int i,j;
	for (i = 1;i <= t;i++)
	{
		scanf("%d",&n);
		for (j = 1;j <= n;j++)
		{
			scanf("%s",&num);
			events[j] = HP(num);
		}
		cha = events[1].Compare(events[2]);
		if (cha > 0)
			t1 = events[1]-events[2];
		else
			t1 = events[2]-events[1];

		for (j = 2;j < n;j++)
		{			
			cha = events[j].Compare(events[j+1]);
			if (cha > 0)
				t2 = events[j]-events[j+1];
			else
				t2 = events[j+1]-events[j];
			cha = t1.Compare(t2);
			if (cha > 0)
			{
				t1 = gcd(t1,t2);
			}
			else
				t1 = gcd(t2,t1);
		}
		temp = t1-(events[1]-1)%t1-1;
		
		printf("Case #%d: ",i);
		cout << temp << endl;

	}		
}