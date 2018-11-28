#include<stdio.h>
#include<math.h>
#include<map>
#include<algorithm>
using namespace std;
int ilecyfr,res=0;

map< pair<int,int>, bool> m;
bool check(int i, int a, int b)
{
    int mn=10;
    int maxx=pow(10,ilecyfr);
    int mn2=maxx/10;
    while(mn<maxx)
    {
	int temp=i;
	int l=temp%mn;
	temp/=mn;	
	temp+=l*mn2;
	mn*=10;
	mn2/=10;
	if(temp==i) continue;
	if(temp>=a && temp<=b)
	{

	    if(m.find(make_pair(min(i,temp),max(i,temp)))==m.end())
	    {
		res++;
		m[make_pair(min(i,temp),max(i,temp))]=true;
	    }
	}
    };
}
int main()
{
    ilecyfr=5;
    check(12345,0,0);
    int zes;scanf("%d",&zes);
    for (int z=1;z<=zes;z++)
    {
	int a,b;
	scanf("%d%d",&a,&b);
	ilecyfr=log10(a)+1;
	for (int i=a;i<=b;i++)
	{
	    check(i,a,b);
	}
	printf("Case #%d: %d\n",z,res);
	res=0;m.clear();


    }
}
