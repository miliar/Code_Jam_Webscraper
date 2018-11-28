#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<map>

using namespace std;
void reverse( char str[])
{
   int i = 0;
   int j = strlen( str )-1;
   while( i < j )
   {
	 char t = str[j];
	 str[j] = str[i];
	 str[i] = t;
	 i++;j--;
   }
}
void add( string &res, char c, map< string, char>&cx, map<char, char>&dx )
{
   res = res + c;
  // cout << res << endl;
   if( res.size() > 1 )
   {
    char combo[3];
    combo[2] = '\0';
	combo[1] = res[res.size()-1];
	combo[0] = res[res.size()-2];
	while( cx.find( combo ) != cx.end() )
	{
	 res = res.substr( 0, res.size()-2 ) + cx[combo];
     combo[2] = '\0';
     combo[1] = res[res.size()-1];
     combo[0] = res[res.size()-2];
	}
	for( int k = res.size()-2; k >= 0 ; k-- )
	  if( dx.find( res[k] ) != dx.end() && dx[res[k]] == res[res.size()-1])
	  {
		res = "";
		break;
	  }
   }
}
int main()
{
  int t;
  scanf("%d", &t);
  for( int i = 1; i <= t; i++ )
  {
	int c;
	map<string, char>cx;
	map<char, char>dx;
	scanf("%d", &c);
	for( int j = 1; j <= c; j++ )
	{
	  char cb[10], let[3];
	  scanf("%s", cb);
	  for( int k = 0; k <= 1; k++ )let[k] = cb[k];
	  let[2] = '\0'; 
	  cx[let] = cb[2];
	  reverse(let);
	  cx[let] = cb[2];
	}
	int d;
	scanf("%d", &d);
	for( int j = 1; j <= d; j++ )
	{
	  char cb[10];
	  scanf("%s", cb);
      dx[cb[0]] = cb[1];
	  dx[cb[1]] = cb[0];
	}
	int n;
	/*for( map <string, char>::iterator iter = cx.begin(); iter != cx.end(); iter++ )printf("%s %c\n", (iter->first).c_str(), iter->second);
	printf("\n");
	for( map <char, char>::iterator iter = dx.begin(); iter != dx.end(); iter++ )printf("%c %c\n", iter->first, iter->second);*/
	scanf("%d", &n);
	getchar();
	string res = "";
    map<char, bool>px;
	for( int j = 1; j <= n; j++ )
	{
	  char c = getchar();
	  add( res, c, cx, dx );
	}
	printf("Case #%d: [", i );
	for( int j = 0; j < res.size(); j++ )
	{
	  printf("%c",res[j]);
	  if( j != res.size() - 1)
		printf(", ");
	}
	printf("]\n");
  }
  return 0;
}