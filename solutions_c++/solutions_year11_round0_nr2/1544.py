#include<iostream>
#include<string>
#include <fstream>
using namespace std;
struct Node1
{
	char a1 , a2;
	char change;
}nod1[40];
struct Node2
{
	char b1 , b2;
}nod2[30];
ifstream fin("C:\\Users\\Edward\\B-large.in");
ofstream fout("C:\\Users\\Edward\\A-small-attempt1.out");
 
#define cin fin
#define cout fout
int main()
{
	int t;
	int c , n , d , a;
	int i , num , j;
	string tmp;
	string wor;
	cin>>t;
	num = 0;
	while( t-- )
	{
		++num;
		wor = "";
		cin>>c;
		for( i = 0 ; i < c ; ++i )
		{
			cin>>tmp;
			nod1[i].a1 = tmp[0];
			nod1[i].a2 = tmp[1];
			nod1[i].change = tmp[2];
		}
		cin>>d;
		for( i = 0 ; i < d ; ++i )
		{
			cin>>tmp;
			nod2[i].b1 = tmp[0];
			nod2[i].b2 = tmp[1];
		}
		cin>>n;
		int l = 0;
		char ch;
		for( i = 0 ; i < n ; ++i )
		{
			cin>>ch;
			if( wor == "" ){ wor += ch; ++l; continue; }
			for( j = 0 ; j < c ; ++j )
			{
				if( ch == nod1[j].a1 && nod1[j].a2 == wor[l - 1] )
				{ wor[l - 1] = nod1[j].change; break; }
				if( ch == nod1[j].a2 && nod1[j].a1 == wor[l - 1] )
				{ wor[l - 1] = nod1[j].change; break; }
			}
			if( j < c ){ continue; }
			for( j = 0 ; j < d ; ++j )
			{
				a = wor.find( nod2[j].b1 );
				if( a != -1 && ch == nod2[j].b2 )
				{ wor = ""; l = 0; break; }
				a = wor.find( nod2[j].b2 );
				if( a != -1 && ch == nod2[j].b1 )
				{ wor = ""; l = 0; break; }
			}
			if( j >= d )
			{ wor += ch; ++l; }
		}
		cout<<"Case #"<<num<<":"<<" [";
		for( i = 0 ; i < l - 1 ; ++i )
		{ 
			cout<<wor[i]<<", ";
		}
		if( l != 0 )
		{ cout<<wor[l - 1]; }
		cout<<"]"<<endl;
	}
	return 0;
}