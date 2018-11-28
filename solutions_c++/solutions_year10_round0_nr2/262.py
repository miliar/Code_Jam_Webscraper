
#include<iostream>
#define MAXLEN 200
#define BASE_DIGIT 9
#define BASE 1000000000
#define IsDigit(c) (('0'<=(c))&&((c)<='9'))
#define PRINTCHAR ("%09d")
using namespace std;
char instr[MAXLEN*BASE_DIGIT+1];
short CMP(const int *a,const int *b){
	if(a[0]<b[0])
		return -1;
	if(a[0]>b[0])
		return 1;
	for(int i=a[0];i>0;i--)
	{
		if(a[i]<b[i])
			return -1;
		if(a[i]>b[i])
			return 1;
	}
	return 0;
}
void ADD(const int *a,const int *b,int *c){
	memset(c,0,sizeof(int)*MAXLEN);
	int la=a[0],lb=b[0],d=0;
	c[0]=(la>lb?la:lb)+1;
	for(int i=1;i<=c[0];i++)
	{
		c[i]= a[i]+b[i]+d;
		d=0;
		if(c[i]>=BASE)
		{
			d=1;
			c[i]-=BASE;
		}
	}
	while(c[0]>1&&c[c[0]]==0)
                             c[0]--;
}
void SUB(const int *a,const int *b,int *c){
	memset(c,0,sizeof(int)*MAXLEN);
	c[0]=a[0];
	int d=0;
	for(int i=1;i<=a[0];i++)
	{
		c[i]=a[i]-b[i]-d;
		d=0;
		if(c[i]<0)
		{
			c[i]+=BASE;
			d++;
		}
	}
	while(c[0]>1&&c[c[0]]==0)
		c[0]--;
	return ;
}
void MUL(const int *a,const int *b,int *c){
	memset(c,0,sizeof(int)*MAXLEN);
	__int64 t=0;
	int l = a[0]+b[0]+1;
	c[0]=l;
	for(int i=1;i<=a[0];i++)
		for(int j=1;j<=b[0];j++)
		{
			t=(__int64)c[i+j-1]+(__int64)a[i]*(__int64)b[j];
			c[i+j-1]=t%BASE;
			c[i+j] += t/BASE;
		}
	while(c[0]>1&&c[c[0]]==0)
		c[0]--;
}
void MUL(const int *a,int b,int *c){
	memset(c,0,sizeof(int)*MAXLEN);
	int l = a[0] + 1 ;
	long long t=0;
	for(int i=1;i<=l;i++)
	{
		t = (long long)a[i]*b + (long long)c[i];
		c[i+1] = t/BASE;
		c[i] = (t%BASE);
	}
	while(c[l]==0&&l>1) l--;
	c[0]=l;
}
void DIV(const int *a,const int *b,int *c,int *d){
		memset(c,0,sizeof(int)*MAXLEN);memset(d,0,sizeof(int)*MAXLEN);
		int *t1 = new int[MAXLEN],*t2 = new int[MAXLEN];
		int la=a[0],lb=b[0],ld=0,min=0,max=0,mid=0,l = la;
		double tdmin=0,tdmax=0,tbmin=b[lb],tbmax=tbmin+1.0;
		if(lb>1)
		{
			tbmin = tbmin*(double)BASE + (double)b[lb-1];
			tbmax = tbmin+1.0;
		}
		for(int i=l;i>0;i--)
		{
			for(int j=d[0];j>=1;j--)d[j+1]=d[j];d[1]=a[i];
			if(d[d[0]+1]!=0)d[0]++;
			if(CMP(d,b)<0)
				continue;
			ld = d[0];
			tdmin = d[ld];
			int j = 1;
			while(tdmin<tbmin)
			{
				tdmin = tdmin*BASE + d[ld-j];
				j++;
			}
			tdmax = tdmin+1.0;
			max =(int)(tdmax/tbmin)+1;min =(int)(tdmin/tbmax)-1;
			while(true)
			{
				mid = (min+max)/2;
				MUL(b,mid,t1);
				if(CMP(d,t1)<0){max = mid-1;continue;}
				SUB(d,t1,t2);
				if(CMP(t2,b)>=0){min = mid+1;continue;}
				break;
			}
			c[i]=mid;
			memcpy(d,t2,sizeof(int)*MAXLEN);
		}
		delete []t1;delete []t2;
		while(c[l]==0&&l>1) l--;
		c[0]=l;
}
class HarInt{/*�����������֧࣬�������������Ļ�������*/
private:
	int numb[MAXLEN];//�������֣���0λ��ʾ���ֳ��ȣ���һλ���Ժ�ֱ��ʾ���ֵĸ�λ����λ
	bool flag;
public:
	HarInt(){}/*Ĭ�Ϲ��캯��*/
	~HarInt(){}/*��������*/
	bool Parse(const char *s){/*��һ���ַ���ת��Ϊһ��������*/
		clear();int l=strlen(s),i=0,nl=1;flag = true;//Ĭ��Ϊ�Ǹ���
		if(s[0]=='-'){i++;flag = false;}//Ϊ��������ֵ�ӵ�2λ��ʼ
		for(int j=l-1;j>=i;j-=BASE_DIGIT)
		{//�Ӹ�λ����λһλһλת
			int n=0,ten=1;
			for(int k=0;(k<BASE_DIGIT&&j-k>=i);k++)
			{
				if(!IsDigit(s[j-k])){clear();return false;}//���������ַ�����ֵʧ��
				n+=(s[j-k]-'0')*ten;ten*=10;
			}
			numb[nl++]=n;//�ӵ�һλ��ʼ������numb��ֵ����0λԤ��Ϊ���ֳ�
		}
		nl--;while(numb[nl]==0&&nl>1)nl--;//��ȥǰ����
		numb[0]=nl;return true;//��ֵ�ɹ�
	}
	void clear(){memset(numb,0,sizeof(int)*MAXLEN);}/*��������λ��Ϊ��*/
	void Parse(const HarInt hi){
		memcpy(numb,hi.numb,sizeof(int)*MAXLEN);
		flag = hi.flag;
	}/*ͨ��һ��������֪����ֵ*/
	void value(const int a){
		int t=a;
		flag=true;if(t<0){flag=false;t*=-1;}
		numb[0]=1;numb[1]=t;
	}/*ͨ��һ����С����������ֵ*/
	int operator[](int i){return numb[i];}/*����[]�����ʵ�iλ����*/
	bool Flag(){return flag;}/*��ȡ��ǰ���ķ���*/
	bool isZero(){return (numb[0]==1&&numb[1]==0);}/*�Ƿ�Ϊ0*/
	int Get(){if(scanf("%s",instr)==EOF)return EOF;return Parse(instr);}/*�Զ������뺯��*/
	void print(char s){
		if(!flag)putchar('-');
		printf("%d",numb[numb[0]]);
		for(int i=numb[0]-1;i>=1;i--)
			printf(PRINTCHAR,numb[i]);
		putchar(s);
	}/*�Զ����������*/
	friend short HarIntCmp(HarInt,HarInt);//��Ԫ�ȽϺ���
	friend void DIV(HarInt,HarInt,HarInt&,HarInt&);//��Ԫ��������
	HarInt& operator+=(const HarInt& a){//����+=�������ʵ�ִ�������+=����
		int *n = new int[MAXLEN];
		memcpy(n,numb,sizeof(int)*MAXLEN);
		if(flag==a.flag)
			ADD(n,a.numb,numb);
		else{
			int c = CMP(n,a.numb);
			if(c==0){numb[0]=1;numb[1]=0;flag=true;}//|a|==|b|&&a*b<0��a-b=0;
			if(c<0){SUB(a.numb,n,numb);flag=a.flag;}//|a|<|b|
			else	SUB(n,a.numb,numb);
		}
		delete []n;n=NULL;
		return *this;
	}
	HarInt& operator-=(const HarInt& a){//����-=�������ʵ�ִ�������-=����
		int *n = new int[MAXLEN];
		memcpy(n,numb,sizeof(int)*MAXLEN);
		if(flag!=a.flag)
			ADD(n,a.numb,numb);
		else{
			int c = CMP(n,a.numb);
			if(c==0){numb[0]=1;numb[1]=0;flag=true;}
			if(c<0){SUB(a.numb,n,numb);flag=!flag;}
			else	SUB(n,a.numb,numb);
		}
		delete []n;n=NULL;
		return *this;
	}
	HarInt& operator*=(const HarInt& a){//����*=�������ʵ�ִ�������*=����
		int *n = new int[MAXLEN];
		memcpy(n,numb,sizeof(int)*MAXLEN);
		MUL(n,a.numb,numb);
		delete []n;n=NULL;
		flag = (flag==a.flag);
		return *this;
	}
	HarInt& operator/=(const HarInt& a){//����/=�������ʵ�ִ�������/=����
		int *n1 = new int[MAXLEN],*n2 = new int[MAXLEN];
		memcpy(n1,numb,sizeof(int)*MAXLEN);
		DIV(n1,a.numb,numb,n2);
		delete []n1;delete []n2;
		flag = (flag==a.flag);
		return *this;
	}
	HarInt& operator%=(const HarInt& a){//����%=�������ʵ�ִ�������%=����
		int *n1 = new int[MAXLEN],*n2 = new int[MAXLEN];
		memcpy(n1,numb,sizeof(int)*MAXLEN);
		DIV(n1,a.numb,n2,numb);
		delete []n1;delete []n2;
		flag = (flag==a.flag);
		return *this;
	}
};
void DIV(HarInt a,HarInt b,HarInt& c,HarInt& d){
	c.flag= (a.flag==b.flag);d.flag=c.flag;
	DIV(a.numb,b.numb,c.numb,d.numb);
	return ;
}
short HarIntCmp(HarInt a,HarInt b){
	if(a.Flag()>b.Flag())//��������ڸ���
		return 1;
	if(a.Flag()<b.Flag())//������С������
		return -1;
	if(a[0]<b[0])//��λ�ٵ���ֵС�����ݷ����жϴ�С
		return ((!a.Flag())?1:-1);
	if(a[0]>b[0])
		return (a.Flag()?1:-1);
	for(int i=a[0];i>=1;i--)
	{
		if(a[i]<b[i])
			return ((!a.Flag())?1:-1);
		if(a[i]>b[i])
			return (a.Flag()?1:-1);
	}
	return 0;
}
bool operator<(HarInt a,HarInt b){return (HarIntCmp(a,b)<0);}
bool operator>(HarInt a,HarInt b){return (HarIntCmp(a,b)>0);}
bool operator==(HarInt a,HarInt b){return (HarIntCmp(a,b)==0);}
bool operator!=(HarInt a,HarInt b){return (HarIntCmp(a,b)!=0);}
bool operator<=(HarInt a,HarInt b){return (HarIntCmp(a,b)<=0);}
bool operator>=(HarInt a,HarInt b){return (HarIntCmp(a,b)>=0);}
HarInt operator+(const HarInt& a,const HarInt& b){HarInt c=a;c+=b;return c;}
HarInt operator+(const HarInt& a,const int b){HarInt c;c.value(b);c+=a;return c;}
HarInt operator-(const HarInt& a,const HarInt& b){HarInt c=a;c-=b;return c;}
HarInt operator-(const HarInt& a,const int b){HarInt c;c.value(b);return (a-c);}
HarInt operator*(const HarInt& a,const HarInt& b){HarInt c=a;c*=b;return c;}
HarInt operator*(const HarInt& a,const int b){HarInt c;c.value(b);c*=a;return c;}
HarInt operator/(const HarInt& a,const HarInt& b){HarInt c=a;c/=b;return c;}
HarInt operator/(const HarInt& a,const int b){HarInt c;c.value(b);return (a/c);}
HarInt operator%(const HarInt& a,const HarInt& b){HarInt c=a;c%=b;return c;}
HarInt operator%(const HarInt& a,const int b){HarInt c;c.value(b);return (a%c);}
/*
int main()
{
	HarInt a,b,c,d;
	while(a.Get()>0&&b.Get())
	{
		DIV(a,b,c,d);
		c.print(' ');
		d.print('\n');
	}
	return 0;
}
*/

