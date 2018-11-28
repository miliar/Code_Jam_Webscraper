#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
using namespace std;

int L,N,A;
char buf[11111111];
char S[11111111];
const int maxnode=1111111;

string name[maxnode];
double prob[maxnode];
int lleft[maxnode];
int rright[maxnode];

int cur;

double readprob(int&x)
{
	double ret=S[x++]-'0';
	if(S[x]=='.')
	{
		x++;
		double mul=0.1;
		while(S[x]>='0'&&S[x]<='9')
		{
			ret+=double(S[x]-'0')*mul;
			mul*=0.1;
			x++;
		}
	}
	return ret;
}

string readname(int&x)
{
	string ret="";
	while(S[x]>='a'&&S[x]<='z')
	{
		ret+=S[x];
		x++;
	}
	return ret;
}
void read(int& x,int n)
{
	
	if(S[x]=='(') x++;

	prob[n]=readprob(x);
	if(S[x]>='a'&&S[x]<='z') name[n]=readname(x);
	if(S[x]!=')')
	{
		lleft[n]=cur+1;
		read(x,++cur);
		rright[n]=cur+1;
		read(x,++cur);
	}
	//cout<<n<<" "<<prob[n]<<" "<<name[n]<<" "<<lleft[n]<<" "<<rright[n]<<endl;
	x++;
}

string AN,ss;
int M;

set<string> SET;
void animal()
{
	cin>>AN>>M;
	SET.clear();
	SET.insert("");

	int i;

	for(i=0;i<M;i++){cin>>ss; SET.insert(ss);};

	double ans=1.0;
	int pos=0;

	while(pos!=-1)
	{
		ans*=prob[pos];
		if(SET.find(name[pos])!=SET.end()) pos=lleft[pos];
		else pos=rright[pos];
	}

	printf("%.10lf\n",ans);

}
void test()
{
	int i,M,j,T;

	S[0]=0;
	strcpy(S,"");
	scanf("%d",&L);
	//cout<<L<<endl;
	cin.getline(buf,1111);

	for(i=0;i<L;i++)
	{
		
		cin.getline(buf,1111);
		//cout<<buf<<endl;
		M=strlen(buf);
		T=strlen(S);
		//cout<<S<<endl;
		for(j=0;j<M;j++) if(buf[j]!=' ') S[T++]=buf[j];
		S[T++]=0;
	}

	cur=0;

	for(i=0;i<maxnode;i++)
	{
		name[i]="";
		lleft[i]=rright[i]=-1;
	}

	int x=1;
	//cout<<S<<endl;
	read(x,0);

	scanf("%d",&A);

	printf("\n");
	for(i=0;i<A;i++) animal();
	
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int t=0,T;

	scanf("%d",&T);

	for(t=0;t<T;t++)
	{
		printf("Case #%d: ",t+1);
		test();
	}
}