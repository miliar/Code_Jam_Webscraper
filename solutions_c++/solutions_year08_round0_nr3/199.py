#include <cmath>
#include "FlySwatter.h"

const double EPSILON = 10E-6;
const double PI      = 4.0*atan(1.0);

FlySwatter::FlySwatter(const double f, const double R, const double t, const double r, const double g)
{
	flyRadius			= f;
	racquetOuterRadius	= R;
	racquetThickness	= t;
	stringRadius		= r;
	gap					= g;

	racquetInnerRadius	= R-t-f;
	cellSize			= 2*r+g;
	notHitSize			= g-2*f;
}

double FlySwatter::computeNotHitProbabilityForNotClippedCell()
{
	double numerator = notHitSize;
	double denom     = cellSize;

	if(numerator < 0)
		numerator = 0;

	return (numerator*numerator)/(denom*denom);
}

double FlySwatter::computeUpperAreaSize(const int diagonalMaxIndex)
{
	int currentXIndex = 0;
	double totalNotHitArea = 0;
	
	double racquetInnerRadiusSqaure = racquetInnerRadius * racquetInnerRadius;
	double cellSizeSquare = cellSize * cellSize;
	while(currentXIndex < diagonalMaxIndex)
	{
		double y0 = sqrt(racquetInnerRadiusSqaure - 
						 currentXIndex*currentXIndex*cellSizeSquare);
		double y1 = sqrt(racquetInnerRadiusSqaure - 
						 (currentXIndex+1)*(currentXIndex+1)*cellSizeSquare);
		int y0Index = (int)(y0/cellSize);
		int y1Index = (int)(y1/cellSize);
		if(y0Index == y1Index)
		{
			RacquetCell cell(currentXIndex, y0Index, this);
			totalNotHitArea += cell.getNotHitAreaSize();

			totalNotHitArea += (y0Index - diagonalMaxIndex) * (notHitSize*notHitSize);
		}
		else
		{
			RacquetCell cell0(currentXIndex, y0Index, this);
			totalNotHitArea += cell0.getNotHitAreaSize();

			RacquetCell cell1(currentXIndex, y1Index, this);
			totalNotHitArea += cell1.getNotHitAreaSize();

			totalNotHitArea += (y1Index - diagonalMaxIndex) * (notHitSize*notHitSize);
		}

		++currentXIndex;
	}

	double y0 = sqrt(racquetInnerRadiusSqaure - 
					 diagonalMaxIndex*diagonalMaxIndex*cellSizeSquare);
	if(y0 > (diagonalMaxIndex+1)*cellSize)
	{
		RacquetCell cell(diagonalMaxIndex, diagonalMaxIndex+1, this);
		totalNotHitArea += cell.getNotHitAreaSize();
	}

	return totalNotHitArea;
}

double FlySwatter::solve()
{
	// 1. compute prob for not clipped cell
	double notHitProbabilityForNotClippedCell = computeNotHitProbabilityForNotClippedCell();
	if(notHitProbabilityForNotClippedCell < EPSILON)
		return 1.0;
	else if(notHitProbabilityForNotClippedCell > 1.0-EPSILON)
		return 0.0;

	double totalNotHitAreaSize = 0;
	double totalAreaSize = PI * racquetOuterRadius * racquetOuterRadius / 4;

	// 2. find the max diagonal index
	int diagonalMaxIndex = (int)(racquetInnerRadius/(sqrt(2.0)*cellSize));

	// 3. compute area size of largest square
	double largestSquareSize = (cellSize*diagonalMaxIndex) * 
							   (cellSize*diagonalMaxIndex);

	double notHitAreaSizeForSquareArea = notHitProbabilityForNotClippedCell * largestSquareSize;
	totalNotHitAreaSize += notHitAreaSizeForSquareArea;

	// 4. compute area size of max diagonal cell
	RacquetCell maxDiagonalCell(diagonalMaxIndex, diagonalMaxIndex, this);
	totalNotHitAreaSize += maxDiagonalCell.getNotHitAreaSize();

	// 5. compute upper area's not hit area size
	double notHitAreaSizeForUpperArea = computeUpperAreaSize(diagonalMaxIndex);
	totalNotHitAreaSize += 2*notHitAreaSizeForUpperArea;

	return 1.0-(totalNotHitAreaSize/totalAreaSize);
}

FlySwatter::RacquetCell::RacquetCell(const int xIndex, const int yIndex, FlySwatter* parent)
{
	x0 = xIndex * parent->cellSize;
	y0 = yIndex * parent->cellSize;
	x1 = (xIndex+1) * parent->cellSize;
	y1 = (yIndex+1) * parent->cellSize;

	gapx0 = x0 + parent->stringRadius + parent->flyRadius;
	gapy0 = y0 + parent->stringRadius + parent->flyRadius;
	gapx1 = x1 - parent->stringRadius - parent->flyRadius;
	gapy1 = y1 - parent->stringRadius - parent->flyRadius;

	this->parent = parent;
}

double FlySwatter::RacquetCell::getNotHitAreaSize()
{
	double y0Pos = sqrt(parent->racquetInnerRadius*parent->racquetInnerRadius -
						gapx0*gapx0);
	double y1Pos;
	double y1Square = parent->racquetInnerRadius*parent->racquetInnerRadius -
					  gapx1*gapx1;
	if(y1Square >= 0)
		y1Pos = sqrt(y1Square);
	else
		y1Pos = sqrt(-y1Square);

	if(y0Pos >= gapy0 && y0Pos <= gapy1)
	{
		if(y1Pos >= gapy0 && y1Pos <= gapy1)
		{
			return getIntegralValueWithInnerRadius(gapx0, gapx1) - (gapx1-gapx0)*gapy0;
		}
		else if(y1Pos <= gapy0)
		{
			double gapxc = sqrt(parent->racquetInnerRadius*parent->racquetInnerRadius -
								gapy0*gapy0);
			return getIntegralValueWithInnerRadius(gapx0, gapxc) - (gapxc-gapx0)*gapy0;
		}
	}
	else if(y0Pos >= gapy1)
	{
		if(y1Pos >= gapy0 && y1Pos <= gapy1)
		{
			double gapxc = sqrt(parent->racquetInnerRadius*parent->racquetInnerRadius -
								gapy1*gapy1);
			return (gapxc-gapx0)*(gapy1-gapy0) +
				   getIntegralValueWithInnerRadius(gapxc, gapx1) - (gapx1-gapxc)*gapy0;
		}
		else if(y1Pos >= gapy1)
		{
			return (gapx1-gapx0)*(gapy1-gapy0);
		}
	}
	
	return 0;
}

double FlySwatter::RacquetCell::getIntegralValueWithInnerRadius(const double xFrom, const double xTo)
{
	double tFrom = acos(xFrom / parent->racquetInnerRadius);
	double tTo   = acos(xTo   / parent->racquetInnerRadius);

	double retValue = tTo   - 0.5 * sin(2*tTo)
		            -(tFrom - 0.5 * sin(2*tFrom));
	retValue *= (-0.5 * parent->racquetInnerRadius * parent->racquetInnerRadius);
	return retValue;
}