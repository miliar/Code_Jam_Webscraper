#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

double ab(double a)
{
  if(a>0)return a;
  else return -a;
}
struct time
{
	double b;
	double e;
	bool d;
	bool operator <(const time &it) const {
    return e <= it.e;}

}na[22],nb[22];

int main()
{
	freopen("B-small-attempt4.in","r",stdin);
	freopen("B-small-attempt4.out","w",stdout);
	int flag;
	string temp;
	double t,h,m;
	int n,a,b,i,j,k,l;
	int ans_a,ans_b;
	cin>>n;
	//cout<<n<<endl;
	for(k=1;k<=n;k++)
	{
		ans_a=0;ans_b=0;
		cin>>t;
		//cout<<t<<endl;
		t=t/60;
		cin>>a>>b;
		//cout<<a<<" "<<b<<endl;
        for(i=0;i<a;i++)
		{
			cin>>temp;
			//cout<<temp<<" ";
			h=(temp[0]-'0')*10+temp[1]-'0';
			m=(temp[3]-'0')*10+temp[4]-'0';
			na[i].b=h+m/60;
			cin>>temp;
			//cout<<temp<<endl;
			h=(temp[0]-'0')*10+temp[1]-'0';
			m=(temp[3]-'0')*10+temp[4]-'0';
			na[i].e=h+m/60;
			na[i].d=1;
		}
		for(i=0;i<b;i++)
		{
			cin>>temp;
		  //cout<<temp<<" ";
			h=(temp[0]-'0')*10+temp[1]-'0';
			m=(temp[3]-'0')*10+temp[4]-'0';
			nb[i].b=h+m/60;
			cin>>temp;
		//cout<<temp<<endl;
			h=(temp[0]-'0')*10+temp[1]-'0';
			m=(temp[3]-'0')*10+temp[4]-'0';
			nb[i].e=h+m/60;
			nb[i].d=1;
		}
        sort(na,na+a);
		sort(nb,nb+b);
        for(i=0;i<a;i++)
		{
			flag=1;
			for(j=0;(nb[j].e<na[i].b+0.001)&&j<b;j++)
				if(nb[j].d&&((na[i].b-nb[j].e)>t||ab(t-ab(na[i].b-nb[j].e))<0.001)){l=j;flag=0;}
				if(!flag)nb[l].d=0;
			if(flag)ans_a++;
		}
		for(i=0;i<b;i++)
		{
			flag=1;
			for(j=0;(na[j].e<nb[i].b+0.001)&&j<a;j++)
				if(na[j].d&&((nb[i].b-na[j].e)>t||ab(t-ab(nb[i].b-na[j].e))<0.001)){l=j;flag=0;}
				if(!flag)na[l].d=0;
			if(flag)ans_b++;
		}
		cout<<"Case #"<<k<<":"<<" "<<ans_a<<" "<<ans_b<<endl;	
	}
		    
        
	return 0;
}