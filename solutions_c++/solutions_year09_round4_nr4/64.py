#include <fstream>
#include <cmath>
using namespace std;
ofstream fout ("d1.out");
ifstream fin ("d1.in");

int c,n;
double x[100],y[100],r[100];
double dis(double x1, double y1, double x2, double y2)
    {
        return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
    }
int main()
    {
        fin >> c;
        fout.precision(6);
        fout.setf(ios::fixed);
        for (int al=0; al<c; al++)
            {
                fin >> n;
                for (int i=0; i<n; i++)
                    fin >> x[i] >> y[i] >> r[i];
                double mi=1992837465;
                if (n==3)
                    {
                        for (int i=0; i<n; i++)
                            for (int j=i+1; j<n; j++)
                                {
                                    int rr;
                                    for (int k=0; k<n; k++)
                                        if ((k!=i)||(k!=j))
                                            {
                                                rr=k;
                                                break;
                                            }
                                    mi=min(mi,max(r[i]+r[j]+dis(x[i],y[i],x[j],y[j]),r[rr]+r[rr]));
                                }
                        mi=mi/2;
                    }
                else
                if (n==2)
                    {
                        mi=max(r[0],r[1]);
                    }
                else
                    mi=r[0];
                fout << "Case #" << al+1 << ": " << mi << endl;
            }
    }
