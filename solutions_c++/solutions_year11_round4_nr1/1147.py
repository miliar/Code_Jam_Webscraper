#include "myheading.h"

void SetFile( string s )
{
  while( s.size()>0 && s[0]<=' ' ) s.erase( 0, 1 ) ;
  while( s.size()>0 && s[s.size()-1]<=' ' ) s.erase( s.size()-1 ) ;
  string::size_type p = s.find('.') ;
  if( p!=string::npos ) s = s.substr( 0, p ) ;
  string sin  = s+".in" ;  freopen( sin. c_str() , "r" , stdin  );
  string sout = s+".out";  freopen( sout.c_str() , "w" , stdout );
}

#define myfor(i,c,d) for( int i=(c); i<=(d); ++i )

const int MAXN = 500000  ;
const int mod = 1000000007 ;

struct Tnode {
  double len;
  double speed;
};

bool cmp (const Tnode &a, const Tnode &b) {
  return a.speed < b.speed;
}

vector<Tnode> a;

double X;
double S, R;
double maxtime ;

void readin()
{
  cin >> X >> S >> R;
  cin >> maxtime;
  assert(R>S);
  R -= S;

  int n;
  cin >> n;

  a.clear();
  
  Tnode node;
  double cur = 0;
  myfor (i, 1, n) {
    double b, e, speed;
    cin >> b >> e >> speed;
    
    node.len = b - cur;
    node.speed = S;
    a.push_back(node);

    node.len = e - b;
    node.speed = speed + S;
    a.push_back(node);;
    cur = e;
  }

  node.len = X - cur;
  node.speed = S;
  a.push_back(node);
  
  sort(a.begin(), a.end(), cmp);
}

void work()
{
  double ans = 0;
  double time_left = maxtime;

  myforv (i, a) {
    double time_to_run = a[i].len / (a[i].speed + R);
    checkmin(time_to_run, time_left);
    
    a[i].len -= (a[i].speed + R) * time_to_run;
    time_left -= time_to_run;
    ans += time_to_run;

    ans += a[i].len / a[i].speed;
  }

  printf("%.12lf\n",ans);
}

int main()
{
  SetFile( "   A-large         " ) ;

  int test ; cin>>test ; readln(cin);
  cerr<<"n_test = "<<test<<endl;

  myfor( _u, 1, test )
  { 
    cout<<"Case #"<<_u<<": ";
    cerr<<"Running on Case #_"<<_u<<endl ;

    readin() ;
    work() ;
    //cout<<ans<<endl;

  }

  if( !seekeof( cin ) ) cout<<("wrong")<<endl;

  fclose( stdin ); fclose( stdout );
  return 0;
}
