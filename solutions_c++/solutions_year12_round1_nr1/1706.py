#include <iostream>


using namespace std;


void main()
{
	int l_testCases;
	cin>>l_testCases;

	for (int caseIndex = 0; caseIndex < l_testCases; ++caseIndex)
	{
		int typed = 0;
		int total = 0;
		cin>>typed>>total;
		double * probArray = new double[typed];
		double * typedArray =  new double[typed];

		double currentProb = 1;

		for (int i=0; i < typed; ++i)
		{
			double tmp = 0;
			cin>>tmp;
			currentProb *= tmp;
			typedArray[i] = tmp;
			probArray[i]  = currentProb;
		}

		double res = (total - typed + 1 ) * currentProb + (total - typed + total + 2) * (1 - currentProb);

		if (res > total + 2)
			res = total + 2;

		double currentErrProb = 1 - typedArray[typed - 1];
		for (int i = typed - 1; i > 0; --i)
		{
			int retype = total + 1;
			int backspaces = typed - i;
			int strokes  = backspaces + total - i + 1;
			double currentRes = (strokes) * probArray[i -1 ] + (strokes + retype) * (1 - probArray[i -1 ]);
			if (res > currentRes) res = currentRes;
			currentErrProb*= 1 - typedArray[i];
		}
		cout<<"Case #"<<(caseIndex +1)<<": "<<res<<endl;
		delete [] probArray;
		delete [] typedArray;
	}
}