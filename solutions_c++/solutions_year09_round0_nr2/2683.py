#include <iostream>
#include <stdlib.h>

#include <list> 

#define ALL 31
#define NO 1
#define NORTH 2
#define WEST 4
#define EAST 8
#define SOUTH 16

using namespace std;

class Pair {
public:
	int x, y;
	Pair(int xx,int yy) {x=xx;y=yy;}
};

int main() {
	list<Pair*> L;
	int testcases;
	cin >> testcases;
	for(int i=0; i<testcases; i++)
	{
		int H, W, SZ, HH, WW;
		cin >> H >> W;
		HH = H+2; WW = W+2;
		SZ = HH * WW;

		int* alt = (int*) calloc(SZ, sizeof(int));
		char* out = (char*) calloc(SZ, sizeof(char));
		char* slope = (char*) calloc(SZ, sizeof(char));
		for(int j=0; j<HH; j++)
		{
			alt[j*WW + WW-1] = 10000;
 			alt[j*WW + 0   ] = 10000;
		}
		for(int k=0; k<WW; k++)
		{
                        alt[0     *WW + k] = 10000;
                        alt[(HH-1)*WW + k] = 10000;
                } 
		for(int j=1; j<HH-1; j++)
			for(int k=1; k<WW-1; k++) 
			{
				cin >> alt[j*WW + k];
			}
		for(int j=1; j<HH-1; j++)
		{
                        for(int k=1; k<WW-1; k++)
                        {
				if((alt[(j-1)*WW + k] >= alt[j*WW + k]) &&
				   (alt[(j+1)*WW + k] >= alt[j*WW + k]) &&
                                   (alt[j*WW + (k-1)] >= alt[j*WW + k]) &&
                                   (alt[j*WW + (k+1)] >= alt[j*WW + k])  )
				{
					slope[j*WW + k] |= NO;
					continue;
				}
				if(alt[(j-1)*WW + k] <= alt[j*WW + (k-1)]) { //N:w
					if(alt[(j-1)*WW + k] <= alt[j*WW + (k+1)]) { //N:e
						if(alt[(j-1)*WW + k] <= alt[(j+1)*WW + k]) { //N:s
							slope[j*WW + k] |= NORTH;
							slope[(j-1)*WW + k] |= SOUTH;
						} else { //S:n
							slope[j*WW + k] |= SOUTH;
							slope[(j+1)*WW + k] |= NORTH;
	                                        }
					} else { //E:n
                                                if(alt[j*WW + (k+1)] <= alt[(j+1)*WW + k]) { //E:s
							slope[j*WW + k] |= EAST;
							slope[j*WW + (k+1)] |= WEST;
                                                } else { //S:e
							slope[j*WW + k] |= SOUTH;
							slope[(j+1)*WW + k] |= NORTH;
                                                }
					}
				} else { //W:n
					if(alt[j*WW + (k-1)] <= alt[j*WW + (k+1)]) { //W:e
                                                if(alt[j*WW + (k-1)] <= alt[(j+1)*WW + k]) { //W:s
							slope[j*WW + k] |= WEST;
							slope[j*WW + (k-1)] |= EAST;
                                                } else { //S:w
							slope[j*WW + k] |= SOUTH;
							slope[(j+1)*WW + k] |= NORTH;
                                                }
                                        } else { //E:w
                                                if(alt[j*WW + (k+1)] <= alt[(j+1)*WW + k]) { //E:s
							slope[j*WW + k] |= EAST;
							slope[j*WW + (k+1)] |= WEST;
                                                } else { //S:e
							slope[j*WW + k] |= SOUTH;
							slope[(j+1)*WW + k] |= NORTH;
                                                }
                                        }
				}
                        }
		}

		char current = 'a';
		for(int j=1; j<HH-1; j++)
                {
                        for(int k=1; k<WW-1; k++)
                        {
				if(out[j*WW + k] == 0) 
				{
					L.push_back(new Pair(j,k));
				
					while (!L.empty()) {
						Pair* tmp=L.back();
						int jj=tmp->x, kk=tmp->y;
						//cout << "("<<jj << ","<< kk<<")" ;
						L.pop_back();
						delete(tmp);
						if (jj<=0 || jj>=HH-1 || kk<=0 || kk>=WW-1 || out[jj*WW + kk]!=0 )
							continue;

						out[jj*WW + kk] = current;

						if(slope[jj*WW + kk] & NORTH) {
                                        	        //out[(jj-1)*WW + kk] = out[jj*WW + kk];
							L.push_back(new Pair(jj-1,kk));
	                                        }
						if(slope[jj*WW + kk] & WEST) {
                	                                //out[jj*WW + (kk-1)] = out[jj*WW + kk];
							L.push_back(new Pair(jj,kk-1));
                                	        }
						if(slope[jj*WW + kk] & EAST) {
							//out[jj*WW + (kk+1)] = out[jj*WW + kk];
							L.push_back(new Pair(jj,kk+1));
						}
						if(slope[jj*WW + kk] & SOUTH) {
                                	        	//out[(jj+1)*WW + kk] = out[jj*WW + kk];
							L.push_back(new Pair(jj+1,kk));
						} 	
					}
					current++;
				}
			}
		}
		
		cout << "Case #" << i+1 << ":\n";
                for(int j=1; j<HH-1; j++)
                {
                        for(int k=1; k<WW-1; k++)
                        {
				cout << out[j*WW + k] << " ";
 			}
			cout << "\n";
		}
	}
	return 1;
}
