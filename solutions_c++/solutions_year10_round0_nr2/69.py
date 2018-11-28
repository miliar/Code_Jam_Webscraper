#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
class INT{
  public:
  vector<char> a;
  char sign;
  int digit;
  INT& operator=(long long k);
  INT(long long k=0){
    *this=k;
  }
};
INT& INT::operator=(long long k){
  long long n=k;
  if (n<0) sign=1,n=-n;
  else sign=0;
  digit=0;
  a.resize(21);
  do{
    a[digit]=n%10;
    digit++;
    n/=10;
  }while(n);
  return *this;
}
int max(int x,int y) {return (x>y)?x:y;}
int min(int x,int y) {return (x<y)?x:y;}
INT add(const INT b1,const INT b2){//only plus
  INT b;
  b.sign=0;
  b.digit=max(b1.digit,b2.digit);
  b.a.resize(b.digit+1);
  int i,d=0,dmax=min(b1.digit,b2.digit);
  for (i=0;i<dmax;i++){
    b.a[i]=b1.a[i]+b2.a[i]+d;
    d=b.a[i]/10;
    b.a[i]%=10;
  }
  if (dmax==b1.digit){
    for (i=dmax;i<b2.digit;i++){
      b.a[i]=b2.a[i]+d;
      d=b.a[i]/10;  
      b.a[i]%=10; 
    }
  }
  if (dmax==b2.digit){
    for (i=dmax;i<b1.digit;i++){
      b.a[i]=b1.a[i]+d;
      d=b.a[i]/10;  
      b.a[i]%=10; 
    }
  }
  if (d){
    b.a[b.digit]=d;
    b.digit++;
  }
  return b;
}
INT sub(const INT b1,const INT b2){//only plus and b1>b2
  INT b;
  b.sign=0;
  b.digit=b1.digit;
  b.a.resize(b.digit);
  int i,d=0;
  for (i=0;i<b2.digit;i++){
    b.a[i]=b1.a[i]-b2.a[i]-d;
    if (b.a[i]<0){
      b.a[i]+=10;  d=1;
    }
    else d=0;
  }
  for (i=b2.digit;i<b1.digit;i++){
    b.a[i]=b1.a[i]-d;
    if (b.a[i]<0){
      b.a[i]+=10;  d=1;
    }
    else d=0;
  }
  for (i=b.digit-1;i>=0;i--)
    if (b.a[i]!=0) break;
  b.digit=i+1;
  return b;
}
INT operator *(const INT b1,const INT b2){//doesn't matter
  INT t,b;
  int i,j,d;
  b.sign=(b1.sign+b2.sign)%2;
  b.digit=b1.digit+b2.digit;
  b.a.resize(b.digit);
  t.a.resize(b.digit);
  for (i=0;i<b.digit;i++)
    b.a[i]=0;
  for (i=0;i<b2.digit;i++)
  if (b2.a[i]){
    d=0;
    for (j=0;j<b1.digit;j++){
      t.a[j]=(b1.a[j]*b2.a[i]+d);
      d=t.a[j]/10;
      t.a[j]%=10;
    }
    if (d){
      t.a[b1.digit]=d;
      t.digit=b1.digit+1;
    }
    else 
      t.digit=b1.digit;
    d=0;
    for (j=0;j<t.digit;j++){
      b.a[j+i]+=(t.a[j]+d);
      d=b.a[j+i]/10;
      b.a[j+i]%=10;
    }
    while (d){
      b.a[j+i]+=d;
      d=b.a[j+i]/10;
      b.a[j+i]%=10;
      j++;
    }
  }
  for (j=b.digit-1;j>=0;j--)
    if (b.a[j]) break;
  b.digit=j+1;
  return b;
}
INT operator %(const INT bi1,const INT bi2){ //doesn't matter
  INT b;
  INT b1=bi1, b2=bi2;
  if ((b2.digit==1&&b2.a[0]==0)||b2.digit==0){
    fprintf(stderr,"Division by 0!\n");
    b.sign=2;
    return b;
  }
  if (b2.digit>b1.digit){
    b=b1;
    return b;
  }
  b.sign=(b1.sign+b2.sign)%2;
  int i,j,nonstop=1,res=0,d;
  for (i=0;i<b1.digit/2;i++)
    swap(b1.a[i],b1.a[b1.digit-i-1]);
  for (i=0;i<b2.digit/2;i++)
    swap(b2.a[i],b2.a[b2.digit-i-1]);
  b.digit=b1.digit-b2.digit+1;
  b.a.resize(b.digit);
  for (i=0;i<b.digit;i++)
    b.a[i]=0;
  for (i=0;i<=b1.digit-b2.digit&&nonstop;i++){
    while (b1.a[i]&&nonstop){
      res=0;
      for (j=0;j<b2.digit;j++)
        if (b2.a[j]>b1.a[i+j]) {res=1; break;}
        else if (b2.a[j]<b1.a[i+j]) {res=-1; break;}
      if (res==0){
        for (j=0;j<b2.digit;j++)
          b1.a[i+j]=0;
        b.a[i]++;
      }
      else if (res==1){
        if (i+1+b2.digit>b1.digit){
          nonstop=0;
          break;
        }
        else{
          d=0;
          for (j=b2.digit-1;j>=0;j--){
            b1.a[i+j+1]-=(b2.a[j]+d);
            if (b1.a[i+j+1]<0){
              b1.a[i+j+1]+=10;
              d=1;
            }
            else d=0;
          }
          if (d) b1.a[i]--;
          b.a[i+1]++;
        }
      }
      else{
        d=0;
        for (j=b2.digit-1;j>=0;j--){
          b1.a[i+j]-=(b2.a[j]+d);
          if (b1.a[i+j]<0){
            d=1;
            b1.a[i+j]+=10;
          }
          else d=0;
        }
        b.a[i]++;
      }
    }//while
  }//for
  for (i=0;i<b.digit/2;i++)
    swap(b.a[i],b.a[b.digit-1-i]);
  for (i=0;i<b1.digit/2;i++)
    swap(b1.a[i],b1.a[b1.digit-i-1]);
  for (i=0;i<b2.digit/2;i++)
    swap(b2.a[i],b2.a[b2.digit-i-1]);
  for (i=b.digit-1;i>=0;i--)
    if (b.a[i]) break;
  b.digit=i+1;
  for (i=b1.digit-1;i>=0;i--)
    if (b1.a[i]) break;
  b1.digit=i+1;
  return b1;
}
INT operator /(const INT bi1,const INT bi2){ //doesn't matter
  INT b;
  INT b1=bi1, b2=bi2;
  if ((b2.digit==1&&b2.a [0]==0)||b2.digit==0){
    fprintf(stderr,"Division by 0!\n");
    b.sign=2;
    return b;
  }
  if (b2.digit>b1.digit){
    b.sign=0;
    b.digit=0;
    return b;
  }
  b.sign=(b1.sign+b2.sign)%2;
  int i,j,nonstop=1,res=0,d;
  for (i=0;i<b1.digit/2;i++)
    swap(b1.a[i],b1.a[b1.digit-i-1]);
  for (i=0;i<b2.digit/2;i++)
    swap(b2.a[i],b2.a[b2.digit-i-1]);
  b.digit=b1.digit-b2.digit+1;
  b.a.resize(b.digit);
  for (i=0;i<b.digit;i++)
    b.a[i]=0;
  for (i=0;i<=b1.digit-b2.digit&&nonstop;i++){
    while (b1.a[i]&&nonstop){
      res=0;
      for (j=0;j<b2.digit;j++)
        if (b2.a[j]>b1.a[i+j]) {res=1; break;}
        else if (b2.a[j]<b1.a[i+j]) {res=-1; break;}
      if (res==0){
        for (j=0;j<b2.digit;j++)
          b1.a[i+j]=0;
        b.a[i]++;
      }
      else if (res==1){
        if (i+1+b2.digit>b1.digit){
          nonstop=0;
          break;
        }
        else{
          d=0;
          for (j=b2.digit-1;j>=0;j--){
            b1.a[i+j+1]-=(b2.a[j]+d);
            if (b1.a[i+j+1]<0){
              b1.a[i+j+1]+=10;
              d=1;
            }
            else d=0;
          }
          if (d) b1.a[i]--;
          b.a[i+1]++;
        }
      }
      else{
        d=0;
        for (j=b2.digit-1;j>=0;j--){
          b1.a[i+j]-=(b2.a[j]+d);
          if (b1.a[i+j]<0){
            d=1;
            b1.a[i+j]+=10;
          }
          else d=0;
        }
        b.a[i]++;
      }
    }//while
  }//for
  for (i=0;i<b.digit/2;i++)
    swap(b.a[i],b.a[b.digit-1-i]);
  for (i=0;i<b1.digit/2;i++)
    swap(b1.a[i],b1.a[b1.digit-i-1]);
  for (i=0;i<b2.digit/2;i++)
    swap(b2.a[i],b2.a[b2.digit-i-1]);
  for (i=b.digit-1;i>=0;i--)
    if (b.a[i]) break;
  b.digit=i+1;
  return b;
}
bool operator ==(const INT b1,const INT b2){
  int i;
  if (b1.sign!=b2.sign) return false;
  if (b1.digit!=b2.digit) return false;
  else{
    for (i=b1.digit-1;i>=0;i--)
    if (b1.a[i]!=b2.a[i]) return false;
    return true;
  }
}
bool operator >(const INT b1,const INT b2){
  int i;
  if (b1.sign!=b2.sign){
    if (b1.sign==0) return true;
    else return false;
  }
  if (b1.digit<b2.digit){
    if (b1.sign==0) return false;
    else return true;
  }
  else if (b1.digit>b2.digit){
    if (b1.sign==0) return true;
    else return false;
  }
  else{
    for (i=b1.digit-1;i>=0;i--)
    if (b1.a[i]<b2.a[i]){
      if (b1.sign==0) return false;
      else return true;
    }
    else if (b1.a[i]>b2.a[i]){
      if (b1.sign==0) return true;
      else return false;
    }
    return false;
  }
}
bool operator <=(const INT b1,const INT b2){
  return !(b1>b2);
}
bool operator <(const INT b1,const INT b2){
  return (b2>b1);
}
bool operator >=(const INT b1,const INT b2){
  return !(b2>b1);
}
bool greater(const INT b1,const INT b2){
  int i;
  if (b1.digit!=b2.digit){
    return (b1.digit>b2.digit);
  }
  for (i=b1.digit-1;i>=0;i--)
  if (b1.a[i]!=b2.a[i]){
    return (b1.a[i]>b2.a[i]);
  }
  return false;
}
INT operator +(const INT b1,const INT b2){
  INT b;
  if (b1.sign==b2.sign){
    b=add(b1,b2);
    b.sign=b1.sign;
  }
  else{
    if (greater(b1,b2)){
      b=sub(b1,b2);
      b.sign=b1.sign;
    }
    else{
      b=sub(b2,b1);
      b.sign=b2.sign;
    }
    if ((b.digit==1&&b.a[0]==0)||b.digit<1){
      b.digit=1;
      b.sign=0;
      b.a[0]=0;
    }
  }
  return b;
}
INT operator -(INT b1,INT b2){
  INT b;
  char s1;
  if (b1.sign!=b2.sign){
    b=add(b1,b2);
    b.sign=b1.sign;
  }
  else{
    if (greater(b1,b2)){
      b=sub(b1,b2);
      b.sign=b1.sign;
    }
    else{
      b=sub(b2,b1);
      b.sign=1-b1.sign;
    }
    if ((b.digit==1&&b.a[0]==0)||b.digit<1){
      b.digit=1;
      b.sign=0;
      b.a[0]=0;
    }
  }
  return b;
}
INT convert(const char *buf){
  INT b;
  int i,l;
  l=strlen(buf)-1;
  if (buf [0]=='-') {b.sign=1; b.digit=l;}
  else {b.sign=0; b.digit=l+1;}
  b.a.resize(b.digit);
  for (i=l;i>=b.sign;i--)
    b.a[l-i]=buf[i]-'0';
  for (l=b.digit-1;l>=0;l--)
    if (b.a[l]) break;
  b.digit=l+1;
  return b;
}
void read(INT &b){
  char buf[10004];
  scanf("%s",buf);
  b=convert(buf);
}
void show(const INT b,char *s=NULL){
  int i;
  if (b.sign==2) { fprintf(stderr,"Error!\n"); return ;}
  if (b.sign&&b.digit) printf("-");
  if (b.digit==0) printf("0");
  for (i=b.digit-1;i>=0;i--)
    printf("%d",b.a[i]);
  if (s) printf("%s",s);
}
void shown(const INT b){
  show(b,"\n");
}

INT gcd(INT a,INT b){
	if ((b.digit==1&&b.a[0]==0)||b.digit==0) return a;
	while(1){
		a=a%b;
		if ((a.digit==1&&a.a[0]==0)||a.digit==0) return b;
		b=b%a;
		if ((b.digit==1&&b.a[0]==0)||b.digit==0) return a;
	}
}
int main(){
	INT c[1000],d,g;
	int t,T;
	int n,i;
	char s[100];
	scanf("%d",&T);
	for (t=1;t<=T;t++){
		printf("Case #%d: ",t);
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%s",s);
			c[i]=convert(s);
		}
		sort(c,c+n);
		d=c[0];
		for (i=0;i<n-1;i++)
			c[i]=c[i+1]-c[i];
		g=c[0];
		for (i=1;i<n-1;i++)
			g=gcd(g,c[i]);
		d=d%g;
		if ((d.digit==1&&d.a[0]==0)||d.digit==0) 	printf("0\n");
		else show(g-d,"\n");
	}
  return 0;
}
