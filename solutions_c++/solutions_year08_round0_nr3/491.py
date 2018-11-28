#include <iostream>
#include <math.h>
#include <windows.h>

using namespace std;

//Converted from perl for various lame reasons, thus holds much perl hackiness.

//Really should refactor this to use a point or vector struct.
double distance(double x1, double y1, double x2, double y2)
{
	return (sqrt( (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1) ) );
}


double getchordsquareareadelta(double x1, double y1, double x2, double y2, double edge)
{
	double areadelta = ( (y2 - y1) * (x1 - x2) / 2);
	//add triangle.

	//calculate chord: arc(from arcsine*2)*radius - sin*cos
	double chordlength = distance(x1, y1, x2, y2);

	double sine = chordlength / (2*edge);

	double arc = asin(sine);

	double arcarea = arc * edge * edge; //we double it, but arc to area is arc*r^2/2

	areadelta -= arcarea;

	double sincosarea = sine * cos(arc) *  edge * edge;

	areadelta += sincosarea;

	return areadelta;	

}

double getborder(double x, double totalradius)
{//gets the X corresponding to the Y of the outer fly-entrable points.
	double totalrsq = totalradius * totalradius;
	if(totalrsq < x*x)
	{
		DebugBreak();
	}
	return (sqrt(totalrsq - ( x * x ) ) );
}

bool inborder(double x, double y, double edge)
{	
	if(x >= edge || y >= edge)
	{
		return 0;
	}

	double ymax = getborder(x, edge);

	return (ymax >= y);
}


int main()
{
	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++)
	{
		double f, R, t, r, g, proportion;
		cin >> f >> R >> t >> r >> g;

		if(f*2 >= g)
		{
			//if the fly doesn't fit in the holes, give up.
			proportion = 1.0;
			goto end;
		}

		double spread = g + 2*r; //how spaced are the rectangles.

		double bottomoffset = r + f; //how far we have to move before fly can get through.
		double topoffset = spread - bottomoffset; //how far up the fly can through the square.

		double topbottom = topoffset - bottomoffset;

		double tbsq = topbottom * topbottom; //fly entrable zone on a full square.

		double edge = R - t - f; //edge of the fly-entrable zone; see totalradius

		int maxsquare = int( (edge/spread) + 1 ); //how far we gotta go.

		double flyarea = 0;

		for(int sx = 0; sx < maxsquare; sx++)
		{
			for(int sy = 0; sy < maxsquare; sy++)
			{
				double x = spread*sx + bottomoffset;
				double y = spread*sy + bottomoffset;

				double topx = x + topbottom;
				double topy = y + topbottom;

				if(inborder(x, y, edge) == 0)
				{
					continue;
				}
				if(inborder(topx, topy, edge) )
				{
					flyarea += tbsq;
					continue;
				}

				//Ok, we have a hard case.  Figure out where the chord is, and handle it!
				if(inborder(x, topy, edge) )
				{//if the opposite corner is inborder, we have a dogear.  Otherwise, a trapezoid.
					if(inborder(y, topx, edge) )
					{//dogear
						//figure out the endpoints of the curve.
						double eary = getborder(topx, edge);
						double earx = getborder(topy, edge);
						flyarea += tbsq;
						flyarea -= getchordsquareareadelta(topx, eary, earx, topy, edge);				}
					else
					{//trapezoid--code duplicated for other case of this.
						/*
						double earytop = getborder(topx, edge);
						double earybottom = getborder(x, edge);
						flyarea += topbottom*(earybottom - y);
						flyarea -= getchordsquareareadelta(topx, earytop, x, earybottom, edge);
						*/
						double earxtop = getborder(topy, edge);
						double earxbottom = getborder(y, edge);
						flyarea += topbottom*(earxbottom - x);
						flyarea -= getchordsquareareadelta(earxtop, topy, earxbottom, y, edge);
					}				
				}
				else
				{//x isn't in border-- either a roundoff, or a trapezoid
					if(inborder(y, topx, edge) )
					{ //y is inside--trapezoid
/*
						double earxtop = getborder(topy, edge);
						double earxbottom = getborder(y, edge);
						flyarea += topbottom*(earxbottom - x);
						flyarea -= getchordsquareareadelta(earxtop, topy, earxbottom, y, edge);
*/
						double earytop = getborder(topx, edge);
						double earybottom = getborder(x, edge);
						flyarea += topbottom*(earybottom - y);
						flyarea -= getchordsquareareadelta(topx, earytop, x, earybottom, edge);

					}
					else
					{ //dogear.
						double topy = getborder(x, edge);
						double topx = getborder(y, edge);
						flyarea += (topx - x)*(topy - y);
						flyarea -= getchordsquareareadelta(topx, y, x,topy, edge);
						
					}
				}



			}
		}

		// "totla fly flyarea\n"; #debug

		//area = pi/4 * r^2

		double totalarea = 3.1415926535 * R * R;
		proportion = 1 - (4*flyarea/totalarea);
		
end:
		cout<< "Case #" << i + 1 <<": ";
		cout << proportion;
		cout << "\n";
	}
	//std::cout << "Hello World!";
	return 1;
}
