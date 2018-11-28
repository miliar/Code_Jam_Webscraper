#include <iostream>

using namespace std;


class CFraction
{
public:
int iNumerator;
int iDenominator;
double dValue;

//constructor...
CFraction( int iNumeratorParam, int iDenominatorParam )
{
	iNumerator = iNumeratorParam;
	iDenominator = iDenominatorParam;
	dValue = iNumerator/ iDenominator;
}


CFraction reduce()
{
	int iGCD = getGCD(iNumerator,iDenominator);
	CFraction retVal( iNumerator/iGCD, iDenominator/iGCD );
	return retVal;
}

int getNumerator()
{
	return iNumerator;
}
int getDenominator()
{
	return iDenominator;
}

private:
//private method to get GCD
	int getGCD( int iNum1, int iNum2 )
	{
		int remainder = iNum2 % iNum1;
		if ( remainder != 0 )
			return getGCD( remainder,iNum1 );
		return iNum1;
	}
};
int main()
{
	int T,N, PD, PG;
	int success = 0,test;

	cin >> T;
	for ( int i = 0; i < T; i++)
	{
		success = 1;
		cin >> N;
		cin >> PD;
		cin >> PG;

		if ( PG == 0 && PD != 0 )
		{
			success = 0;
		}
		else if ( PD != 100 && PG == 100 )
		{
			success = 0;
		}
		else
		{
			if ( PD == 0 ){
				success = 1;
			}
			else
			{
			CFraction temp(PD,100);
			CFraction reduced = temp.reduce();
			if ( reduced.getDenominator() <= N )
			{
				success = 1;
			}
			else
			{
				success = 0;
			}
			}
		}
		cout << "Case #" << i+1 <<": "<<(success? "Possible":"Broken") << endl;

	}
}
