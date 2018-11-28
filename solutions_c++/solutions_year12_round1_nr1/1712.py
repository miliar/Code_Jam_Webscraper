#include<fstream>
#include<vector>
#include<algorithm>
#include<iomanip>

using namespace std;

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int T, A, B;
	int i,j;
	double P1 = 0, P2 = 0, P3 = 0;
	double except = 0;
	double except1 = 0;
	double except2 = 0;
	double except3 = 0;

	double tmp = 0;
	vector<double> need;

	fin >> T;

	for(i = 0; i != T; ++i)
	{
		need.clear();
		fin >> A >> B;
		if(A == 1)
		{
			fin >> P1;
			if(B+2 > 2*B+1 - P1*(B+1))
				except =2*B+1 - P1*(B+1);
			else
				except = B+2;
			 fout<<"Case #" << i+1 << ": " << setprecision(6)<<setiosflags(ios::fixed | ios::showpoint) <<  except << endl;
		}
		else
		{
			if(A == 2)
			{
				fin >> P1 >> P2;
				except1 = (B-1)*P1*P2 + (2*B-1)*(1-P1*P2);
				except2 = (B+1)*(2-P1);
				except3 = B+2;
				need.push_back(except1);
				need.push_back(except2);
				need.push_back(except3);
				sort(need.begin(),need.end());
				fout<<"Case #" << i+1 << ": " << setprecision(6)<<setiosflags(ios::fixed | ios::showpoint) <<  need[0] << endl;
			}

			else
			{
				fin >> P1 >> P2 >> P3;
				except1 = (B-2)*P1*P2*P3 + (2*B-1)*(1-P1*P2*P3);
				except2 = B*P1*P2 + (2*B+1)*(1 - P1*P2);
				except3= B+2;
				need.push_back(except1);
				need.push_back(except2);
				need.push_back(except3);
				sort(need.begin(),need.end());
				 fout<<"Case #" << i+1 << ": " << setprecision(6)<<setiosflags(ios::fixed | ios::showpoint) <<  need[0] << endl;
			}
		}
	}

	return 0;
}


