#include <iostream>

using namespace std;


string a;
int tt;

void go(int lv,string c)
{
	if (lv==a.size()-1)
	{
		long long ss=0;
		long long cc=a[0]-'0';
		int ff=1;
		//cout<<c<<endl;
		for(int i=1;i<c.size();i++)
		{
			if (c[i]==' ')
				if (ff)
				cc=cc*10+a[i]-'0';
			else
				cc=cc*10-(a[i]-'0');
			else if (c[i]=='+')
				ss+=cc,cc=a[i]-'0',ff=1;
			else
				ss+=cc,cc='0'-a[i],ff=0;
		}
		ss+=cc;
		//cout<<c<<ss<<endl;
		if (ss%3==0||ss%2==0||ss%5==0||ss%7==0)
			tt++;
		return;
	}
	go(lv+1,c+"+");
	go(lv+1,c+"-");
	go(lv+1,c+" ");
}

int main()
{
	int q;
	cin>>q;
	for (int z=0;z<q;z++)
	{
		
		cin>>a;
		tt=0;
		go(0,"x");
		cout<<"Case #"<<z+1<<": "<<tt<<endl;
	}
	return 0;
}