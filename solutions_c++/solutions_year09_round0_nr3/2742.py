#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;
int main()
{



string s;
int tc,i,z=0;
cin>>tc; getchar();
while(tc--)
{
z++;
vector <int>w;
vector <int>e;
vector <int>l;
vector <int>c;
vector <int>o;
vector <int>m;

vector <int>space;

vector <int>t;

vector <int>d;

vector <int>j;
vector <int>a;
	
	
	char str[550];
	gets(str);
	int count=0,slen=strlen(str);
	for(i=0;i<slen;i++)
	{
		switch(str[i])
		{
		case 'w':	w.push_back(i);
				break;
		case 'e':	e.push_back(i);
				break;
		case 'l':	l.push_back(i);
				break;
		case 'c':	c.push_back(i);
				break;
		case 'o':	o.push_back(i);
				break;
		case 'm':	m.push_back(i);
				break;
		case 't':	t.push_back(i);
				break;
		case ' ':	space.push_back(i);
				break;
		case 'd':	d.push_back(i);
				break;
		case 'j':	j.push_back(i);
				break;
		case 'a':	a.push_back(i);
				break;
		}
	}
		
		//for(int i=0;i<e.size();i++)cout<<e[i]<<" ";
		int arr[20]={0};
		
		for(arr[0]=0;arr[0]<w.size();arr[0]++)//w
		{
		for(arr[1]=0;arr[1]<e.size();arr[1]++)//e
		{
		for(arr[2]=0;arr[2]<l.size();arr[2]++)//l
		{
		for(arr[3]=0;arr[3]<c.size();arr[3]++)//c
		{
		for(arr[4]=0;arr[4]<o.size();arr[4]++)//o
		{
		for(arr[5]=0;arr[5]<m.size();arr[5]++)//m
		{
		for(arr[6]=arr[1];arr[6]<e.size();arr[6]++)//e
		{
		for(arr[7]=0;arr[7]<space.size();arr[7]++)//space
		{
		for(arr[8]=0;arr[8]<t.size();arr[8]++)//t
		{
		for(arr[9]=arr[4];arr[9]<o.size();arr[9]++)//o
		{
		for(arr[10]=arr[7];arr[10]<space.size();arr[10]++)//space
		{
		for(arr[11]=arr[3];arr[11]<c.size();arr[11]++)//c
		{
		for(arr[12]=0;arr[12]<o.size();arr[12]++)//o
		{
		for(arr[13]=0;arr[13]<d.size();arr[13]++)//d
		{
		for(arr[14]=arr[6];arr[14]<e.size();arr[14]++)//e
		{
		for(arr[15]=arr[10];arr[15]<space.size();arr[15]++)//space
		{
		for(arr[16]=0;arr[16]<j.size();arr[16]++)//j
		{
		for(arr[17]=0;arr[17]<a.size();arr[17]++)//a
		{
		for(arr[18]=arr[5];arr[18]<m.size();arr[18]++)//m
		{
		
		if(w[arr[0]]<e[arr[1]] && e[arr[1]]<l[arr[2]] && l[arr[2]]<c[arr[3]] && c[arr[3]]<o[arr[4]] && o[arr[4]]<m[arr[5]] && m[arr[5]]<e[arr[6]] && e[arr[6]]<space[arr[7]] && space[arr[7]]<t[arr[8]] && t[arr[8]]<o[arr[9]] && o[arr[9]]<space[arr[10]] && space[arr[10]]<c[arr[11]] && c[arr[11]]<o[arr[12]] && o[arr[12]]<d[arr[13]] && d[arr[13]]<e[arr[14]] && e[arr[14]]<space[arr[15]] && space[arr[15]]<j[arr[16]] && j[arr[16]]<a[arr[17]] && a[arr[17]]<m[arr[18]])
		{
		//cout<<"dfgf";
		count++;
		}
		
		
		
		
		
		
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		}
		
		}
		count=count%10000;
		int no=0,ct=count;
		while(ct!=0)
		{
		ct/=10;
		no++;
		}
		
	cout<<"Case #"<<z<<": ";
	for(int k=0;k<4-no;k++)
	cout<<"0";
	if(count!=0)
	
	cout<<count;
	
	cout<<endl;
	}
	
}


