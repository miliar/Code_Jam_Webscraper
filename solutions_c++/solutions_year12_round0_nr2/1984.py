#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	//ifstream in("E:\\GoogleCodeJam2012\\QRound\\B-small-attempt1.in");
	ifstream in("E:\\GoogleCodeJam2012\\QRound\\B-large.in");
	//ofstream out("E:\\GoogleCodeJam2012\\QRound\\b-small-out.txt");
	ofstream out("E:\\GoogleCodeJam2012\\QRound\\b-large-out.txt");

	if (in.is_open())
	{
		int cases;

	    in >> cases;

		for (int c = 1;c <= cases;++c)
		{
			int googlers, surprising, p, result = 0;

			in >> googlers >> surprising >> p;

			for (int i = 0;i < googlers;++i)
			{
				int num;

				in >> num;

				if (num >= p * 3 - 2)
				{
					++result;
				} 
				else if (num >= p * 3 - 4)
				{
					// Case : p, p-2, p-2
					if (surprising > 0 && num > 0)
					{
                        --surprising;
						++result;
					}
				}
			}

			out << "Case #" << c << ": " << result << endl;
		}
	}

	return 0;
}