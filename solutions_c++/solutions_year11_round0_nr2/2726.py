#include<iostream>
#include<string>
#include <fstream>
using namespace std;

struct S1
{
	char a1 , a2;
	char ch;

}s1[40];

struct S2
{
	char b1 , b2;
}s2[30];

ifstream fin("D:\\acm\\pa\\B-large.in");
ofstream fout("D:\\acm\\pa\\B-large.out");
 
#define cin fin
#define cout fout
int main()
{
	int t;
	int c , n , d , a;
	int i,j,count;
	string T;
	string W;
	cin>>t;
	count=0;
	while( t-- )
	{
		++count;
		W = "";
		cin>>c;
		for( i = 0 ; i < c ; ++i )
		{
			cin>>T;
			s1[i].a1 = T[0];
			s1[i].a2 = T[1];
			s1[i].ch = T[2];
		}

		cin>>d;

		for(i=0;i<d;++i)
		{
			cin>>T;
			s2[i].b1 = T[0];
			s2[i].b2 = T[1];
		}
		cin>>n;
		int l = 0;
		char ch;
		for(i=0;i<n;++i)
		{
			cin>>ch;
			if(W=="")
			{ 
				W += ch; 
				++l;
				continue; 
			}
			for(j=0;j<c;++j)
			{
				if(ch==s1[j].a1&&s1[j].a2==W[l - 1])
				{
					W[l - 1] = s1[j].ch; 
					break;
				}
				if(ch== s1[j].a2&&s1[j].a1==W[l-1])
				{ 
					W[l - 1] = s1[j].ch; 
					break;
				}
			}
			if( j < c )  continue; 
			for( j = 0 ; j < d ; ++j )
			{
				a = W.find( s2[j].b1 );
				if( a != -1 && ch == s2[j].b2 )
				{
					W = ""; 
					l = 0; 
					break; 
				}
				a = W.find( s2[j].b2 );
				if( a != -1 && ch == s2[j].b1 )
				{
					W= "";
					l = 0;
					break; 
				}
			}
			if( j >= d )
			{ 
				W += ch; 
				++l; 
			}
		}
		cout<<"Case #"<<count<<":"<<" [";
		for( i = 0 ; i < l - 1 ; ++i )
		{ 
			cout<<W[i]<<", ";
		}
		if( l != 0 )
		{ cout<<W[l - 1]; }
		cout<<"]"<<endl;
	}
	return 0;
}