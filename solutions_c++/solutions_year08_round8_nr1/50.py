#include <cstdio>
#include <cmath>

static const double EPS = 1e-7;

int X11, Y11, X12, Y12, X13, Y13;
int X21, Y21, X22, Y22, X23, Y23;

void Read()
{
	scanf( "%d%d%d%d%d%d", &X11, &Y11, &X12, &Y12, &X13, &Y13 );
	scanf( "%d%d%d%d%d%d", &X21, &Y21, &X22, &Y22, &X23, &Y23 );
}

double Abs( double x )
{
	if( x >= 0 )
		return x;
	else
		return -x;
}

double Sqr( double x )
{
	return x * x;
}

double Sqrt( double x )
{
	if( x < 0 )
		return 0;
	return sqrt( x );
}

struct sPoint
{
	double X, Y;
	sPoint()
	{
	}
	sPoint( double x, double y )
		: X( x )
		, Y( y )
	{
	}
};

struct sVector
{
	double X, Y;
	sVector()
	{
	}
	sVector( double x, double y )
		: X( x )
		, Y( y )
	{
	}
};

sVector operator -( const sPoint &p1, const sPoint &p2 )
{
	return sVector( p1.X - p2.X, p1.Y - p2.Y );
}

sPoint operator +( const sPoint &p, const sVector &v )
{
	return sPoint( p.X + v.X, p.Y + v.Y );
}

sVector operator *( double x, const sVector &v )
{
	return sVector( x * v.X, x * v.Y );
}

double Det( const sVector &v1, const sVector &v2 )
{
	return v1.X * v2.Y - v1.Y * v2.X;
}

sVector operator -( const sVector &v )
{
	return sVector( -v.X, -v.Y );
}

bool Cross( const sPoint &a, const sPoint &b, const sPoint &c, const sPoint &d, sPoint &p )
{
	sVector ab = b - a, ac = c - a, cd = d - c;
	double det = Det( ab, -cd );
	double detu = Det( ac, -cd );
	double detv = Det( ab, ac );

	if( fabs( det ) <= EPS )
		return false;
	else
	{
		double u = detu / det;
		double v = detv / det;
		if( !( -EPS <= u && u <= 1 + EPS &&
			   -EPS <= v && v <= 1 + EPS ) )
		   return false;
		p = a + u * ab;
		return true;
	}
}

double operator *( const sVector &v1, const sVector &v2 )
{
	return v1.X * v2.X + v1.Y * v2.Y;
}

double Abs( const sVector &v )
{
	return sqrt( Sqr( v.X ) + Sqr( v.Y ) );
}

double Angle( const sVector &v1, const sVector &v2 )
{
	double cos = v1 * v2 / Abs( v1 ) / Abs( v2 );
	double sin = Sqrt( 1 - Sqr( cos ) );
	if( Det( v1, v2 ) < 0 )
		sin = -sin;
	return atan2( sin, cos );
}

sVector Rotate( const sVector &v, double angle )
{
	return sVector( v.X * cos( angle ) + v.Y * -sin( angle ), v.X * sin( angle ) + v.Y * cos( angle ) );
}

//bool Inside( const sPoint &a, const sPoint &b, const sPoint &c, const sPoint &p )
//{
//	double deta = Det( b - a, p - a );
//	double detb = Det( c - b, p - b );
//	double detc = Det( a - c, p - c );
//	return deta <= EPS && detb <= EPS && detc <= EPS ||
//		   deta >= -EPS && detb >= -EPS && detc >= -EPS;
//}

void Translate( sPoint &p, const sPoint &a1, const sPoint &b1, const sPoint &c1, const sPoint &a2, const sPoint &b2, const sPoint &c2 )
{
	double det1 = Det( b1 - a1, c1 - a1 );
	double det2 = Det( b2 - a2, c2 - a2 );

	double angle = Angle( b1 - a1, p - a1 );

	if( det1 >= 0 && det2 <= 0 ||
		det1 <= 0 && det2 >= 0 )
		angle = -angle;

	sVector ap = Abs( p - a1 ) / Abs( b1 - a1 ) * ( b2 - a2 );
	ap = Rotate( ap, angle );
	p = a2 + ap;
}

bool Result;
sPoint Answer;

void Work()
{
	//sPoint sector[ 6 ][ 2 ] =
	//{
	//	{ sPoint( X11, Y11 ), sPoint( X12, Y12 ) },
	//	{ sPoint( X12, Y12 ), sPoint( X13, Y13 ) },
	//	{ sPoint( X13, Y13 ), sPoint( X11, Y11 ) },
	//	{ sPoint( X21, Y21 ), sPoint( X22, Y22 ) },
	//	{ sPoint( X22, Y22 ), sPoint( X23, Y23 ) },
	//	{ sPoint( X23, Y23 ), sPoint( X21, Y21 ) }
	//};

	//int i, j;

	//Result = true;

	//for( i = 0; i < 6; ++i )
	//{
	//	for( j = i + 1; j < 6; ++j )
	//	{
	//		if( Cross( sector[ i ][ 0 ], sector[ i ][ 1 ], sector[ j ][ 0 ], sector[ j ][ 1 ], Answer ) )
	//		{
	//			if( Inside( sPoint( X11, Y11 ), sPoint( X12, Y12 ), sPoint( X13, Y13 ), Answer ) &&
	//				Inside( sPoint( X21, Y21 ), sPoint( X22, Y22 ), sPoint( X23, Y23 ), Answer ) )
	//			{
	//				return;
	//			}
	//		}				
	//	}					
	//}
	//Result = false;

	//sVector x( 1, 0 );
	//sVector y( 0, 1 );

	//sVector z = Rotate( x, Angle( x, y ) );

	Result = true;
	
	sPoint answer = sPoint( ( X21 + X22 + X23 ) / 3., ( Y21 + Y22 + Y23 ) / 3. );
	do
	{
		Answer = answer;
		Translate( answer, sPoint( X11, Y11 ), sPoint( X12, Y12 ), sPoint( X13, Y13 ), sPoint( X21, Y21 ), sPoint( X22, Y22 ), sPoint( X23, Y23 ) );
	} while( fabs( Answer.X - answer.X ) > EPS ||
		   fabs( Answer.Y - answer.Y ) > EPS );
	Answer = answer;
}

void Write( int i )
{
	printf( "Case #%d: ", i );
	if( Result )
		printf( "%.6lf %.6lf\n", Answer.X, Answer.Y );
	else
		puts( "No Solution" );
}

int main()
{
	int i, n;
	scanf( "%d", &n );
	for( i = 1; i <= n; ++i )
	{
		Read();
		Work();
		Write( i );
	}
	return 0;
}
