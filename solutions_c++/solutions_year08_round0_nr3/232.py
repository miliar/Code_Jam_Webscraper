#include <iostream>
#include <string>
#include <cmath>
using namespace std;

void do_case(int n);
char skip[100];
long double  calcul( long double x1, long double y1, long double y2,
	long double a, long double b, long double wk_R );
long double  integral( long double wk_R, long double a, long double b );

int main(int , char **)
{
	int  ncases;
	cin >> ncases;
	cin.getline(skip,100);

	for (int i=0; i<ncases; i++)
		do_case(i);

	return 0; 
}

long double  in_f, in_R, in_t, in_r, in_g;

void do_case(int n)
{
	//
	// input
	//
	cin >> in_f >> in_R >> in_t >> in_r >> in_g;
	cin.getline(skip,100);


	//
	// process
	//
	
	
	const long double WK_PI = 3.14159265358979323846L;
	long double ans = WK_PI*in_R*in_R/4.0;
	long double squares = 0.0;
	
	long double wk_R = in_R - in_t - in_f;
	long double wk_r = in_r + in_f;
	long double wk_g = in_g - 2*in_f;	
	long double kan = wk_g + 2*wk_r;
	if ( wk_g <= 0.0 )
	{
		ans = 1.0;
	}
	else if ( wk_R*wk_R <= 2.0*wk_r*wk_r )
	{
		ans = 1.0;
	}
	else {
		
		int max_k = int(( sqrt( wk_R*wk_R - wk_r*wk_r ) - wk_r )/kan);
		for (int k=0; k<=max_k; k++)
		{
			long double  a = wk_r+wk_g;
			long double  b = wk_r+wk_g + k*kan;
			long double  c = wk_r + k*kan;
			int max_l = -1;
			if ( a*a + b*b <= wk_R*wk_R )
			{
				max_l = int(( sqrt(wk_R*wk_R - b*b) - a)/kan);
			}
	
			// add simple square area
			squares += wk_g*wk_g * (max_l+1);
	
			int max_l2 = int(( sqrt(wk_R*wk_R - c*c) - wk_r)/kan);
	
			// breaken squares
			for (int l=max_l+1; l<=max_l2; l++)
			{
				// calculate breaken square area
				long double x1 = wk_r + k*kan;  // left lower
				long double y1 = wk_r + l*kan;  // left lower
				long double x2 = wk_r + wk_g + k*kan;  // right lower
				long double y2 = wk_r + wk_g + l*kan;  // left upper
				long double t = wk_R*wk_R - y2*y2;
				long double a;
				if ( t < 0 || sqrt(t) < x1 )
					a = x1;
				else
					a = sqrt(t);
					
				long double b = sqrt( wk_R*wk_R - y1*y1 );
				if ( b > x2 )
					b = x2;
				long double area = calcul( x1, y1, y2,	a, b, wk_R );
				
				// add it
				squares += area;
			}		
		}
		
		ans = (ans - squares)/ans;
	}
		
	//
	// output
	//
//	cout << "Case #" << n+1 << ": " << ans << endl;
	printf("Case #%d: %8.6Lf\n", n+1, ans);

//	cout << in_f << " " << in_R << " " 
//		<< in_t << " " << in_r << " " << in_g << endl;
//	printf("%25.20Lf %25.20Lf %25.20Lf %25.20Lf %25.20Lf %25.20Lf\n",
//		in_f, in_R, in_t, in_r, in_g );
}


long double  calcul( long double x1, long double y1, long double y2,
	long double a, long double b, long double wk_R )
{
	long double  area = 0.0L;
	if ( a > x1 )
		area += (a-x1)*(y2-y1);
	area += integral(wk_R, a, b) - y1*(b-a);
	return  area;
}

long double  integral( long double wk_R, long double a, long double b )
{
//	a = a/wk_R;
//	b = b/wk_R;
	long double t = wk_R*wk_R*asin(b/wk_R)/2.0L + b/2.0L*sqrt(wk_R*wk_R-b*b);
	t -= wk_R*wk_R*asin(a/wk_R)/2.0L + a/2.0L*sqrt(wk_R*wk_R-a*a);
//	t = t*wk_R*wk_R;
	return  t;
}
