#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

int rec[1<<9];

inline int conv(int num,int base)
{
	int res=0,temp;
	while(num)
	{
		temp=num%base;
		res+=temp*temp;
		num/=base;
	}
	return res;
}

set<int> flag;

bool happy(int num,int base)
{
	flag.clear();
	while(1)
	{
		if(flag.find(num)!=flag.end()) return false;
		else if(num==1) return true;
		flag.insert(num);
		num=conv(num,base);
	}
	return num==1;
}

int base[20];
char input[60];

int getint(char s[],int &start)
{
	int res=0;
	while(s[start]!='\0' && s[start]==' ') start++;
	if(s[start]=='\0') return -1;
	while(s[start]!='\0' && s[start]>='0' && s[start]<='9')
	{
		res=res*10+s[start]-'0';
		start++;
	}
	return res;
}

void init()
{
	memset(rec,-1,sizeof(rec));
	int i,j;
	int temp=0;
	//rec[(1<<9)-1]=11814485;
	for(i=2;i<=11814485;i++)
	{
		//if(i%5000==0) printf("%d\n",i);
		temp=0;
		for(j=10;j>=2;j--)
		{
			if(happy(i,j))
				temp|=(1<<(j-2));
		}
		if(rec[temp]==-1) rec[temp]=i;
	}
}

int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int ca=1;
	int t,n;
	int i,j;
	int len,temp;
	int uu;
	int minone;
	bool flag;
	init();
	//printf("DONE!\n");
	scanf("%d",&t);
	gets(input);
	while(t--)
	{
		gets(input);
		len=0,n=0;
		while((temp=getint(input,len))!=-1)
			base[n++]=temp;
		temp=0;
		for(i=0;i<n;i++)
			temp|=(1<<(base[i]-2));
		uu=(1<<9);
		minone=99999999;
		for(i=1;i<uu;i++)
			if(rec[i]!=-1 && (i&temp)==temp && minone>rec[i])
				minone=rec[i];
		printf("Case #%d: %d\n",ca++,minone);
	}
	return 0;
}
