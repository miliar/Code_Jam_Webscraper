#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))
#define mx(a,b) ((a<b) ? (b) : (a))
#define ab(a) ((a<0) ? (-(a)) : (a))
#define fr(a,b) for(int a=0; a<b; ++a)
#define fe(a,b,c) for(int a=b; a<c; ++a)
#define fw(a,b,c) for(int a=b; a<=c; ++a)
#define df(a,b,c) for(int a=b; a>=c; --a)
#define BIG 1000000000
#define SMALL -1000000000

using namespace std;

char buf[300];

void get_string(string &s)
	{
	scanf("%s", &buf);
	s.assign(buf);
	}

void get_line(string &s)
	{
	gets(buf);
	s.assign(buf);
	}
                                 
int n,d,l,quan = 0;
string mas[5000];
string pattern;

void process(int cur, int pos, string pref)
	{
//	cout<<"In the function: "<<cur<<" "<<pos<<" "<<pref<<endl;
	if(cur>=l)
		{
		fr(i,d)
			if(mas[i].compare(pref)==0)
				{
				quan++;
				}
		}
//	cout<<"Define symbol: "<<pattern[pos]<<endl;
	if(pattern[pos]!='(')
		{
		bool p = false;
		fr(i,d)
			{
//			cout<<"Get word start: "<<mas[i].substr(0,cur+1)<<endl;
//			cout<<"Get our start: "<<(pref+pattern[pos])<<endl;
			if(mas[i].substr(0,cur+1).compare(pref+pattern[pos])==0)
				{
				p = true;
				break;
				}
			}
		if(p) process(cur+1,pos+1,pref+pattern[pos]);
		return;
		}
	int i=pos+1;
	while(pattern[i]!=')') i++;
//	cout<<"End of brackets: "<<i<<endl;
	fe(j,pos+1,i)	
		{
		bool p =false;
//		cout<<"Order number: "<<j<<endl;
//		cout<<"Pattern symbol: "<<pattern[j]<<endl;
		fr(k,d)
			{
//			cout<<"Get word start: "<<mas[k].substr(0,cur+1)<<endl;
//			cout<<"Get our start: "<<(pref+pattern[j])<<endl;
			if((mas[k].substr(0,cur+1)).compare(pref+pattern[j])==0)
				{
//				cout<<"Accepted"<<endl;
				p = true;
				break;
				}
			}
		if(p) process(cur+1,i+1,pref+pattern[j]);
		}
						
	}


int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d%d%d\n",&l,&d,&n);
fr(i,d)
	{
	get_line(mas[i]);
//	cout<<"Get word: "<<mas[i]<<endl;
	}
fr(i,n)
	{
	get_line(pattern);
//	cout<<"Get pattern: "<<pattern<<endl;
	quan = 0;	
	process(0,0,"");
	printf("Case #%d: %d\n", (i+1), quan);

	}
return 0;
}
