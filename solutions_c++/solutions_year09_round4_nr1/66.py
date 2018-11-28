#include <fstream>
#include <cmath>
using namespace std;
ofstream fout ("a1.out");
ifstream fin ("a1.in");

int tt,n;
char ma[60][60];
int tmm[60];
int main()
    {
        fin >> tt;
        for (int al=0; al<tt; al++)
            {
                fin >> n;
                for (int i=0; i<n; i++)
                    for (int j=0; j<n; j++)
                        fin >> ma[i][j];
                int an=0;
                for (int i=0; i<n; i++)
                    {
                    for (int j=i+1; j<n; j++)
                        {
                            if (ma[i][j]=='1')
                                {
                                    for (int k=i+1; k<n; k++)
                                        {
                                            bool flag=0;
                                            for (int x=i+1; x<n; x++)
                                                if (ma[k][x]=='1')
                                                    {
                                                        flag=1;
                                                        break;
                                                    }
                                            if (!flag)
                                                {
                                                    for (int x=0; x<n; x++)
                                                        tmm[x]=ma[k][x];
                                                    for (int y=k; y>i; y--)
                                                        for (int x=0; x<n; x++)
                                                            ma[y][x]=ma[y-1][x];
                                                    for (int x=0; x<n; x++)
                                                        ma[i][x]=tmm[x];
                                                    an+=k-i;
                                                    break;
                                                }
                                        }
                                    break;
                                }
                        }
                    }
                    fout << "Case #" << al+1 << ": " << an << endl;
            }
    }
