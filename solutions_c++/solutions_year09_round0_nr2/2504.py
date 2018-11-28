#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int water(int map[100][100],int i,int j,int H, int W)
{
	int d, min,direction,posi,posj;	

	min=map[i][j];
	direction=0;
	for(d=1;d<=4;d++)
	{
		posi=i;
		posj=j;		
		switch (d) {
			case 1: posi--; break;
			case 2: posj--; break;
			case 3: posj++; break;
			case 4: posi++; break;
			default: break;
		}
		if(posi>=0 && posi<H && posj>=0 && posj<W)
			if(map[posi][posj]<min)
			{
				min=map[posi][posj];
				direction=d;
			}
	}
		
	return direction;
}

int main (int argc, char * const argv[]) {
    // insert code here...
	int i,j,k,T,H,W,l,posi,posj,direction;
	int map[100][100];
	int label[100][100];
	
	ifstream myfile("/Users/Ashkan/Documents/Programming/Input/B-large.in");
	ofstream output("/Users/Ashkan/Documents/Programming/Output/B-large.out");
	
	if (myfile.is_open())
	{
		myfile >> T;
		for(k=1;k<=T;k++)
		{
			myfile >> H;
			myfile >> W;
			for(i=0; i<H;i++)
				for(j=0;j<W;j++)
				{
					myfile >> map[i][j];
					label[i][j]=0;
				}
			
			l=1;
			for(i=0;i<H;i++)
				for(j=0;j<W;j++)
				{
					posi=i;
					posj=j;
					direction=water(map,posi,posj,H,W);
					while(direction!=0)
					{
						switch (direction) {
							case 1: posi--; break;
							case 2: posj--; break;
							case 3: posj++; break;
							case 4: posi++; break;
							default: break;
						}
						direction=water(map,posi,posj,H,W);
					}
					if (label[posi][posj]!=0)
						label[i][j]=label[posi][posj];
					else
					{
						label[i][j]=label[posi][posj]=l;
						l++;
					}
				}
			
			output <<"Case #"<<k<<":"<<endl;
			for(i=0; i<H;i++)
			{
				for(j=0;j<W;j++)
					output << (char)(label[i][j]-1+((int) 'a'))<<" ";
				output <<endl;
			}
		}
			myfile.close();
			output.close();
					
	}
	else cout << "Unable to open file"; 	
    return 0;
}
