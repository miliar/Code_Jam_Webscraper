#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int case_N, NA, NB, ans_A, ans_B, turn_T, rem_A, rem_B;
ifstream fin;
ofstream fout;
string sTmp;

struct trip {
       int dep;
       int arr;
};

vector<trip> A_to_B;
vector<trip> B_to_A;


int strToTime(string str)
{
    return ((int(str[0])-48)*600+(int(str[1])-48)*60+(int(str[3])-48)*10+(int(str[4])-48));
}

bool cmp(trip A, trip B)
{
     if (A.dep != B. dep) return (A.dep < B.dep);
     else return (A.arr < B.arr);
}

int main()
{
    fin.open("B-small-attempt0.in");
    fout.open("B-small-attempt0.out");       
    
    
    fin >> case_N;
    for (int n = 1; n <= case_N; ++n)
    {
        //=============================== INPUT ================================
        A_to_B.clear();
        B_to_A.clear();
        ans_A = 0;
        ans_B = 0;
        rem_A = 0;
        rem_B = 0;
        vector<int> depA;
        vector<int> depB;
        
        
        fin >> turn_T;
        fin >> NA >> NB;
        for (int i = 0; i < NA; ++i) 
        {
            trip tTmp;
            fin >> sTmp;
            tTmp.dep = strToTime(sTmp);
            fin >> sTmp;
            tTmp.arr = strToTime(sTmp) + turn_T;
            A_to_B.push_back(tTmp);
        }
        sort(A_to_B.begin(), A_to_B.end(), cmp);

        for (int i = 0; i < NB; ++i) 
        {
            trip tTmp;
            fin >> sTmp;
            tTmp.dep = strToTime(sTmp);
            fin >> sTmp;
            tTmp.arr = strToTime(sTmp) + turn_T;
            B_to_A.push_back(tTmp);
        }
        sort(B_to_A.begin(), B_to_A.end(), cmp);

        //=============================== OUTPUT ===============================    
        vector<trip>::iterator iterA = A_to_B.begin(), iterB = B_to_A.begin();
        while ((iterA != A_to_B.end()) || (iterB != B_to_A.end()))
        {
              if (iterA == A_to_B.end()) {
                  if (depB.empty() || ((*depB.begin()) > (*iterB).dep))
                  {
                      depA.push_back((*iterB).arr);
                      sort(depA.begin(),depA.end());
                      ans_B++;
                  } else {
                      depB.erase(depB.begin());
                      sort(depB.begin(),depB.end());
                      depA.push_back((*iterB).arr);
                  }
                  iterB++;
              } else if (iterB == B_to_A.end()) {
                  if (depA.empty() || ((*depA.begin()) > (*iterA).dep))
                  {
                      depB.push_back((*iterA).arr);
                      sort(depB.begin(),depB.end());
                      ans_A++;
                  } else {
                      depA.erase(depA.begin());
                      sort(depA.begin(),depA.end());
                      depB.push_back((*iterA).arr);
                  }
                  iterA++;
              } else {  
                  if (cmp(*iterA, *iterB)) {
                      if (depA.empty() || ((*depA.begin()) > (*iterA).dep))
                      {
                          depB.push_back((*iterA).arr);
                          sort(depB.begin(),depB.end());
                          ans_A++;
                      } else {
                          depA.erase(depA.begin());
                          sort(depA.begin(),depA.end());
                          depB.push_back((*iterA).arr);
                      }
                      iterA++;
                  } else {
                      if (depB.empty() || ((*depB.begin()) > (*iterB).dep))
                      {
                          depA.push_back((*iterB).arr);
                          sort(depA.begin(),depA.end());
                          ans_B++;
                      } else {
                          depB.erase(depB.begin());
                          sort(depB.begin(),depB.end());
                          depA.push_back((*iterB).arr);
                      }
                      iterB++;
                  }
              }
        }
        fout << "Case #" << n << ": " << ans_A << " " << ans_B << endl;
    }
    fin.close();
    fout.close();
    system("PAUSE");
    return 0;
}    
    
    
