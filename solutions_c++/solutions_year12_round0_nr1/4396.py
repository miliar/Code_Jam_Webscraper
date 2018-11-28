// codejam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"



// basic file operations

#include <iostream>
#include <fstream>
#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
using namespace std;





using namespace std;
#define FOR(N) for(int i = 0; i < N; i++)
#define FOR2(N) for(int j = 0; j < N; j++)
#define FOR3(N) for(int k = 0; k < N; k++)

void A()
{
	freopen("c:\\A-small-practice.in","rt",stdin);
	freopen("c:\\A-small.out","wt",stdout);
	int N;
	std::cin >> N;
	int credit;
	int noItems;
	int array1[2010];
	FOR(N)
	{
		printf("Case #%d: ",i+1);
		cin >> credit;
		cin >> noItems;
		FOR2(noItems)
		{
			cin >> array1[j];
		}
		FOR2(noItems)
		{
			for(int k = j+1; k < noItems; k++)
			{
				if(array1[j] + array1[k] == credit)
				{
					cout << j+1 << " " << k+1 << endl;
				}
			}
		}
	}
}

void B()
{
	freopen("c:\\B.in","rt",stdin);
	freopen("c:\\B-small.out","wt",stdout);
	int N;
		string s1;
	std::cin >> N;
	getline(cin,s1);
	
	FOR(N)
	{
		string s;
	
		printf("Case #%d:",i+1);
		getline(cin,s);
		std::stringstream ss(s);
		std::vector<std::string> v;
		
		while(ss>>s1)
		{
			v.push_back(s1);
		}
		reverse(v.begin(),v.end());
		FOR2(v.size())
		{
			cout<< " " << v[j];
		}
		cout << endl;
		
	}
}

void C()
{
	freopen("c:\\c.in","rt",stdin);
	freopen("c:\\c-small.out","wt",stdout);
	int N;
		string s1;
	std::cin >> N;
	getline(cin,s1);
	
	FOR(N)
	{
		string s;
	
		printf("Case #%d: ",i+1);
		getline(cin,s);
		int lastButton = -1;
		FOR(s.length())
		{
			char c = s[i];
			if(c == 'a' || c == 'b' || c == 'c')
			{
				if(lastButton == 2)
					cout << " " ;
				lastButton = 2;
				if(c=='a')
					cout << 2;
				if(c=='b')
					cout << 22;
				if(c=='c')
					cout << 222;
			}
			if(c == 'd' || c == 'e' || c == 'f')
			{
				if(lastButton == 3)
					cout << " " ;
				lastButton = 3;
				if(c=='d')
					cout << 3;
				if(c=='e')
					cout << 33;
				if(c=='f')
					cout << 333;
			}

			if(c == 'g' || c == 'h' || c == 'i')
			{
				if(lastButton == 4)
					cout << " " ;
				lastButton = 4;
				if(c=='g')
					cout << 4;
				if(c=='h')
					cout << 44;
				if(c=='i')
					cout << 444;
			}
			if(c == 'j' || c == 'k' || c == 'l')
			{
				if(lastButton == 5)
					cout << " " ;
				lastButton = 5;
				if(c=='j')
					cout << 5;
				if(c=='k')
					cout << 55;
				if(c=='l')
					cout << 555;
			}

			if(c == 'm' || c == 'n' || c == 'o')
			{
				if(lastButton == 6)
					cout << " " ;
				lastButton = 6;
				if(c=='m')
					cout << 6;
				if(c=='n')
					cout << 66;
				if(c=='o')
					cout << 666;
			}

			if(c == 'p' || c == 'q' || c == 'r'|| c == 's')
			{
				if(lastButton == 7)
					cout << " " ;
				lastButton = 7;
				if(c=='p')
					cout << 7;
				if(c=='q')
					cout << 77;
				if(c=='r')
					cout << 777;
				if(c=='s')
					cout << 7777;
			}

			if(c == 't'|| c == 'u' || c == 'v')
			{
				if(lastButton == 8)
					cout << " " ;
				lastButton = 8;
				if(c=='t')
					cout << 8;
				if(c=='u')
					cout << 88;
				if(c=='v')
					cout << 888;
			}

			if(c == 'w' || c == 'x' || c == 'y'|| c == 'z')
			{
				if(lastButton == 9)
					cout << " " ;
				lastButton = 9;
				if(c=='w')
					cout << 9;
				if(c=='x')
					cout << 99;
				if(c=='y')
					cout << 999;
				if(c=='z')
					cout << 9999;
			}
			if(c == ' ' )
			{
				if(lastButton == 0)
					cout << " " ;
				lastButton = 0;
			
					cout << 0;
			}
		}
		cout << endl;
		
	}
}




void A_2008()
{
	freopen("c:\\jam\\A.in","rt",stdin);
	freopen("c:\\jam\\A.out","wt",stdout);
	int N;
	string s1;
	std::cin >> N;
	//getline(cin,s1);
	
	FOR(N)
	{
		string s;
		std::vector<long long> v;
		std::vector<long long> v2;
		printf("Case #%d: ",i+1);		
		int nn;
		cin >>nn;		
		long long ll;
	
		FOR2(nn)
		{	
			cin>>ll;
			v.push_back(ll);
		}
		FOR2(nn)		
		{
			cin>>ll;
			v2.push_back(ll);
		}
		sort(v.begin(),v.end());
		sort(v2.begin(),v2.end(),greater<long long>());
		//reverse(v2.begin(),v2.end());
		long long minSum =0;
		FOR2(v.size())
		{
			minSum += v[j]*v2[j];
		}
		cout << minSum;
		cout << endl;
		
	}
}





#define rep(i,N) for(int i=0;i<N;i++)
#define rep2(i,j,N) for(int i =j;j<N;i++)
int _tmain(int argc, _TCHAR* argv[])
{
	freopen("c:\\A-small-attempt1.in","rt",stdin);
	freopen("c:\\A-small.out","wt",stdout);
	
	string map1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string map1v = "our language is impossible to understand";
	string map2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string map2v = "there are twenty six factorial possibilities";
	string map3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	string map3v = "so it is okay if you want to just give up";
	char map[29];
	int i;
	rep(i,map1.size())
	{
		if(map1[i] != ' ')
		{
			int index =   map1[i]- 'a';
			map[index] = map1v[i];
		}
	}
	rep(i,map2.size())
	{
		if(map2[i] != ' ')
		{
			map[map2[i]-'a'] = map2v[i];
		}
	}

	rep(i,map3.size())
	{
		if(map3[i] != ' ')
		{
			map[map3[i]-'a'] = map3v[i];
		}
	}

	map['q'-'a'] = 'z';
	map['z'-'a'] = 'q';
	//rep(i,28)
	//{
	//	cout <<char('a'+ i) << " = " <<  map[i] << endl;
	//}
	int N;
		string s1;
	std::cin >> N;
	getline(cin,s1);

	FOR(N)
	{
		
		getline(cin,s1);
		rep(i,s1.size())
		{
			if(s1[i] != ' ')
			{
				s1[i] = map[s1[i]-'a'];
			}
		}
		printf("Case #%d: ",i+1);
		cout << s1 << endl;
	}


	return 0;
}

