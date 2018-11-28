#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_LEN_LINE		100

#define PI					acos(-1.0)


double f;
double R;
double t;
double r;
double g;

double GetAbs(double x, double y)
{
	return sqrt(x*x + y*y);
}

double GetSectorPart(double dAngle, double dRadius)
{
	//double dResult = dAngle/(2*PI) * PI * dRadius*dRadius;
	double dSector = 0.5* dAngle * dRadius*dRadius;
	double dSideC = 2.0 * dRadius * sin(0.5*dAngle);
	double dSideH = dRadius * cos(0.5*dAngle);

	double dResult = dSector - 0.5*dSideC*dSideH;
	return dResult;
}

double GetArea(int x, int y)
{
	// square not in circle
	double dxmin = (2.0*x+1)*r + x*g + f;
	double dymin = (2.0*y+1)*r + y*g + f;
	double dxmax = (2.0*x+1)*r + (x+1)*g - f;
	double dymax = (2.0*y+1)*r + (y+1)*g - f;
	double dRadius = R-t-f;
	
	double dmin = GetAbs(dxmin, dymin);
	if (dmin >= dRadius)
		return 0.0;
	
	// square complete in circle
	double dmax = GetAbs(dxmax, dymax);
	if (dmax <= dRadius)
		return ((g-2.0*f)*(g-2.0*f));

	double ds1 = GetAbs(dxmax, dymin);
	double ds2 = GetAbs(dxmin, dymax);

	double dAreaCircle = 0.0;
	double dAreaTriangle = 0.0;
	if (ds1 >= dRadius && ds2 >=dRadius)
	{
		// only corner in circle (triangle)
		double dAngleUnder = asin(dymin/dRadius);
		double dSectorMaxX = dRadius * cos(dAngleUnder);
		double dAngleOver = asin(dxmin/dRadius);
		double dSectorMaxY = dRadius * cos(dAngleOver);
		double dAngleSector = 0.5*PI - dAngleUnder - dAngleOver;
		// first part of area
		dAreaCircle = GetSectorPart(dAngleSector, dRadius);

		// second part
		dAreaTriangle = 0.5 * (dSectorMaxX-dxmin) * (dSectorMaxY-dymin);
	}
	else if (ds1 >= dRadius && ds2 < dRadius)
	{
		// trapeze
		double dAngleUnder = asin(dymin/dRadius);
		double dSectorMaxXUnder = dRadius * cos(dAngleUnder);
		double dAngleUnderAndSector = asin(dymax/dRadius);
		double dSectorMaxXUpper = dRadius * cos(dAngleUnderAndSector);
		double dAngleSector = dAngleUnderAndSector - dAngleUnder;
		// first part of area
		dAreaCircle = GetSectorPart(dAngleSector, dRadius);

		// second part
		dAreaTriangle = 0.5 * ((dSectorMaxXUnder-dxmin) + (dSectorMaxXUpper-dxmin)) * (dymax-dymin);
	}
	else if (ds1 < dRadius && ds2 >= dRadius)
	{
		// trapeze
		double dAngleLowerAndSector = acos(dxmin/dRadius);
		double dSectorMaxYRight = dRadius * sin(dAngleLowerAndSector);
		double dAngleLower = acos(dxmax/dRadius);
		double dSectorMaxYLeft = dRadius * sin(dAngleLower);
		double dAngleSector = dAngleLowerAndSector - dAngleLower;
		// first part of area
		dAreaCircle = GetSectorPart(dAngleSector, dRadius);

		// second part
		dAreaTriangle = 0.5 * ((dSectorMaxYRight-dymin) + (dSectorMaxYLeft-dymin)) * (dxmax-dxmin);

	}
	else
	{
		// only corner is out of circle
		double dAngleUnder = acos(dxmax/dRadius);
		double dSectorY = dRadius * sin(dAngleUnder);
		double dAngleSectorAndUnder = asin(dymax/dRadius);
		double dSectorX = dRadius * cos(dAngleSectorAndUnder);
		double dAngleSector = dAngleSectorAndUnder - dAngleUnder;
		// first part of area
		dAreaCircle = GetSectorPart(dAngleSector, dRadius);

		// second part: rectangle - triangle
		dAreaTriangle = (g-2.0*f)*(g-2.0*f) - (0.5 *(dxmax-dSectorX)*(dymax-dSectorY));
	}

	return (dAreaCircle + dAreaTriangle);
}

int main(int argv, char *argc[])
{
	if (argv < 2)
		return -1;
	
	//int i;

	int iCountCases = 0;
	
	// read Input
	FILE *fInput = fopen(argc[1], "r");
	if (fInput == NULL)
		return -1;

	// output
	FILE *fOutput = fopen("output.txt", "w");
	if (fOutput == NULL)
	{
		fclose(fInput);
		return -1;
	}


	char strLine[MAX_LEN_LINE];
	// read first line
	if (fgets(strLine, MAX_LEN_LINE, fInput)==NULL)
	{
		// Fehler beim Lesen
		return -1;
	}


	iCountCases = atoi(strLine);

	int iCase = 1;
	while (fgets(strLine, MAX_LEN_LINE, fInput) != NULL)
	{
		char strZahl[15];
		int ipos = 0;
		int istart;
		// radius of fly
		istart = ipos;
		while (strLine[ipos] != ' ' && strLine[ipos] != '\n')
		{
			ipos++;
		}
		strncpy(strZahl, &strLine[istart], ipos-istart);
		strZahl[ipos-istart] = 0;
		f = atof(strZahl);

		ipos++;

		// outer radius
		istart = ipos;
		while (strLine[ipos] != ' ' && strLine[ipos] != '\n')
		{
			ipos++;
		}
		strncpy(strZahl, &strLine[istart], ipos-istart);
		strZahl[ipos-istart] = 0;
		R = atof(strZahl);

		ipos++;

		// thickness of ring
		istart = ipos;
		while (strLine[ipos] != ' ' && strLine[ipos] != '\n')
		{
			ipos++;
		}
		strncpy(strZahl, &strLine[istart], ipos-istart);
		strZahl[ipos-istart] = 0;
		t = atof(strZahl);

		ipos++;

		// radius of string
		istart = ipos;
		while (strLine[ipos] != ' ' && strLine[ipos] != '\n')
		{
			ipos++;
		}
		strncpy(strZahl, &strLine[istart], ipos-istart);
		strZahl[ipos-istart] = 0;
		r = atof(strZahl);

		ipos++;

		// gap between strings
		istart = ipos;
		while (strLine[ipos] != ' ' && strLine[ipos] != '\n')
		{
			ipos++;
		}
		strncpy(strZahl, &strLine[istart], ipos-istart);
		strZahl[ipos-istart] = 0;
		g = atof(strZahl);

		ipos++;
		
		// algorythm
		double dSumArea = 0.0;
		double dResult;
		if (f*2.0 >= g)
			dResult = 1.0;
		else if (r>=R-t)
			dResult = 1.0;
		else
		{
			double dx = (R-t+r)/(2.0*r+g)+1;
			int ix;
			if (dx<0)
				ix = 0;
			else
				ix = (int)dx;

			for (int i=0; i<ix; i++)
			{
				for (int j=0; j<ix; j++)
				{
					double dArea = GetArea(i, j);
					dSumArea += dArea;
				}
			}
			
			dResult = 1.0 - (4.0*dSumArea / (PI*R*R));
		}


		// Ausgabe
		fprintf(fOutput, "Case #%d: %.6f\n", iCase, dResult);
		iCase++;
	
	}

	fclose(fInput);
	fclose(fOutput);

	return 0;
}