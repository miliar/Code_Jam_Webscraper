#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#define MAX 200
using namespace std;
void getvalues( int &n, int btn[][MAX], pair<char, int>seq[], char inpt[])
{
    int t = 0;
	int h = -1, x = 1, y = 1, counter = 1;
    for( int i = 0; i < strlen(inpt); i++ )
	{
	  //cout << inpt[i] << endl;
	  if( inpt[i] != ' ')
	  {
		//cout << "-----" << endl;
		if( n == -1 )
		 t = t*10 + (inpt[i] - '0');
		else if( h == -1 ) t = inpt[i] == 'O' ? 0 : 1;
		else
		  t = t*10 + (inpt[i] - '0');
	  }
	  else
	  {
		//cout << "?????" << endl;
		 if( n == -1 )
		 {
		   n = t;
		   //cout << n << endl;
		   t = 0;
		 }
		 else if( h == -1 )
		 {
		   h = t;
		  // cout << "h :" << h << endl;
		   t = 0;
		 }
		 else if( t != 0 )
		 {
		   btn[h][h == 0? x++ : y++] = t;
		  // cout << "h : " << h << " " << t << endl;
		   seq[counter++] = make_pair( h == 0? 'O' : 'B', t );
		   t = 0;
		   h = -1;
		 }
	  }
	}
	btn[h][h == 0? x++ : y++] = t;
    //cout << "h : " << h << " " << t << endl;
	seq[counter++] = make_pair( h == 0? 'O' : 'B', t );
}
int main()
{
  int t;
  scanf("%d", &t);
  for( int i = 1; i <= t; i++ )
  {
	int n = -1;
	pair< char, int > seq[MAX];
	int btn[2][MAX];
	memset( btn, -1, sizeof( btn ) );
	char inpt[MAX*10];
	getchar();
	scanf("%[^\n]", inpt);
	//cout << inpt << endl;
    getvalues(n, btn, seq, inpt );
	/*for( int j = 1; j <= n; j++ )
	{
	  char bot;
	  int bt;
	  getchar();
	  scanf("%c", &bot);
	  getchar();
	  scanf("%d", &bt);
	  printf("%c %d\n", bot, bt );
	  seq[j] = make_pair( bot, bt );
	  if( bot == '0' )btn[0][x++] = bt;
	  else if( bot == 'B' )btn[1][y++] = bt;
	}*/
    //for( int j = 1; j <= n; j++ )printf("%c %d\n",seq[j].first, seq[j].second );
	int oidx = 1, bidx = 1, idx = 1, opos = 1, bpos = 1;
	int time = 0;
	while( idx <= n )
	{
	  char c = seq[idx].first;
	  //cout << seq[idx].first << "  " << seq[idx].second << endl;
	  int hidx = c == 'O' ? 0 : 1;

	  if( hidx == 0 )
	  {
		int gap = (int)abs((float)btn[0][oidx] - opos) + 1;
		opos = btn[0][oidx];
		time += gap;
        int xx;
		if( btn[1][bidx] != -1 )
		{
		  if(gap > (int)abs( (float)btn[1][bidx] - bpos )) xx = (int)abs((float)btn[1][bidx] - bpos);
		  else xx = gap;
        
		  bpos += ( xx * (btn[1][bidx] - bpos < 0 ? -1 : 1) );
		}
		
		oidx += 1;

	  }
	  else
	  {
		int gap = (int)abs((float)btn[1][bidx] - bpos) + 1;
		bpos = btn[1][bidx];
		time += gap;
        int xx;
        if( btn[0][oidx] != -1 )
		{
		  if(gap > (int)abs( (float)btn[0][oidx] - opos )) xx = (int)abs((float)btn[0][oidx] - opos);
		  else xx = gap;

		  opos += (xx * ( btn[0][oidx] - opos < 0 ? -1 : 1 ) );
		}
		bidx += 1;
	  }
	  idx += 1;
	}
	printf("Case #%d: %d\n", i, time);
  }
  return 0;
}