#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream input;
	input.open("A-large.in");
	
	ofstream output;
	output.open("output.txt");

	int T,N,button;
	char robot;

	input>>T;

	for(int i=0;i<T;++i)
	{
		int N;
		input>>N;
	
		int posO=1;
		int posB=1;
		vector <bool> isOrange;
		vector <int> listO,listB;
		isOrange.resize(N);

		for(int j=0;j<N;++j)
		{
			input>>robot;
			input>>button;

			if(robot=='O')
			{
				isOrange[j]=true;
				listO.push_back(button);
			}
			else
			{
				isOrange[j]=false;
				listB.push_back(button);
			}
		}

		output<<"Case #"<<i+1<<": ";
		int total=0;
		int lPosO=0;
		int lPosB=0;

		for(int j=0;j<N;++j)
		{
			int sec=0;
			if(isOrange[j])
			{
				sec=abs(listO[lPosO]-posO)+1;
				total+=sec;
				posO=listO[lPosO];
				++lPosO;

				if(lPosB<listB.size())
				{
					int diff=abs(listB[lPosB]-posB);
					posB = sec > diff ?  listB[lPosB] : listB[lPosB]+(diff-sec);
				}
			}
			else
			{
				sec=abs(listB[lPosB]-posB)+1;
				total+=sec;
				posB=listB[lPosB];
				++lPosB;

				if(lPosO<listO.size())
				{
					int diff=abs(listO[lPosO]-posO);
					posO = sec > diff ?  listO[lPosO] : listO[lPosO]+(diff-sec);
				}
			}
		}

		output<<total<<endl;
	}
	
	input.close();
	output.close();

	return 0;
}