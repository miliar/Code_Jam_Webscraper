#include <iostream>
#include <cstdlib>
#include <string>
#include <map>

using namespace std;

int tt[25][61];

int main()
{
    int N, T, NA, NB;
    
    cin >> N;
    
    char strDep[64], strArr[64];
    char *p;
    int hour, minute;
    
    int m_A_arr[24*60], m_A_dep[24*60], m_B_arr[24*60], m_B_dep[24*60], add_tr_A[24*60], add_tr_B[24*60];
    
    for(int i = 0; i < N; i++)
    {
            for(int j = 0; j < 24*60; j++)
            {
                    m_A_arr[j] = 0;
                    m_A_dep[j] = 0;
                    m_B_arr[j] = 0;
                    m_B_dep[j] = 0; 
                    
                    add_tr_A[j] = 0;
                    add_tr_B[j] = 0;
            }            
            
            cin >> T;
            cin >> NA;
            cin >> NB;
            
            for(int j = 0; j < NA; j++)
            {
                    cin >> strDep;
                    cin >> strArr;  
                    
                    p = strtok(strDep, ":");
                    sscanf(p, "%d", &hour);
                    p = strtok(NULL, "");
                    sscanf(p, "%d", &minute);  
                    
                    m_A_dep[hour*60 + minute]++;
                    
                    p = strtok(strArr, ":");
                    sscanf(p, "%d", &hour);
                    p = strtok(NULL, "");
                    sscanf(p, "%d", &minute);  
                    
                    m_B_arr[hour*60 + minute]++;                
            }
            for(int j = 0; j < NB; j++)
            {
                    cin >> strDep;
                    cin >> strArr;  
                    
                    p = strtok(strDep, ":");
                    sscanf(p, "%d", &hour);
                    p = strtok(NULL, "");
                    sscanf(p, "%d", &minute);  
                    
                    m_B_dep[hour*60 + minute]++;
                    
                    p = strtok(strArr, ":");
                    sscanf(p, "%d", &hour);
                    p = strtok(NULL, "");
                    sscanf(p, "%d", &minute);  
                    
                    m_A_arr[hour*60 + minute]++;                
            }

            int tr_a = 0, tr_b = 0, needed_a = 0, needed_b = 0;           
            for(int j = 0; j < 60*24; j++)
            {
                    if(m_A_arr[j] > 0)
                    {
                             add_tr_A[j + T] += m_A_arr[j];
                    }
                    
                    if(m_B_arr[j] > 0)
                    {
                             add_tr_B[j + T] += m_B_arr[j];
                    }
                    
                    if(add_tr_A[j] > 0)
                    {
                             tr_a += add_tr_A[j];         
                    }
                    
                    if(add_tr_B[j] > 0)
                    {
                             tr_b += add_tr_B[j];         
                    }

                    if(m_A_dep[j] > 0)
                    {
                             if(tr_a < m_A_dep[j])
                             {
                                     needed_a += (m_A_dep[j] - tr_a);
                                     tr_a = 0;    
                             }
                             else
                             {
                                 tr_a -= m_A_dep[j];    
                             }         
                    }
                    
                    if(m_B_dep[j] > 0)
                    {
                             if(tr_b < m_B_dep[j])
                             {
                                     needed_b += (m_B_dep[j] - tr_b);
                                     tr_b = 0;    
                             }
                             else
                             {
                                 tr_b -= m_B_dep[j];    
                             }         
                    }
                    
            }
            
            cout << "Case #" << i + 1 << ": " << needed_a << " " << needed_b << endl;
    }
}
