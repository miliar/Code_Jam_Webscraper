#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <list>
#include <algorithm>
#include <cmath>
#include <cfloat>
#include <string>

typedef unsigned long long ull;

using namespace std;

typedef struct coord
{
  int x,y;
};

typedef struct node
{
  vector<coord> nbs;
  vector<int> cost;
  int dist;
  bool in;
};

int main()
{
  int _N;
  cin >> _N;

  int R,C;
  string s[15];

  node graph[15][15];
  coord dest,start;

  for (int _n=0; _n<_N; _n++)
    {
      cout << "Case #" << _n+1 << ": ";

      cin >> R >> C;
      for (int i=0; i<R; i++)
	{
	  cin >> s[i];
	}

      for (int i=0; i<R; i++)
	{
	  for (int j=0; j<C; j++)
	    {
	      //	  cout << "0" << endl;
	      int k=i*R+j;
	      graph[i][j].nbs.clear();
	      graph[i][j].cost.clear();
	      graph[i][j].dist=1000000;
	      graph[i][j].in=false;

	      coord c;
	      if (s[i][j]!='#')
		{
		  //	  cout << "5" << endl;
		  if (i>0 && s[i-1][j]!='#')
		    {
		      c.x=i-1;
		      c.y=j;
		      graph[i][j].nbs.push_back(c);
		      graph[i][j].cost.push_back(1);
		    }
		  if (j>0 && s[i][j-1]!='#')
		    {
		      c.x=i;
		      c.y=j-1;
		      graph[i][j].nbs.push_back(c);
		      graph[i][j].cost.push_back(1);
		    }
		  if (i<R-1 && s[i+1][j]!='#')
		    {
		      c.x=i+1;
		      c.y=j;
		      graph[i][j].nbs.push_back(c);
		      graph[i][j].cost.push_back(1);
		    }
		  if (j<C-1 && s[i][j+1]!='#')
		    {
		      c.x=i;
		      c.y=j+1;
		      graph[i][j].nbs.push_back(c);
		      graph[i][j].cost.push_back(1);
		    }
		  int mind=1000;
		  //	  cout << "6" << endl;

		  int i2=i,j2=j;
		  while (i2>0 && s[i2-1][j2]!='#')
		    {
		      i2--;
		    }
		  mind=i-i2+1;

		  int i3=i,j3=j;
		  while (i3<R-1 && s[i3+1][j3]!='#')
		    {
		      i3++;
		    }
		  mind=min(mind,i3-i+1);


		  int i4=i,j4=j;
		  //		  mind=1000;
		  while (j4>0 && s[i4][j4-1]!='#')
		    {
		      j4--;
		    }
		  mind=min(mind,j-j4+1);

		  int i5=i,j5=j;
		  while (j5<C-1 && s[i5][j5+1]!='#')
		    {
		      j5++;
		    }
		  mind=min(mind,j5-j+1);
		  //	  cout << "7" << endl;

		  c.x=i2;
		  c.y=j2;
		  graph[i][j].nbs.push_back(c);
		  graph[i][j].cost.push_back(mind);
		  c.x=i3;
		  c.y=j3;
		  graph[i][j].nbs.push_back(c);
		  graph[i][j].cost.push_back(mind);
		  c.x=i4;
		  c.y=j4;
		  graph[i][j].nbs.push_back(c);
		  graph[i][j].cost.push_back(mind);
		  c.x=i5;
		  c.y=j5;
		  graph[i][j].nbs.push_back(c);
		  graph[i][j].cost.push_back(mind);
		  //	  cout << "8" << endl;

		  if (s[i][j]=='O')
		    {
		      start.x=i;
		      start.y=j;
		      graph[i][j].dist=0;
		    }
		  else if (s[i][j]=='X')
		    {
		      dest.x=i;
		      dest.y=j;
		    }
		}
	    }
	}
      //	  cout << "10" << endl;

      //      vector<node> nbs;
      node added=graph[start.x][start.y];
      graph[start.x][start.y].in=true;
      //      nbs=start.nbs;

      int ret=-1;
      //	  cout << "9" << endl;
      while (true)
	{
	  //	  cout << "5" << endl;
	  for (int i=0; i<added.nbs.size(); i++)
	    {
	      if (graph[added.nbs[i].x][added.nbs[i].y].dist>added.dist+added.cost[i])
		{
		  graph[added.nbs[i].x][added.nbs[i].y].dist=added.dist+added.cost[i];
		}
	    }
	  int mini=-1;
	  int minj;
	  for (int i=0; i<R; i++)
	    {
	      for (int j=0; j<C; j++)
		{
		  int k=i*R+j;
		  if (!graph[i][j].in && (mini==-1 || (graph[mini][minj].dist>graph[i][j].dist && graph[i][j].dist < 1000000)))
		    {
		      mini=i;
		      minj=j;
		    }
		}
	    }
	  //	  cout << mini << " : " << minj << " | " << graph[mini][minj].dist << endl;
	  if (mini==-1)
	    {
	      break;
	    }
	  else if (mini==dest.x && minj==dest.y)
	    {
	      //	  cout << mini << " : " << minj << " | " << graph[mini][minj].dist << endl;
	      ret=graph[mini][minj].dist;
	      break;
	    }
	  else
	    {
	      //	  cout << mini << " : " << minj << " | " << graph[mini][minj].dist << endl;
	      graph[mini][minj].in=true;
	      added=graph[mini][minj];
	    }
	}

      if (ret==-1 || ret>=1000000)
	cout << "THE CAKE IS A LIE";
      else
	cout << ret;

      cout << endl;
    }

  return 0;
}
