#include<iostream>
#include<cstring>
using namespace std;
typedef unsigned int bitmap[160];

int n,d,l,i,j,k;
bitmap a[20][26],all,part;
char s[1000];

void addString(int i)
{
	int x,y,j;
	x = (i-1)>>5;
	y = 1<<((i-1)&31);
	for(j=0;j<l;++j)
		a[j][s[j]-'a'][x] |= y;
}

void and(bitmap a,bitmap b)
{
	for(int i=0;i<160;++i) 
		a[i] &= b[i];
}

void or(bitmap a,bitmap b)
{
	for(int i=0;i<160;++i) 
		a[i] |= b[i];
}

int size(bitmap a)
{
	unsigned int nr = 0, j, k;
	for(int i=0;i<160;++i)
	{
		for(j=1,k=0;k<32;++k,j<<=1)
			if(a[i]&j)
				++nr;	
	}
	return nr;
}

int eval()
{
	memset(all,-1,sizeof(bitmap));
	char *p = s;
	for(i=0;i<l;++i)
	{
		if(*p!='(')
			and(all,a[i][(*p) - 'a']);
		else
		{
			memset(part,0,sizeof(bitmap));
			++p;
			while(*p!=')')
			{
				or(part,a[i][*p - 'a']);
				++p;
			}
			and(all,part);
		}
		++p;
	}
	return size(all);
}


int main()
{
	freopen("a_input.in","r",stdin);
	freopen("a_output.out","w",stdout);

	cin>>l>>d>>n;
	for(i=1;i<=d;++i)
	{
		cin>>s;
		addString(i);
	}
	for(k=1;k<=n;++k)
	{
		cin>>s;
		cout<<"Case #"<<k<<": "<<eval()<<endl;
	}

	fclose(stdout);
	return 0;
}
