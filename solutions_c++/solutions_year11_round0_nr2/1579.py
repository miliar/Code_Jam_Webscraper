#include<iostream>
#include<string>
#include <fstream>
using namespace std;
struct Node
{
	char a1 , a2;
	char x;
}N[40];
struct Node2
{
	char b1 , b2;
}nod2[30];

ifstream fin("C:\\B-large.in");
ofstream fout("C:\\A-small-attempt6.out");
 
#define cin fin
#define cout fout

int main()
{
	string ex,sign;
	int t;
	int c,n,d,a,i,num,j;
	cin>>t;
	num = 0;
	while( t-- )
	{
		++num;
		sign = "";
		cin>>c;
		for( i = 0 ; i < c ; ++i )
		{
			cin>>ex;
			N[i].a1 = ex[0];
			N[i].a2 = ex[1];
			N[i].x = ex[2];
		}
		cin>>d;
		for( i = 0 ; i < d ; ++i )
		{
			cin>>ex;
			nod2[i].b1 = ex[0];
			nod2[i].b2 = ex[1];
		}
		cin>>n;
		int l = 0;
		char ch;
		for( i = 0 ; i < n ; ++i )
		{
			cin>>ch;
			if( sign == "" ){ sign += ch; ++l; continue; }
			for( j = 0 ; j < c ; ++j )
			{
				if( ch == N[j].a1 && N[j].a2 == sign[l - 1] )
				{ sign[l - 1] = N[j].x; break; }
				if( ch == N[j].a2 && N[j].a1 == sign[l - 1] )
				{ sign[l - 1] = N[j].x; break; }
			}
			if( j < c ){ continue; }
			for( j = 0 ; j < d ; ++j )
			{
				a = sign.find( nod2[j].b1 );
				if( a != -1 && ch == nod2[j].b2 )
				{ sign = ""; l = 0; break; }
				a = sign.find( nod2[j].b2 );
				if( a != -1 && ch == nod2[j].b1 )
				{ sign = ""; l = 0; break; }
			}
			if( j >= d )
			{ sign += ch; ++l; }
		}
		int flag = 0;
		cout<<"Case #"<<num<<":"<<" [";
		for( i = 0 ; i < l ; ++i )
		{ 
			if( flag ) cout<<", ";
			else flag = 1;
			cout<<sign[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}