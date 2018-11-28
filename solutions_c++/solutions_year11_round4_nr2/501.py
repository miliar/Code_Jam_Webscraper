#include <iostream>
#include <fstream>
using namespace std;

int M[510][510];
double X[510][510], Y[510][510];
double cX[510][510], cY[510][510], cM[510][510];

	
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
	
	int T, R, C, D;
    fin >> T;
    int ans = 0;
		
    for (int i = 1 ; i <= T ; i++)
    {    
        fin >> R >> C >> D;
		
		char f;
		for (int j = 0 ; j <= R ; j++)
			for (int k = 0 ; k <= C ; k++)
            	{cX[j][k] = 0; cY[j][k] = 0; cM[j][k] = 0;}
				
		for (int j = 1 ; j <= R ; j++)
			for (int k = 1 ; k <= C ; k++)
			{
				fin >> f;
				M[j][k] = (int)f-48;
				M[j][k] += D;
				X[j][k] = (j)*M[j][k];
				Y[j][k] = (k)*M[j][k];				
				if (k == 1) {cX[j][k] = X[j][k]; cY[j][k] = Y[j][k]; cM[j][k] = M[j][k];}
				else {
					cX[j][k] = cX[j][k-1] + X[j][k];
					cY[j][k] = cY[j][k-1] + Y[j][k];
					cM[j][k] = cM[j][k-1] + M[j][k];
				}
			    //fout << j << " " << k << " : " << cM[j][k] << endl;
			}
		
		bool check = false;

		int s = (C<R)? C:R; 
		for (;s>=3;s--)
		{			
			for (int j = 1 ; j <= R-s+1 ; j++)
			{
				for (int k = 1 ; k <= C-s+1 ; k++)
				{
					double xTotal = 0; 
					double yTotal = 0;
					double mTotal = 0;
					for (int ss = 0 ; ss < s ; ss++)
					{
                        if (ss == 0 || ss == s-1)
                        {
                        	xTotal += cX[j+ss][k+s-2]-cX[j+ss][k];
							yTotal += cY[j+ss][k+s-2]-cY[j+ss][k];
	         				mTotal += cM[j+ss][k+s-2]-cM[j+ss][k]; 
                        }
                        else
                        {
							xTotal += cX[j+ss][k+s-1]-cX[j+ss][k-1];
							yTotal += cY[j+ss][k+s-1]-cY[j+ss][k-1];
	         				mTotal += cM[j+ss][k+s-1]-cM[j+ss][k-1];
						}
					}
					//fout << "s: " << s << " j: " << j << " k: " << k << endl;
					//fout << "x: " << xTotal << " y: " << yTotal << " m: " << mTotal << endl;
					if (xTotal == mTotal * ((double)(j+j+s-1)/2.0) && yTotal == mTotal * ((double)(k+k+s-1)/2.0))
						{ans = s; check = true; break;}
				}
				if (check == true) break;
			}
			if (check == true) break;
		}
		
        fout << "Case #" << i << ": ";  
		if (check == true) fout << ans;
		else fout << "IMPOSSIBLE";
        fout << endl;
    }
}



