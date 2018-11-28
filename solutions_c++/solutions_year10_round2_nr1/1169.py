/*
 * Olaf "Ritave" Tomalka
 * Google Code Jam 2010
 *
 * Dfs it adding only the edges that are in the path
 */
#include <iostream>
#include <vector>
#include <string>

int n,m,answer=0;
std::vector<std::string> question;		// The path we're working on right now

struct Edge
{
	int parent;
	//std::vector<int> index;			 Index in vector which we should go to where depth+1 and width=index
	std::string name;			// Name of the edge
};

std::vector< std::vector<Edge> > G;		// The graph [a][b] - a is height, b is width of the graph;


void DebugGrafWrite()
{
        std::cout << "Answer:" << answer << '\n';
	for (int i=0;i<G.size();i++)
	{
		for (int j=0;j<G[i].size();j++)
		{
			std::cout << G[i][j].name << ' ';
		}
		std::cout << std::endl;
	}
}

void AddToGraf()				// Which depth of tree should we look at
{
	int Parent=-1;
	for (int i=0;i<question.size();i++)	// Depth
	{
		bool wasFound=false;
		if (i<G.size())			// Already need to create the graf
		{
			for (int j=0;j<G[i].size();j++)
			{
				if (G[i][j].name==question[i] && Parent==G[i][j].parent)
				{
					wasFound=true;	// Don't add to the answer, it exists
					Parent=j;
					break;
				}
			}
		}
		if (!wasFound)			// We need to create it
		{
			// As the folder doesn't exist, all below doesn't either
			// So we popullate the branch, and make parents and indexes
                        if (G.size()<question.size())
                            G.resize(question.size());
                        for (int j=i;j<question.size();j++)
			{
				/*if (j>=G.size())
				{
					G.resize(G.size()+1);
				}*/
                                //std::cout << j << ' ' << std::flush;
                                //DebugGrafWrite();
				Edge temp;
				temp.parent=Parent;
				temp.name=question[j];
				Parent=G[j].size();
				G[j].push_back(temp);
			}
			answer+=question.size()-i;	// The lenght of the branch created
			return;
		}
	}
}

int main()
{
	std::ios::sync_with_stdio(0);
        int t;
        std::cin >> t;
        for (int k=0;k<t;k++)
        {
            answer=0;
            G.clear();
            std::cin >> n >> m;
            for (int i=0;i<n;i++)
            {
		std::string tempBuffer;
		std::string read;
		std::cin >> read;

		for (int i=1;i<=read.length();i++)
		{
			if (read[i]=='/' || i==read.length())
			{
				question.push_back(tempBuffer);
				tempBuffer.clear();
			} else
				tempBuffer+=read[i];
		}
		AddToGraf();
		question.clear();
            }
            //DebugGrafWrite();
            answer=0;				// We clear it, as it was used in function

            for (int i=0;i<m;i++)
            {
		std::string tempBuffer;
		std::string read;
		std::cin >> read;

		for (int i=1;i<=read.length();i++)
		{
			if (read[i]=='/' || i==read.length())
			{
				question.push_back(tempBuffer);
				tempBuffer.clear();
			} else
				tempBuffer+=read[i];
		}
		AddToGraf();
		question.clear();
            }
            std::cout << "Case #" << k+1 << ": " << answer << '\n';
        }
}
