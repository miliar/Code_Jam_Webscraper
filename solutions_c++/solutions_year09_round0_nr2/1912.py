#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <set>
using namespace std;

class Watersheds
{
public:
	int T;
	static int direction[4][2];
	void run()
	{
		ifstream in("B-large.in");
		ofstream out("B-large.out");
		in>>T;
		for (int i=0; i<T; i++)
		{
			int H, W;
			in>>H>>W;
			char** result = new char*[H];
			int**  altitudes = new int*[H];
			for (int j=0; j<H; j++)
			{
				result[j] = new char[W];
				altitudes[j] = new int[W];
			}
			for (int j=0; j<H; j++)
			{
				for (int k=0; k<W; k++)
				{
					in>>altitudes[j][k];
					result[j][k] = '\0';
				}
			}

			int sinkCount = 0;
			multimap<std::pair<int,int>, std::pair<int, int> >reverseFlow;
			for (int j=0; j<H; j++)
			{
				for (int k=0; k<W; k++)
				{
					bool isSink = true;
					int tmp = ~(1<<31);
					std::pair<int, int> flowTo;
					for (int l=0; l<4; l++)
					{
						int x = j+direction[l][0];
						int y = k+direction[l][1];
						if (x<0 || x >=H || y<0 || y>=W)
							continue;
						if (altitudes[x][y] < altitudes[j][k] && altitudes[x][y] < tmp)
						{
							isSink = false;
							tmp = altitudes[x][y];
							flowTo.first = x;
							flowTo.second = y;
						}
					}
					if (isSink)
					{
						result[j][k] = 'A' + sinkCount;
						sinkCount++;
					}
					else
					{
						reverseFlow.insert(std::make_pair(flowTo, std::make_pair(j, k)));

					}
				}
			}

			std::set<std::pair<int, int> > toDelete;
			while(!reverseFlow.empty())
			{
				toDelete.clear();
				multimap<std::pair<int, int>, std::pair<int, int> >::iterator itr =reverseFlow.begin();
				for (; itr!=reverseFlow.end(); itr++)
				{
					if(result[itr->first.first][itr->first.second] == '\0')
						continue;
					result[itr->second.first][itr->second.second] = result[itr->first.first][itr->first.second];
					toDelete.insert(itr->first);
				}
				for (std::set<std::pair<int, int> >::iterator itr = toDelete.begin(); itr!=toDelete.end(); itr++)
				{
					reverseFlow.erase(std::make_pair(itr->first, itr->second));
				}
			}

			map<char, char > changeName;
			map<char, char >::iterator changeItr;
			sinkCount = 0;
			for (int j=0; j<H; j++)
			{
				for (int k=0; k<W; k++)
				{
					changeItr = changeName.find(result[j][k]);
					if (changeItr == changeName.end())
					{
						changeName.insert(std::make_pair(result[j][k], 'a' + sinkCount));
						result[j][k] = 'a' + sinkCount;
						sinkCount++;
					}
					else
					{
						result[j][k] = changeItr->second;
					}
				}
			}
			out<<"Case #"<<i+1<<":"<<endl;
			for (int j=0; j<H; j++)
			{
				for (int k=0; k<W-1; k++)
				{
					out<<result[j][k]<<" ";
				}
				out<<result[j][W-1]<<endl;
			}
			for (int j=0; j<H; j++)
			{
				delete(altitudes[j]);
				delete(result[j]);
			}
			delete(altitudes);
			delete(result);
		}
	}
};

int Watersheds::direction[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int main(int argc, char** argv)
{
	Watersheds ws;
	ws.run();
}
