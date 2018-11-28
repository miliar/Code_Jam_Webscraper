#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;

typedef struct centermass {
  int x;
  int y;
  int z;
  int velx;
  int vely;
  int velz;
} centermass;



//from http://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment and http://www.softsurfer.com/Archive/algorithm_0102/#dist_Point_to_Line()
typedef struct tagXYZ
{
    double X, Y, Z;
}
XYZ;

#define dot(u,v)   ((u).X * (v).X + (u).Y * (v).Y + (u).Z * (v).Z)
#define norm(v)    sqrt(dot(v,v))  // norm = length of vector
#define d(u,v)     norm(u-v)       // distance = norm of difference

double Magnitude( XYZ *Point1, XYZ *Point2 )
{
    XYZ Vector;

    Vector.X = Point2->X - Point1->X;
    Vector.Y = Point2->Y - Point1->Y;
    Vector.Z = Point2->Z - Point1->Z;

    return (double)sqrt( Vector.X * Vector.X + Vector.Y * Vector.Y + Vector.Z * Vector.Z );
}

int DistancePointLine( XYZ *Point, XYZ *LineStart, XYZ *LineEnd, double *Distance, double *Time )
{
    double LineMag;
    double U;
    XYZ Intersection;

    LineMag = Magnitude( LineEnd, LineStart );
    /*
    if(LineMag<0.00001&&LineMag>-0.00001) {
        *Time=0.0f;
        *Distance=Magnitude(Point,LineStart);
    }*/

    double Unum = ( ( ( Point->X - LineStart->X ) * ( LineEnd->X - LineStart->X ) ) +
    ( ( Point->Y - LineStart->Y ) * ( LineEnd->Y - LineStart->Y ) ) +
    ( ( Point->Z - LineStart->Z ) * ( LineEnd->Z - LineStart->Z ) ) );
    double Udem= ( LineMag * LineMag );
    U=Unum/Udem;
    *Time=U;


    Intersection.X = LineStart->X + U * ( LineEnd->X - LineStart->X );
    Intersection.Y = LineStart->Y + U * ( LineEnd->Y - LineStart->Y );
    Intersection.Z = LineStart->Z + U * ( LineEnd->Z - LineStart->Z );

    *Distance = Magnitude( Point, &Intersection );

    if( U <= 0.0f ) {
        *Time=0.0f;
        *Distance=Magnitude(Point,LineStart);
        return 0;   // closest point does not fall within the line segment
    }


    return 1;
}

/*
float
dist_Point_to_Line( Point P, Line L)
{
    Vector v = L.P1 - L.P0;
    Vector w = P - L.P0;

    double c1 = dot(w,v);
    double c2 = dot(v,v);
    double b = c1 / c2;

    Point Pb = L.P0 + b * v;
    return d(P, Pb);
}
*/


int ncases;

int main() {
  scanf(" %d",&ncases);
  for(int i=0;i<ncases;i++) {
    int nflies;
    scanf(" %d",&nflies);
    centermass a;
    a.x=0;
    a.y=0;
    a.z=0;
    a.velx=0;
    a.vely=0;
    a.velz=0;
    for(int j=0;j<nflies;j++) {
      int x,y,z,velx,vely,velz;
      scanf(" %d %d %d %d %d %d",&x,&y,&z,&velx,&vely,&velz);
      a.x+=x;
      a.y+=y;
      a.z+=z;
      a.velx+=velx;
      a.vely+=vely;
      a.velz+=velz;
    }
    double x=a.x/(double)nflies;
    double y=a.y/(double)nflies;
    double z=a.z/(double)nflies;
    double velx=a.velx/(double)nflies;
    double vely=a.vely/(double)nflies;
    double velz=a.velz/(double)nflies;
    double dist;
    double time;

    XYZ start,end,orig;
    orig.X=orig.Y=orig.Z=0;
    start.X=x;
    start.Y=y;
    start.Z=z;
    end.X=x+velx;
    end.Y=y+vely;
    end.Z=z+velz;
    if(velx==0&&vely==0&&velz==0) {
      dist=Magnitude(&orig,&start);
      time=0.0;
    } else {
      DistancePointLine( &orig, &start, &end, &dist, &time );
    }
    printf("Case #%d: %.08f %.08f\n",i+1,dist,time);

  }
  return 0;
}



