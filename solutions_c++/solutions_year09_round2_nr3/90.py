#include <iostream>
#include <string>
#include <vector>

typedef std::vector<std::vector<std::vector<std::string> > > Matrix;

const int MAX = 500;

std::vector<std::string> M, queries;
Matrix curr, next;

bool mygreater(const std::string &s1, const std::string &s2)
{
    if (s1.size() > s2.size())
        return true;
    if (s1.size() < s2.size())
        return false;
    return s1 > s2;
}

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cout << "Case #" << t << ":\n";
        int W, Q;
        std::cin >> W >> Q;
        curr.clear();
        curr.resize(W);
        next.clear();
        next.resize(W);
        std::string s;
        std::getline(std::cin, s);
        M.clear();
        for (int i = 0 ; i < W ; ++i)
        {
            std::getline(std::cin, s);
            M.push_back(s);
            curr[i].resize(W);
            next[i].resize(W);
            for (int j = 0 ; j < W ; ++j)
            {
                curr[i][j].resize(MAX * 2);
                next[i][j].resize(MAX * 2);
            }
        }

        std::vector<int> q;
        q.resize(Q);
        for (int i = 0 ; i < Q ; ++i)
            std::cin >> q[i];

        // init first step
        for (int i = 0 ; i < W ; ++i)
            for (int j = 0 ; j < W ; ++j)
            {
                if (M[i][j] >= '0' && M[i][j] <= '9')
                {
                    curr[i][j][M[i][j] - '0' + MAX].push_back(M[i][j]);
                }
            }

        queries.clear();
        queries.resize(MAX * 2);

        //int moves = 10;
        while (true)
        {
/*            for (int i = 0 ; i < W ; ++i)
            {
                for (int j = 0 ; j < W ; ++j)
                {
                    for (int k = 0 ; k < MAX * 2 ; ++k)
                        if (!curr[i][j][k].empty())
                            std::cout << k - MAX << ",";
                    std::cout << "\t";
                }
                std::cout << "\n";
            }
            std::cout << "\n";
*/
            for (int i = 0 ; i < W ; ++i)
            {
                for (int j = 0 ; j < W ; ++j)
                    for (int k = 0 ; k < MAX * 2 ; ++k)
                    if (!curr[i][j][k].empty() 
                        && (queries[k].empty() || mygreater(queries[k], curr[i][j][k])))
                    {
                        queries[k] = curr[i][j][k];
                    }
            }
            int num = 0;
            for (int i = 0 ; i < Q ; ++i)
            {
                if (!queries[q[i] + MAX].empty())
                    ++num;
            }
            if (num == Q)
                break;
            for (int i = 0 ; i < W ; ++i)
            {
                for (int j = 0 ; j < W ; ++j)
                {
                    next[i][j].clear();
                    next[i][j].resize(MAX * 2);
                }
            }

            const int dx[4]={-1, 1, 1,-1};
            const int dy[4]={-1,-1, 1, 1};
            const int dx1[4]={-1, 1, 0, 0};
            const int dy1[4]={ 0, 0,-1, 1};
            for (int i = 0 ; i < W ; ++i)
            {
                for (int j = 0 ; j < W ; ++j)
                {
                    for (int sum = 0 ; sum < MAX * 2 ; ++sum)
                    {
                        if (!curr[i][j][sum].empty())
                        {
                            for (int k = 0 ; k < 4 ; ++k)
                            {
                                // goto next cell
                                int ii = i + dx[k];
                                int jj = j + dy[k];
                                if (ii >= 0 && ii < W && jj >= 0 && jj < W)
                                {
                                    std::string next1 = curr[i][j][sum];
                                    int sum1 = sum;
                                    next1.push_back(M[ii][j]);
                                    next1.push_back(M[ii][jj]);
                                    if (M[ii][j] == '+')
                                        sum1 += M[ii][jj] - '0';
                                    else
                                        sum1 -= M[ii][jj] - '0';
                                    if (sum1 >= 0 && sum1 < MAX * 2 
                                        && (next[ii][jj][sum1].empty() || mygreater(next[ii][jj][sum1], next1)))
                                    {
                                        next[ii][jj][sum1] = next1;
                                    }

                                    std::string next2 = curr[i][j][sum];
                                    int sum2 = sum;
                                    next2.push_back(M[i][jj]);
                                    next2.push_back(M[ii][jj]);
                                    if (M[i][jj] == '+')
                                        sum2 += M[ii][jj] - '0';
                                    else
                                        sum2 -= M[ii][jj] - '0';
                                    if (sum2 >= 0 && sum2 < MAX * 2 
                                        && (next[ii][jj][sum2].empty() || mygreater(next[ii][jj][sum2], next2)))
                                    {
                                        next[ii][jj][sum2] = next2;
                                    }
                                }
                                // go back to current one
                                ii = i + dx1[k];
                                jj = j + dy1[k];
                                if (ii >= 0 && ii < W && jj >= 0 && jj < W)
                                {
                                    std::string next1 = curr[i][j][sum];
                                    int sum1 = sum;
                                    next1.push_back(M[ii][jj]);
                                    next1.push_back(M[i][j]);
                                    if (M[ii][jj] == '+')
                                        sum1 += M[i][j] - '0';
                                    else
                                        sum1 -= M[i][j] - '0';
                                    if (sum1 >= 0 && sum1 < MAX * 2 
                                        && (next[i][j][sum1].empty() || mygreater(next[i][j][sum1], next1)))
                                    {
                                        next[i][j][sum1] = next1;
                                    }
                                }
                                // straight move
                                int ii1 = i + dx1[k] * 2;
                                int jj1 = j + dy1[k] * 2;
                                if (ii >= 0 && ii < W && jj >= 0 && jj < W
                                    && ii1 >= 0 && ii1 < W && jj1 >= 0 && jj1 < W)
                                {
                                    std::string next1 = curr[i][j][sum];
                                    int sum1 = sum;
                                    next1.push_back(M[ii][jj]);
                                    next1.push_back(M[ii1][jj1]);
                                    if (M[ii][jj] == '+')
                                        sum1 += M[ii1][jj1] - '0';
                                    else
                                        sum1 -= M[ii1][jj1] - '0';
                                    if (sum1 >= 0 && sum1 < MAX * 2 
                                        && (next[ii1][jj1][sum1].empty() || mygreater(next[ii1][jj1][sum1], next1)))
                                    {
                                        next[ii1][jj1][sum1] = next1;
                                    }
                                }
                            }
                        }
                    }
                }
            }

            curr = next;
        }
        for (int i = 0 ; i < Q ; ++i)
            std::cout << queries[q[i] + MAX] << "\n";
    }
    return 0;
}
