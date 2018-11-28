//#include<iostream>
//using namespace std;
//
//int num[10],n;
//
//void toDec ( int v )
//{
//	memset(num,0,sizeof(num));
//	while ( v)
//	{
//		num[v%10]++;
//		v/=10;
//	}
//}
//bool check ( int v )
//{
//	int i,buf[10];
//	for (  i=0 ; i<10 ; i++ )
//		buf[i]=num[i];
//	while ( v )
//	{
//		buf[v%10]--;
//		if ( buf[v%10]<0 && v%10 )
//			return false;
//		v/=10;
//	}
//	for ( i=1 ; i<10 ; i++ )
//		if(  buf[i] )
//			return false;
//	return true;
//}
//
//int main ()
//{
//	int cas,a,k;
//	freopen("B-small-attempt0.in","r",stdin);
//	freopen("out.txt","w",stdout);
//	scanf("%d",&cas);
//	for ( k=1 ; k<=cas; k++ )
//	{
//		int i;
//		scanf("%d",&a);
//		toDec(a);
//		for ( i=a+1 ; ; i++ )
//		{
//			if ( check(i)  )
//			{
//				
//				break;
//			}
//
//		}
//		printf("Case #%d: %d\n",k,i);
//
//	}
//
//}
#include<iostream>
#include<string>
#include<sstream>
#include<map>
using namespace std;

#define MAXN 10000

struct NODE
{
	string cha;
	double p;
	NODE *left,*right;
	NODE()
	{
		left=right=NULL;
		cha="";
		p=0;
	}
};
NODE* root;
int L,A,N;

int B[MAXN];
map<string,int> look;
string str;

struct leftb
{
	int s,t;
};

NODE* build ( int s , int t )
{
	int j,i,tag=0,f=0,k;
	NODE* v=new NODE;
	string buf=str.substr(s,t-s+1),temp;
	for ( i=s+1 ; i<=t-1 ; i++ )
	{
		if ( str[i]==' ' )
			continue;
		if ( isdigit(str[i]) )
		{
			for ( j=i+1 ; j<=t ; j++)
			{
				if(  str[j]=='.' || isdigit(str[j]) )
					continue;
				break;
			}
			
			if ( str[j]==')' )
			{
				istringstream in1(str.substr(i,j-i));
				in1>>v->p;
				i=j;
			}
			else
				if ( str[j]==' ' )
				{
					istringstream in2(temp=str.substr(i,j-i));
					double tt;
					in2>>tt;
					v->p=tt;
					for ( k=j+1 ; k<=t && islower(str[k]) ; k++ );
					v->cha=temp=str.substr(j+1,k-j-1);
					i=k;
					
				}
		}
		else
		{
			if ( str[i]=='(' )
			{
				if(  tag==0 )
				{
					tag=1;
					v->left=build(i,B[i]);
					i=B[i];
				}
				else
				{
					v->right=build(i,B[i]);
					i=B[i];
				}
			}
		}
	}
	return v;
}

void read ( )
{
	string buf;
	str="";
	for (int i=0 ; i<L ; i++ )
	{
		getline(cin,buf);
		str+=buf;
	}
}

void makeb ( )
{
	leftb st[MAXN];
	int top=0,i;
	for ( i=0 ; i<str.size() ; i++ )
	{
		if ( str[i]=='(' )
		{
			st[top].s=i;
			top++;
		}
		else
			if ( str[i]==')' )
			{
				st[top-1].t=i;
				B[st[top-1].s]=i;
				top--;
			}
	}
}

double search ( NODE* v )
{
	if ( v==NULL )
		return 1;
	if ( v->cha=="" )
	{
		return v->p;
	}
	if ( look.find(v->cha)!=look.end() )
	{
		return v->p*search(v->left);
	}
	else
		return v->p*search(v->right);
}

double solve ( )
{
	look.clear();
	string ani,cha[MAXN] ;
	int n,i;
	cin>>ani>>n;
	for ( i=0 ; i<n ; i++ )
	{
		cin>>cha[i];
		look[cha[i]]=1;
	}
	double res=1;
	if ( look.find(root->left->cha)!=look.end() ||root->right==NULL)
	{
		res=search(root->left);
	}
	else
		res=search(root->right);
	return res;


}

int main ( )
{
	int cas,k,i;
		freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&cas);
	for ( k=1 ; k<=cas ; k++ )
	{
		printf("Case #%d:\n",k);
		scanf("%d",&L);
		getchar();
		read();
		makeb();
		int tag=0;
		root=new NODE;
		for ( i=0 ; i<str.size() ; i++ )
		{
			if ( str[i]=='(' )
			{
				if ( tag==0 )
				{
					tag=1;
					root->left=build(i,B[i]);
					i=B[i];
				}
				else
				{
					root->right=build(i,B[i]);
				}
			}
		}
		scanf("%d",&N);
		for ( i=0 ; i<N ; i++ )
		{
			double	res=solve();
			printf("%.7lf\n",res);
		}

	}
}