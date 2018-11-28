#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

double pi;

double areaSubCircle(double x1, double x2, double iR)
{
	assert(x1 <= x2);
	
	double alpha1 = acos(x1/iR), alpha2=acos(x2/iR);
	if (x1 < -iR) alpha1=pi;
	if (x2>iR) alpha2 = 0;
	
//	 cout << "x1: " << x1 << " x2: " << x2 << endl;
 //	 cout << "alpha1: " << alpha1/pi*180 << " alpha2: " << alpha2/pi*180 << endl;
	//  cout << "alpha1(rad): " << alpha1 << " alpha2(rad): " << alpha2 << endl;
	
	double area1 = alpha1;
	// cout << "Angular sector 1: " << area1*iR*iR << endl;
	double height1 = 1-x1*x1/(iR*iR);
	if (height1 < 0) height1 = 0;
	area1 -= (sqrt(height1)*x1/iR); // this addendum can be negative if x1<0
	
  // cout << "area1: " << area1*iR*iR << endl;
	
	double area2 = alpha2;
	double height2 = 1-((x2*x2)/(iR*iR));
	if (height2 < 0) height2 = 0;
	
//	cout << "Angular sector 2: " << area2*iR*iR << endl;
	area2 -= sqrt(height2)*x2/iR;
//	cout << "area2: " << area2*iR*iR << endl;

//	cout << "Area sub circle between " << x1 << " and " << x2 << ": " << (area1-area2)*iR*iR << endl;

	return (area1-area2)*iR*iR;
}

double hitArea(double f, double R, double t, double r, double g)
{
	//cout << "Original interval size: " << g << endl;
	
	double iR = R-t-f; // inner radius (we do not count the radius of the fly as if the center is t+f away from the border it hits it...)
	g = g-2*f;
	r = r+f;
	
	if (iR <= 0 || g <= 0) { // fly is too big
	//	cout << "Fly is too big" << endl;
		return pi*R*R;
	}
	
/*	cout << "Fly size: " << f << endl;
	cout << "Real inner radius: " << iR << endl;
	cout << "Real string size: " << r << endl;
	cout << "Real interval size: " << g << endl;
*/
	
	double rightArea = 0;
		
	for (double x1 = r+g; x1 < iR; x1+=(2*r+g)) {
		double x2 = min(x1+2*r, iR);
		rightArea += areaSubCircle(x1,x2,iR);
	}

//	cout << "Right vertical area " << rightArea << endl;
	
	// add left strings
	double verticalStringsArea = rightArea * 2;
	
	// add center string
	double centerString = areaSubCircle(-r, r, iR);

//	cout << "Center string: " << centerString << endl;

	verticalStringsArea += centerString;
	
//	cout << "Vertical area " << verticalStringsArea << endl;
	
	// add horizontal strings 
	
	rightArea = 0;
	for (double x1 = r+g; x1 < iR; x1+=(2*r+g)) {
		double x2 = x1+2*r;
		
		double heightAtX1 = sqrt((iR*iR-x1*x1));		
		
		for (double y1 = r; y1 < heightAtX1; y1+=(2*r+g)) {
			double y2 = y1+g;
			
	//		cout << "1 ("<<x1<<","<<y1<<")"<< " 2 ("<<x2<<","<<y2<<")" << endl;
			
			if (y2*y2+x2*x2 <= iR*iR) // if (x2,y2) in the circle 
			{
				rightArea += 2*g*2*r;
			} else if (y1*y1+x2*x2 < iR*iR) // the stripe is cut off horizontally (x2,y1) is in the circle
			{
				double stripeArea;
				
				if (x1*x1+y2*y2<=iR*iR) {
			//			cout << "x2 y2 is the only corner missing" << endl;
						double cutoffX = sqrt(iR*iR-y2*y2);
						stripeArea = 2*(cutoffX-x1)*(y2-y1);
						stripeArea += areaSubCircle(cutoffX, x2, iR) - 2*y1*(x2-cutoffX);
				}
				else 
				{
		//			cout << "Cut off horizontally";
					stripeArea =  areaSubCircle(x1,x2,iR);
		//			cout << "omit portion: " << 2*y1*(x2-x1) << endl;
					stripeArea -= 2*y1*(x2-x1);
				}
			
	//			cout << "Stripe area: " << stripeArea << endl;
			
				assert(stripeArea>=0);
					
				rightArea += stripeArea;
			}
			else  // strip if cut off vertically or both ways
			{				
				if (x1*x1+y2*y2>iR*iR) {
				// stripe is cut off both ways
	//				cout << "Stripe cut off both ways" << endl;
					y2 = heightAtX1;
				} 
				else
				{
		//			cout << "Stripe is cut off vertically" << endl;
				}
				
				double stripeArea =  areaSubCircle(y1,y2,iR);
		//		cout << "omit portion: " << 2*(y2-y1)*x1 << endl;
				stripeArea -= 2*(y2-y1)*x1;
				
			//	cout << "Stripe area: " << stripeArea << endl;
				
				assert(stripeArea>=0);
				
				rightArea += stripeArea;
			}
		}
	}
	
//	cout << "Horizontal upper area " << rightArea << endl;

	double horizontalStringsArea = rightArea * 2;

	// add center string
	for (double y1 = r; y1 < iR; y1+=(2*r+g)) {
		double y2 = y1+g;
		if (y2 > iR) {
			horizontalStringsArea += areaSubCircle(-r, r, iR) - 2*y1*2*r;
		}
		else
		{
			horizontalStringsArea += 2*g*2*r;
		}
	}
	
//	cout << "Horizontal total area " << horizontalStringsArea << endl;

			
	// omit center square, add border, add 
	double totalStringsArea = verticalStringsArea+horizontalStringsArea+pi*((t+f)*(R+iR));
	
//	cout << "Strings area " << totalStringsArea << endl;
	
	return totalStringsArea;
}

int main(void)
{
	int N;
	cin >> N;
	pi = atan(1)*4;
	for (int nCase = 0; nCase < N ; nCase++) {
		double f, t, R, r, g;

		cin >> f >> R >> t >> r >> g;
//		cout << f << " "<< R << " " << t << " " << r << " "<<  g << endl;
		
		printf("Case #%d: %1.7f\n", nCase+1, hitArea(f,R,t,r,g)/(pi*R*R));
		
	}
}