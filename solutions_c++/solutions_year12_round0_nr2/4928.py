#include <stdlib.h>
#include <fstream>
#include <iostream>

void set_points(int sum, int p[3])
{
    int rem_sum = sum;
    
    if (rem_sum > p[0])
        {
            rem_sum -= p[0];
            
            if (rem_sum > p[1])
                {
                    rem_sum -= p[1];
                    
                    p[2] = rem_sum;
                }
            else
                {
                    if ((p[1] - 1) != -1)
                        {
                            --p[1];
                            
                            set_points(sum, p);
                        }
                    else if ((p[0] - 1) != -1)
                        {
                            --p[0];
                            set_points(sum, p);
                        }
                }
        }
    else if ((p[0] - 1) != -1)
        {
            --p[0];
            set_points(sum, p);
        }
}

void adjust(int p[3])
{
    bool flag;
    do
    {
        flag = false;
        
        int diff = p[0] - p[1];
        
        if (diff > 1)
            {
                --p[0];
                ++p[1];
                flag = true;
            }
        else if (diff < -1)
            {
                ++p[0];
                --p[1];
                flag = true;
            }
            
        diff = p[1] - p[2];
        
        if (diff > 1)
            {
                --p[1];
                ++p[2];
                flag = true;
            }
        else if (diff < -1)
            {
                ++p[1];
                --p[2];
                flag = true;
            }

        diff = p[2] - p[0];
        
        if (diff > 1)
            {
                --p[2];
                ++p[0];
                flag = true;
            }
        else if (diff < -1)
            {
                ++p[2];
                --p[0];
                flag = true;
            }
    }
    while (flag == true);
}

void set_surprising(int b, int n, int num, int p[100][3])
{
    int count = 0, completed[100];
    
    for (int i = 0; i < num; ++i)
        {
            completed[i] = 0;
        }
    
    for (int i = 0; i < num; ++i)
        {
            if (count == n)
                {
                    break;
                }
            else if (completed[i] == 1)
                {
                    continue;
                }
            else if (p[i][0] >= b)
                {
                    continue;
                }
            else if (p[i][1] >= b)
                {
                    continue;
                }
            else if (p[i][2] >= b)
                {
                    continue;
                }
            else if ((b - p[i][0]) == 1)
                {
                    if ((p[i][0] - p[i][1]) == 0)
                        {
                            if ((p[i][0] < 10) && (p[i][1] > 0))
                            {
                                ++p[i][0];
                                --p[i][1];
                            
                                ++count;
                                completed[i] = 1;
                            }
                        }
                    else if ((p[i][0] - p[i][2]) == 0)
                        {
                            if ((p[i][0] < 10) && (p[i][2] > 0))
                            {
                                ++p[i][0];
                                --p[i][2];
                            
                                ++count;
                                completed[i] = 1;
                            }
                        }
                }
            else if ((b - p[i][1]) == 1)
                {
                    if ((p[i][1] - p[i][2]) == 0)
                        {
                            if ((p[i][1] < 10) && (p[i][2] > 0))
                            {
                                ++p[i][1];
                                --p[i][2];
                            
                                ++count;
                                completed[i] = 1;
                            }
                        }
                    else if ((p[i][1] - p[i][0]) == 0)
                        {
                            if ((p[i][1] < 10) && (p[i][0] > 0))
                            {
                                ++p[i][1];
                                --p[i][0];
                        
                                ++count;
                                completed[i] = 1;
                            }
                        }
                }
            else if ((b - p[i][2]) == 1)
                {
                    if ((p[i][2] - p[i][0]) == 0)
                        {
                            if ((p[i][2] < 10) && (p[i][0] > 0))
                            {
                                ++p[i][2];
                                --p[i][0];
                            
                                ++count;
                                completed[i] = 1;
                            }
                        }
                    else if ((p[i][2] - p[i][1]) == 0)
                        {
                            if ((p[i][2] < 10) && (p[i][1] > 0))
                            {
                                ++p[i][2];
                                --p[i][1];
                            
                                ++count;
                                completed[i] = 1;
                            }
                        }
                }
        }
    
    if (count < n)
        {
            for (int i = 0; i < num; ++i)
                {
                    if (count == n)
                    {
                        break;
                    }
                    else if (completed[i] == 1)
                        {
                            continue;
                        }
                    else if ((p[i][0] - p[i][1]) == 0)
                        {
                            if ((p[i][0] < 10) && (p[i][1] > 0))
                            {
                                ++p[i][0];
                                --p[i][1];
                            
                                ++count;
                                completed[i] = 1;
                            }
                        }
                    else if ((p[i][1] - p[i][2]) == 0)
                        {
                            if ((p[i][1] < 10) && (p[i][2] > 0))
                            {
                                ++p[i][1];
                                --p[i][2];
                            
                                ++count;
                                completed[i] = 1;
                            }
                        }
                    else if ((p[i][2] - p[i][0]) == 0)
                        {
                            if ((p[i][2] < 10) && (p[i][0] > 0))
                            {
                                ++p[i][2];
                                --p[i][0];
                            
                                ++count;
                                completed[i] = 1;
                            }
                        }
                }
        }
}

int main(int argc, char** argv)
{
    std::ifstream f1;
    std::ofstream f2;

    f1.open("B-large-0.in");
    f2.open("B-large-0.out");

    int T, N, S, p, ti[100], pi[100][3], result;

    f1 >> T;

    for (int i = 1; i <= T; ++i)
        {
            f1 >> N >> S >> p;
            
            for (int j = 0; j < N; ++j)
                {
                    f1 >> ti[j];
                    
                    if (ti[j] < 3)
                    {
                        if (ti[j] == 0)
                        {
                            pi[j][0] = pi[j][1] = pi[j][2] = 0;
                        }
                        else if (ti[j] == 1)
                            {
                                pi[j][0] = 1;
                                pi[j][1] = pi[j][2] = 0;
                            }
                        else if (ti[j] == 2)
                            {
                                pi[j][0] = pi[j][1] = 1;
                                pi[j][2] = 0;
                            }
                        
                    }
                    else
                    {
                        pi[j][0] = pi[j][1] = pi[j][2] = 10;
                    }
                }
            
            for (int j = 0; j < N; ++j)
                {                    
                    set_points(ti[j], pi[j]);
                    
                    adjust(pi[j]);

                }
                
            set_surprising(p, S, N, pi);
            
            result = 0;
            
            for (int j = 0; j < N; ++j)
                {
                    for (int k = 0; k < 3; ++k)
                        {
                            if (pi[j][k] >= p)
                                {
                                    ++result;
                                    break;
                                }
                        }
                }
                
            f2 << "Case #" << i << ": " << result << "\n";
        }
        
        f1.close();
        f2.close();

    return (EXIT_SUCCESS);
}
