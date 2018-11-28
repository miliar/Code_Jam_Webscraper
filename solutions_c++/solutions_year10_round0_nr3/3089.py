#include <fstream>
#include <deque>
#include <sstream>

using namespace std;

int main()
{
	ifstream InFile("C-small-attempt0.in");
	ofstream OutFile("C-small-result.in");
	int num;
	InFile>>num;
	deque<unsigned int> uDeq;
	for (int i=0;i<num;++i)
	{
		uDeq.clear();
		unsigned int R,k,N;
		//string paraLine,deqLine;
		//getline(InFile,paraLine);
		//stringstream paraStrm(paraLine);
		if (InFile>>R>>k>>N)
		{
			//getline(InFile,deqLine);
			//stringstream deqStrm(deqLine);
			unsigned int personNum;
			for (int j=0;j<N;++j)
			{
				InFile>>personNum;
				uDeq.push_back(personNum);
			}
		}

		unsigned int oneTimePerson;
		unsigned int totalMoney = 0;
		for (int j=0;j<R;++j)
		{
			oneTimePerson = 0;
			unsigned int temp = 0;
			deque<unsigned int>::const_iterator it = uDeq.begin();
			int deqLength = uDeq.size();
			for (int n=0;it != uDeq.end();)
			{
				temp = uDeq.front();
				if (oneTimePerson + temp <= k)
				{
					oneTimePerson += temp;
					uDeq.push_back(temp);
					++it;
					uDeq.pop_front();
					++n;
					if (deqLength == n)
					{
						totalMoney += oneTimePerson;
						break;
					}
				}
				else
				{
					totalMoney += oneTimePerson;
					break;
				}		
			}
		}


		OutFile<< "Case #" << i+1 << ": " <<totalMoney<<endl;

	}
	return 0;
}