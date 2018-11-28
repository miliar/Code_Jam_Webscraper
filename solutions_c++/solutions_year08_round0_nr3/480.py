#pragma warning(disable : 4786) 

#include <stdio.h>
#include <string>
#include <vector>
#include <map>
#include <iostream.h>
#include <assert.h>
#include <algorithm>
#include <math.h>
using namespace std;


#define M_PI       3.14159265358979323846
#define BL 1024
char buf[BL];
vector<string> aToken;

struct quad
{
  quad( double x1, double y1, double x2, double y2 )
  {
    nx = x1;
    ny = y1;
    xx = x2;
    xy = y2;
  }
  double nx, ny, xx, xy;
};

struct point
{
  point(){}
  point( double &a, double &b)
  {
    x = a; y=b;
  }
  double x,y;
};

void toknize(char *p, char *del)
{
  aToken.clear();

  char *tok = strtok(p,del);

  if(tok != NULL)
    aToken.push_back( tok );  
  
  while( tok != NULL )
  {
    tok = strtok( 0 , del);

    if(tok != NULL)
      aToken.push_back( tok );
  }
}
  
double q_area;
double f, R, t, r ,g;
vector< pair<double, double> > range;
vector< quad > qlist;

int point_in_cir( double &x, double &y, double &r)
{
  if(x*x+y*y < r*r) return 1;

  return 0;
}

int intersect( point &p1, point &p2, double &r)
{// intersect:0 ; in:1 , out:2 ; 
  int ia = point_in_cir( p1.x , p1.y , r);
  int ib = point_in_cir( p2.x , p2.y , r);

  if( ia==1 && ib==1) return 1;
  if( ia==0 && ib==0) return 2;

  point p;
  if( fabs(p1.x-p2.x) <1.0e-10 )
  {
    p.x = p1.x;
    p.y = sqrt( r*r - p1.x*p1.x );
  }
  else
  {
    p.x = sqrt( r*r - p1.y*p1.y);
    p.y = p1.y;
  }

  if( ia == 1 && ib == 0) p2 = p;
  else if( ia == 0 && ib==1) p1 = p;
  else assert(0);

  return 0;
}

double cal_ql_area()
{
  double poly_area = 0;
  double arc_area = 0;

  double rr = R-t-f;
  vector<quad> line_list;
  for( int i=0 ; i< qlist.size(); i++)
  {
    line_list.clear();
    quad &q = qlist[i];
    point qpnt[4] = { point(q.nx, q.ny) , point(q.xx, q.ny) , point(q.xx, q.xy), point(q.nx, q.xy)};
    
    point sp,ep;

    int inum = 0;
    for( int j=0 ; j<4; j++)
    {
      point p1 = qpnt[j];
      point p2 = qpnt[(j+1)%4];
      int rlt = intersect( p1, p2, rr);
      if( rlt == 1 )
      { 
        line_list.push_back( quad(p1.x,p1.y, p2.x, p2.y) );
      }
      else if( rlt == 0)
      {
        if(inum != 0 )
        {
          quad prev = *(line_list.rbegin());

          line_list.push_back( quad(prev.xx,prev.xy, p1.x, p1.y) );
          sp = point(prev.xx,prev.xy);
          ep = point( p1.x, p1.y);

        }
        inum ++;
        line_list.push_back( quad(p1.x,p1.y, p2.x, p2.y) );
      }
    }

    double n_p_a = 0;
    int lc = line_list.size();
    for( j=0 ; j< lc ; j++)
    {
      double dx = -(line_list[j].xx - line_list[j].nx);
      double dy = (line_list[j].xy + line_list[j].ny);

      n_p_a += dx*dy/2.0;
    }

    poly_area += n_p_a;


    double arc_l2 = ( pow(sp.x-ep.x,2) + pow(sp.y - ep.y,2) );
    double arc_l  = sqrt(arc_l2);
    double arc_h = sqrt( pow(rr,2) - arc_l2*0.25 );
    double arc_ta= arc_l * arc_h /2.0;
    double theta = acos(arc_h/rr) * 2.0;
    double t_s   = asin(0.5*arc_l/rr);
    double arc_a = 0.5*rr*rr*theta - (arc_ta);

    arc_area += arc_a;
    






  }

  return poly_area + arc_area;
}

double cal_area()
{
  double rr = R-f-t;
  for( int i=0 ; i< range.size() ; i++)
  {
    for( int j=0 ; j<range.size() ; j++)
    {
      double x1 = range[j].first;
      double y1 = range[i].first;
      double x2 = range[j].second;
      double y2 = range[i].second;

      if( !point_in_cir(x1, y1, rr) ) break;
      if( !point_in_cir(x2, y2, rr) )
      {
        //add
        qlist.push_back( quad(x1,y1, x2,y2) );
      }
      else
      {
        q_area += pow( x2-x1, 2);
      }

    }
  }

  return q_area + cal_ql_area();


  return 0.0;
}

double docase()
{
  cin.getline( buf , BL);
  toknize( buf, " \n");
  assert(aToken.size() == 5);
  f = atof(aToken[0].c_str());
  R = atof(aToken[1].c_str());
  t = atof(aToken[2].c_str());
  r = atof(aToken[3].c_str());
  g = atof(aToken[4].c_str());


  double rr = R - t - f;
  double ql , qr;

  q_area = 0.0;
  range.clear();
  qlist.clear();

  while(1)
  {
    if(range.empty()) {
      ql = r+f;
    }
    else
    {
      ql = range.rbegin()->second;

      ql += (2.0*(f+r));
    }

    qr = ql + g - (2.0*f);

    if(ql > rr) break;
    if( ql >= qr) break;

    range.push_back( make_pair(ql, qr) );
    //printf( "%f ", qr - ql);
  }
  //printf("\n");

  double ina = cal_area();
  double ta  = M_PI * R * R / 4.0;

  //cout << ""
  //cout <<"Case #" << i+1 <<": " <<na <<" " <<nb <<endl;
  
  return 1.0-ina/ta;
}

void main()
{
  int icnt;

  cin.getline(buf, BL);
  icnt = atoi(buf);

  for( int i= 0 ; i< icnt ; i++)
  {
    printf("Case #%d: %lf\n", i+1 , docase() );
  }


}