HarInt zero;
HarInt gcd(HarInt a,HarInt b)
{
    while(b != zero)
    {
        HarInt t;
        t=a%b;
        a=b;
        b=t;
    }
    return a;
}

HarInt num[1010];
HarInt delta[1000001];
HarInt T,y;
int sum_delta;                   
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    zero.value(0);
    int cas,cas_top;
    int n,i,j;
    HarInt temp;
    scanf("%d",&cas_top);
    for(cas=1;cas<=cas_top;cas++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            num[i].Get();
        }
        sum_delta=0;
        for(i=0;i<n;i++)
                for(j=i+1;j<n;j++)
                {
                    if(num[i]>num[j])
                        delta[sum_delta++]=num[i]-num[j];
                    else if(num[i]<num[j])
                        delta[sum_delta++]=num[j]-num[i];
                    
                }
       T=delta[0];
/*
printf("delta[0]\n");
delta[0].print('\n'); 
printf("T\n");
T.print('\n');
*/         
       for(i=1;i<sum_delta;i++)
       {
/*
printf("delta[%d]\n",i);
delta[i].print('\n'); 
printf("T\n");
T.print('\n'); 
*/
           T=gcd(T,delta[i]);
       }
       //T.print('\n');
       
       temp=num[0]%T;
       if(temp == zero)
       {
           cout<<"Case #"<<cas<<": "<<0<<endl;
       }
       else
       {
           y=T-temp;
           cout<<"Case #"<<cas<<": ";
           y.print('\n');
           
       }
       
    }
      return(0);
}



