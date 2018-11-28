/*

//#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <string.h>
#include <algorithm>
#include <stack>
#include <map>
#include <list>
#include <cmath>
#include <math.h>
#include <stdlib.h>
#include <vector>
using namespace std;

ifstream cin("E:\\Heyi\\pd\\GoogleJam\\Qualification2010.5.7\\Qualification\\B-small-attempt5.in");
ofstream cout("E:\\Heyi\\pd\\GoogleJam\\Qualification2010.5.7\\Qualification\\B-small-attempt5.out");
#define POUT(n,v){cout<<"Case #"<<(n+1)<<": "<<v<<endl;} 
#define  MAX_C 37
#define MAX_D 29
#define MAX_N 101

list<char> m_list;
void Combine(char *c)
{
	if (m_list.size()<2)
	{
		return;
	}
	char ch[3]={0};
	ch[0]=m_list.front();
	m_list.pop_front();
	ch[1]=m_list.front();
	
	if(c[0]==ch[0] && c[1]==ch[1]
		|| c[0]==ch[1] && c[1]==ch[0])
	{
		m_list.pop_front();
		m_list.push_front(c[2]);
	}
	else
		m_list.push_front(ch[0]);
}
void Oppose(char *o)
{
	if (m_list.size()<2)
	{
		return;
	}
	char ch;
	ch=m_list.front();
	list<char>::iterator it;
	if (o[0]==ch)
	{
		for (it=m_list.begin();it!=m_list.end();it++)
		{
			if (*it==o[1])
			{
				m_list.clear();
				return;
			}
		}

	}				
	else if (o[1]==ch)
	{
		for (it=m_list.begin();it!=m_list.end();it++)
		{
			if (*it==o[0])
			{
				m_list.clear();
				return;
			}
		}
	}
}
int main()
{
	
	int T;
	cin>>T;
	for (int i=0;i<T;i++)
	{
		
		char combine[4]={0};
		char opposed[3]={0};
		int C,D,N;
		cin>>C;
		int j;
		for (j=0;j<C;j++)
		{
			cin>>combine[j];
		}
		cin>>D;
		for(j=0;j<D;j++)
		{
			cin>>opposed[j];
		}
		cin>>N;
		char str[MAX_N];
		cin>>str;
		
		int status[MAX_N];
		memset(status,1,MAX_N);
		m_list.clear();

		for (j=0;j<N;j++)
		{
			
			m_list.push_front(str[j]);
			if (C)
			{
				Combine();
			}
			if (D)
			{
				Oppose();
			}
		}
		
		cout<<"Case #"<<(i+1)<<": [";
		list<char>::iterator it;
		int first=1;
		m_list.reverse();
		for (it=m_list.begin();it!=m_list.end();it++)
		{
			if (first)
			{
				cout<<*it;
				first=0;
			}
			else cout<<", "<<*it;
		}
		
		cout<<"]"<<endl;
	}
	return 0;
}
*/
//#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <string.h>
#include <algorithm>
#include <stack>
#include <map>
#include <list>
#include <cmath>
#include <math.h>
#include <stdlib.h>
#include <vector>
using namespace std;

ifstream cin("E:\\Heyi\\pd\\GoogleJam\\Qualification2010.5.7\\Qualification\\B-large.in");
ofstream cout("E:\\Heyi\\pd\\GoogleJam\\Qualification2010.5.7\\Qualification\\B-large.out");
#define POUT(n,v){cout<<"Case #"<<(n+1)<<": "<<v<<endl;} 
#define  MAX_C 37
#define MAX_D 29
#define MAX_N 101

char combine[MAX_C][4];
char opposed[MAX_D][3];

list<char> m_list;
bool getCombine(char *c)
{
	if (m_list.size()<2)
	{
		return false;
	}
	char ch[3]={0};
	ch[0]=m_list.front();
	m_list.pop_front();
	ch[1]=m_list.front();
	
	if(c[0]==ch[0] && c[1]==ch[1]
		|| c[0]==ch[1] && c[1]==ch[0])
	{
		m_list.pop_front();
		m_list.push_front(c[2]);
		return true;
	}
	else
	{
		m_list.push_front(ch[0]);
		return false;
	}
}
void Combine(int n)
{
	if (m_list.size()<2)
	{
		return;
	}
	for (int i=0;i<n;i++)
	{
		if(getCombine(combine[i]))
			break;
	}
	
}
bool findOppose(char* o)
{
	if (m_list.size()<2)
	{
		return false;
	}
	char ch;
	ch=m_list.front();
	list<char>::iterator it;
	if (o[0]==ch)
	{
		for (it=m_list.begin();it!=m_list.end();it++)
		{
			if (*it==o[1])
			{
				m_list.clear();
				return true;
			}
		}
		
	}				
	else if (o[1]==ch)
	{
		for (it=m_list.begin();it!=m_list.end();it++)
		{
			if (*it==o[0])
			{
				m_list.clear();
				return true;
			}
		}
	}
	return false;
}
void Oppose(int n)
{
	if (m_list.size()<2)
	{
		return;
	}
	for (int i=0;i<n;i++)
	{
		if(findOppose(opposed[i]))
			break;
	}

}
int main()
{
	
	int T;
	cin>>T;
	for (int i=0;i<T;i++)
	{
		
		
		int C,D,N;
		cin>>C;
		int j;
		for (j=0;j<C;j++)
		{
			cin>>combine[j];
		}
		cin>>D;
		for(j=0;j<D;j++)
		{
			cin>>opposed[j];
		}
		cin>>N;
		char str[MAX_N];
		cin>>str;
		
		int status[MAX_N];
		memset(status,1,MAX_N);
		m_list.clear();

		for (j=0;j<N;j++)
		{	
			m_list.push_front(str[j]);	
			Combine(C);
			Oppose(D);		
		}
		
		cout<<"Case #"<<(i+1)<<": [";
		list<char>::iterator it;
		int first=1;
		m_list.reverse();
		for (it=m_list.begin();it!=m_list.end();it++)
		{
			if (first)
			{
				cout<<*it;
				first=0;
			}
			else cout<<", "<<*it;
		}
		
		cout<<"]"<<endl;
	}
	return 0;
}