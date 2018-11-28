#include <iostream>
#include <vector>
#include <utility>
#include <map>
#include <complex>
#include <iomanip>

using namespace std;
typedef long double real_type;
struct vector_type {
  real_type x;
  real_type y;
  real_type z;

  vector_type(){}
  vector_type(real_type ax, real_type ay, real_type az) { x=ax;y=ay;z=az; }
};

static real_type dot( const vector_type& u, const vector_type& v )
{
  return u.x * v.x + u.y * v.y + u.z * v.z;
}

static vector_type cross( const vector_type& u, const vector_type& v )
{
  return vector_type(
      u.y * v.z - u.z * v.y,
      -u.x * v.z + u.z * v.x,
      u.x * v.y - u.y * v.x );
}

static real_type length_sq(const vector_type& v) {
  return v.x*v.x+v.y*v.y+v.z*v.z;
}

static vector_type operator*(real_type a, const vector_type& b) {
  return vector_type(b.x*a,b.y*a,b.z*a);
}

static vector_type operator+(const vector_type& a, const vector_type& b) {
  return vector_type(a.x+b.x,a.y+b.y,a.z+b.z);
}


static real_type nearest(
    const vector_type& p, const vector_type& a, const vector_type& d) {
  real_type s = (-dot(a,d)+dot(p,d))/(length_sq(d));
  return s;
}

int main() {
  vector_type o(0,0,0);

  int T;
  std::cin >> T;
  for( int i =  0 ; i< T ; i++ ) {
    int N;
    std::cin >> N;

    int tx = 0;
    int ty = 0;
    int tz = 0;
    int tvx=0;
    int tvy=0;
    int tvz=0;
    for( int j = 0 ; j < N ; j++ ) {
      int x, y, z, vx,vy,vz;
      cin >> x >> y >> z >> vx >> vy >> vz;
      tx+=x;
      ty+=y;
      tz+=z;
      tvx+=vx;
      tvy+=vy;
      tvz+=vz;
    }

    vector_type a;
    a.x = tx/real_type(N);
    a.y = ty/real_type(N);
    a.z = tz/real_type(N);

    vector_type v;
    v.x = tvx/real_type(N);
    v.y = tvy/real_type(N);
    v.z = tvz/real_type(N);

    if(length_sq(v) == 0) {
      std::cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
      cout << "Case #" << i+1 << ": " << setprecision(8)
           << sqrt(length_sq(a)) << " " << 0 << endl;
      continue;
    }

    real_type s = nearest(o,a,v);
    if(s < 0 ) { s = 0; }

    vector_type q = a + s * v;

#if 0
    cerr << a.x << "," << a.y << "," << a.z << ":" 
         << tvx << "," << tvy << "," << tvz << ":" 
         << q.x << "," << q.y << "," << q.z;
#endif

    real_type d = sqrt(length_sq(q));
    std::cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
    cout << "Case #" << i+1 << ": " << setprecision(8)
         << d << " " << s << endl;
  }
  return 0;
}
