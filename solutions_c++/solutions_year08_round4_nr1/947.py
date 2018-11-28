#include <iostream>

using namespace std;

#define fi(n) for (int i=0;i<n;i++)
#define fj(n) for (int j=0;j<n;j++)

struct pt{int x,y;};

int m,v,a[300],b[300],c[300],ub;
string gg="",tg;

bool fv(int x)
{
	if (x>(m-1)/2)
		return c[x];
	if (tg[x]=='0')
		return (fv(x*2)||fv(x*2+1));
	return (fv(x*2)&&fv(x*2+1));
}

void go(int lv,string s)
{
	//cout<<lv<<' '<<s<<endl;
	if (lv==(m-1)/2+1)
	{
		tg=s;
		//cout<<"lv"<<lv<<fv(1)<<v<<(fv(1)&&v)<<endl;
		if ((fv(1)&&(v))||(!fv(1)&&!v))
		{
			//cout<<"diu";
			int uu=0;
			fi(s.size())
			if (s[i]!=gg[i])
				uu++;
			//cout<<uu<<s<<gg<<endl;
			ub=min(uu,ub);
			//cout<<ub<<endl;
		}
		return;
	}
	if (b[lv]){
	go(lv+1,s+"0");
		go(lv+1,s+"1");
	}
	else if (a[lv])
		go(lv+1,s+"1");
	else
		go(lv+1,s+"0");
}

int main()
{
	int cc;
	cin>>cc;
	for (int xx=0;xx<cc;xx++)
	{
		gg=" ";
		ub=99999;
		cin>>m>>v;
		for (int i=1;i<=m;i++)
		 {
		 if (i<=(m-1)/2)
		 {
			 cin>>a[i]>>b[i];
			 gg+=(char)(a[i]+'0');
		 }
		 else
		 {
			 cin>>c[i];
		 }
			 //cout<<i;
		}
		//cout<<gg<<endl;
		go(1," ");
		if (ub==99999)
			cout<<"Case #"<<xx+1<<": "<<"IMPOSSIBLE"<<endl;
		else
				cout<<"Case #"<<xx+1<<": "<<ub<<endl;
	}
	return 0;
}