#include <fstream>
using namespace std;
int pos[1000][3],pow[1000];
void main()
{
	int n,CASE;
	ifstream in ("input.in");
	ofstream out ("output.out");
	in >> n;
	for(CASE=0;CASE<n;CASE++)
	{
		int m;
		double avg[3]={0,};
		int i,j;
		in >> m;
		for(i=0;i<m;i++)
		{
			in >> pos[i][0] >> pos[i][1] >> pos[i][2] >> pow[i];
		}
		double max=0.0;
		for(i=0;i<m;i++)
			for(j=i+1;j<m;j++)
			{
				double diff[3];
				diff[0]=pos[i][0]-pos[j][0]; if(diff[0]<0) diff[0]*=-1.0;
				diff[1]=pos[i][1]-pos[j][1]; if(diff[1]<0) diff[1]*=-1.0;
				diff[2]=pos[i][2]-pos[j][2]; if(diff[2]<0) diff[2]*=-1.0;
				double req=(diff[0]+diff[1]+diff[2])/(double)(pow[i]+pow[j]);
				if(max<req)
					max=req;
			}
		char str[20]="";
		sprintf(str,"%.6f",max);
		out << "Case #" << CASE+1 << ": " << str << endl;
	}
	out.close();
	in.close();
}